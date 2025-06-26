# clinic_agent

A LangChain-based research assistant specialized for clinical trial design.

## Changelog

- **v0.2**
  - manage the project with `uv`
  - provide a console interface using `click`
  - integrate Tavily search
  - implement a ReAct-style agent (think then act)
  - load configuration from a `.env` file
- configure the LLM endpoint and model via environment variables
- optional proxy support for network access
- disable SSL certificate verification with `DISABLE_SSL_VERIFY`
- see `prompt/clinic_agent.md` for the initial prompt design
- extract a PDF paper or patent to Markdown before running the agent
- **v0.1**
  - develop a working prompt

## Usage

1. Install dependencies using [`uv`](https://github.com/astral-sh/uv):
   ```bash
   uv pip install -r pyproject.toml
   ```
2. Copy `.env.example` to `.env` and fill in your API keys. You can also
   specify `OPENAI_API_BASE`, `OPENAI_MODEL`, or `HTTPS_PROXY` for a custom
   endpoint, model, or network proxy. Set `DISABLE_SSL_VERIFY=1` to skip
   certificate validation if necessary.
3. Run the agent with a question:
   ```bash
   clinic_agent "What are the latest trials for CAR T therapy?"
   ```
   Or process a PDF directly:
   ```bash
   clinic_agent --pdf /path/to/paper.pdf
   ```
   Without an argument the command enters an interactive session. Type `exit` to quit.
