import os
from pathlib import Path
from typing import Any

import click
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from pypdf import PdfReader

try:  # openai is an optional dependency of langchain-openai
    import openai
except Exception:  # pragma: no cover - openai not installed
    openai = None  # type: ignore


def create_agent() -> Any:
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
        llm_kwargs["model"] = model
    if api_base:
        llm_kwargs["base_url"] = api_base
    if proxy:
        llm_kwargs["proxy"] = proxy
    llm = ChatOpenAI(**llm_kwargs)
    search_tool = TavilySearchResults(max_results=5)
    tools = [search_tool]
    return initialize_agent(
        tools,
        llm,
        agent=AgentType.REACT_DOCSTORE,
        verbose=True,
    )


def pdf_to_markdown(pdf_path: str) -> str:
    """Extract text from a PDF and save it as a Markdown file."""
    reader = PdfReader(pdf_path)
    text = "\n\n".join(page.extract_text() or "" for page in reader.pages)
    md_path = Path(pdf_path).with_suffix(".md")
    md_path.write_text(text)
    return text


@click.command()
@click.argument("query", required=False)
@click.option("--pdf", "pdf_path", type=click.Path(exists=True, dir_okay=False), help="PDF file to process")
def cli(query: str | None = None, pdf_path: str | None = None) -> None:
    """Run the clinic agent once or enter an interactive loop."""
    load_dotenv()
    agent = create_agent()

    if pdf_path:
        query = pdf_to_markdown(pdf_path)

    if query:
        result = agent.run(query)
        click.echo(result)
        return

    # Interactive loop
    while True:
        try:
            user_input = click.prompt("Input", default="", show_default=False)
        except (EOFError, KeyboardInterrupt):
            break
        if user_input.lower() in {"exit", "quit"}:
            break
        answer = agent.run(user_input)
        click.echo(answer)


if __name__ == "__main__":
    cli()

