import os
import sys
from pathlib import Path
from typing import Any

import click
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.prompts import PromptTemplate
import fitz  # PyMuPDF

try:  # openai is an optional dependency of langchain-openai
    import openai
except Exception:  # pragma: no cover - openai not installed
    openai = None  # type: ignore


def create_agent(language: str = "en") -> Any:
    """Create the LangChain agent using OpenAI chat model and Tavily search."""
    if os.getenv("DISABLE_SSL_VERIFY"):
        os.environ["CURL_CA_BUNDLE"] = ""
        os.environ["REQUESTS_CA_BUNDLE"] = ""
        if openai is not None:  # pragma: no cover - openai optional
            openai.verify_ssl_certs = False  # type: ignore[attr-defined]

    model = os.getenv("OPENAI_MODEL")
    api_base = os.getenv("OPENAI_API_BASE")
    proxy = os.getenv("HTTPS_PROXY")

    llm_kwargs: dict[str, Any] = {"temperature": 0}
    if model:
        click.echo(f"Using model: {model}")
        llm_kwargs["model"] = model
    if api_base:
        llm_kwargs["base_url"] = api_base
    if proxy:
        click.echo(f"Using proxy: {proxy}")
        llm_kwargs["proxy"] = proxy

    llm = ChatOpenAI(**llm_kwargs)
    search_tool = TavilySearch(max_results=5)
    tools = [search_tool]

    prompt_path = Path(__file__).parent / "prompt" / "clinic_agent.md"
    template = prompt_path.read_text(encoding="utf-8")
    if language == "cn":
        template += "\n\nPlease provide the final answer in Chinese."
    else:
        template += "\n\nPlease provide the final answer in English."
    prompt = PromptTemplate.from_template(template)
    agent = create_openai_tools_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)


def pdf_to_markdown(pdf_path: str) -> str:
    """Extract text from a PDF and save it as a Markdown file."""
    click.echo(f"Extracting and refining text from {pdf_path}...")
    doc = fitz.open(pdf_path)
    
    refine_prompt_path = Path(__file__).parent / "prompt" / "refine_pdf_prompt.md"
    refine_template = refine_prompt_path.read_text(encoding="utf-8")
    refine_prompt = PromptTemplate.from_template(refine_template)
    llm = ChatOpenAI()
    chain = refine_prompt | llm
    
    refined_texts = []
    for i, page in enumerate(doc):
        click.echo(f"Processing page {i+1}/{len(doc)}...")
        raw_text = page.get_text()
        if raw_text.strip():
            refined_page_text = chain.invoke({"raw_text": raw_text}).content
            refined_texts.append(refined_page_text)
            
    doc.close()
    
    final_text = "\n\n".join(refined_texts)

    if not final_text.strip():
        raise ValueError("Failed to extract text from PDF. The PDF file might be protected or images.")

    md_path = Path(pdf_path).with_suffix(".md")
    md_path.write_text(final_text, encoding="utf-8")
    return final_text


@click.command()
@click.argument("query", required=False)
@click.option("-f", "--file", "file_path", type=click.Path(exists=True, dir_okay=False), help="Path to the input file (PDF or Markdown)")
@click.option("-o", "--output", "output_path", type=click.Path(), help="Path to save the output markdown file")
@click.option("--lang", "language", type=click.Choice(['en', 'cn']), default='en', help="Language for the final report")
def cli(query: str | None = None, file_path: str | None = None, output_path: str | None = None, language: str = 'en') -> None:
    """Run the clinic agent once or enter an interactive loop."""
    load_dotenv()
    agent = create_agent(language)

    if file_path:
        path = Path(file_path)
        if path.suffix == ".pdf":
            md_path = path.with_suffix(".md")
            if md_path.exists():
                click.echo(f"Using existing markdown file: {md_path}")
                query = md_path.read_text(encoding="utf-8")
            else:
                query = pdf_to_markdown(file_path)
        else:
            query = path.read_text(encoding="utf-8")

    if query:
        result = agent.invoke({"input": query})
        output = result["output"]
        if output_path:
            Path(output_path).write_text(output, encoding="utf-8")
            click.echo(f"Report saved to {output_path}")
        else:
            click.echo(output)
        return

    # Interactive loop
    while True:
        try:
            user_input = click.prompt("Input", default="", show_default=False)
        except (EOFError, KeyboardInterrupt):
            break
        if user_input.lower() in {"exit", "quit"}:
            break
        answer = agent.invoke({"input": user_input})
        output = answer["output"]
        if output_path:
            Path(output_path).write_text(output, encoding="utf-8")
            click.echo(f"Report saved to {output_path}")
        else:
            click.echo(output)


if __name__ == "__main__":
    cli()

