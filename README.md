# clinic_agent

A LangChain-based research assistant specialized for clinical trial design.

## Changelog

 - [x] **v0.3**
  - create tests for the project
  - create bootstrap.sh for the project
  - make sure all the listed tests are passed
  - please investigate how to implement the agent, please reference `clinic_agent\prompt\clinic_agent.md`  
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
   uv sync
   ```
2. Copy `.env.example` to `.env` and fill in your API keys. You can also
   specify `OPENAI_API_BASE`, `OPENAI_MODEL`, or `HTTPS_PROXY` for a custom
   endpoint, model, or network proxy. Set `DISABLE_SSL_VERIFY=1` to skip
   certificate validation if necessary.
   ```
   cp .env.example .env
   ```
3. Install the package
    ```
    uv pip install .
    ```
5. Run the agent with a question:
   - test 1
   ```bash
   python clinic_agent/main.py -f example/CHAD_full_head.md -o report.md --lang cn
   ```
   - test 2
   Or process a PDF directly:
   ```bash
   clinic_agent --pdf example/CHAD_Full.pdf -o report.md --lang cn
   ```
   Without an argument the command enters an interactive session. Type `exit` to quit.
