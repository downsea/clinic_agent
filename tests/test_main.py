import os
import shutil
from pathlib import Path
from unittest.mock import MagicMock
import types
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Stub out heavy dependencies before importing the package
fake_community = types.ModuleType("langchain_community")
fake_tools = types.ModuleType("langchain_community.tools")
fake_tavily = types.ModuleType("langchain_community.tools.tavily_search")
fake_tavily.TavilySearchResults = MagicMock()
fake_tools.tavily_search = fake_tavily
fake_community.tools = fake_tools
sys.modules["langchain_community"] = fake_community
sys.modules["langchain_community.tools"] = fake_tools
sys.modules["langchain_community.tools.tavily_search"] = fake_tavily

fake_dotenv = types.ModuleType("dotenv")
fake_dotenv.load_dotenv = MagicMock()
sys.modules["dotenv"] = fake_dotenv

fake_langchain = types.ModuleType("langchain")
fake_agents = types.ModuleType("langchain.agents")
fake_chat_models = types.ModuleType("langchain.chat_models")
fake_agents.AgentExecutor = MagicMock()
fake_agents.create_react_agent = MagicMock()
fake_chat_models.ChatOpenAI = MagicMock()
fake_langchain.agents = fake_agents
fake_langchain.chat_models = fake_chat_models
sys.modules["langchain"] = fake_langchain
sys.modules["langchain.agents"] = fake_agents
sys.modules["langchain.chat_models"] = fake_chat_models

fake_langchain_core = types.ModuleType("langchain_core")
fake_prompts = types.ModuleType("langchain_core.prompts")

class DummyPrompt:
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_template(cls, template):
        return cls()

fake_prompts.PromptTemplate = DummyPrompt
fake_langchain_core.prompts = fake_prompts
sys.modules["langchain_core"] = fake_langchain_core
sys.modules["langchain_core.prompts"] = fake_prompts

fake_pypdf = types.ModuleType("pypdf")
class DummyReader:
    class _Page:
        def extract_text(self):
            return "example"

    def __init__(self, path):
        self.pages = [self._Page()]
fake_pypdf.PdfReader = DummyReader
sys.modules["pypdf"] = fake_pypdf

import pytest
from click.testing import CliRunner

from clinic_agent.main import create_agent, pdf_to_markdown, cli


def test_pdf_to_markdown(tmp_path):
    src = Path('example/US11826325.pdf')
    pdf = tmp_path / 'sample.pdf'
    shutil.copy(src, pdf)
    text = pdf_to_markdown(str(pdf))
    assert (tmp_path / 'sample.md').exists()
    assert isinstance(text, str) and text


def test_create_agent(monkeypatch):
    called = {}

    def fake_chat_openai(**kwargs):
        called['llm_kwargs'] = kwargs
        return 'llm'

    def fake_search_results(**kwargs):
        called['search'] = kwargs
        tool = MagicMock()
        tool.name = 'search'
        return tool

    def fake_create(agent, tools, prompt):
        called['agent'] = True
        return 'agent'

    monkeypatch.setenv('OPENAI_MODEL', 'gpt-4')
    monkeypatch.setenv('OPENAI_API_BASE', 'https://api.test')
    monkeypatch.setenv('HTTPS_PROXY', 'http://proxy')
    monkeypatch.setenv('DISABLE_SSL_VERIFY', '1')

    monkeypatch.setattr('clinic_agent.main.ChatOpenAI', fake_chat_openai)
    monkeypatch.setattr('clinic_agent.main.TavilySearchResults', fake_search_results)
    monkeypatch.setattr('clinic_agent.main.create_react_agent', lambda llm, tools, prompt: 'agent_body')
    monkeypatch.setattr('clinic_agent.main.AgentExecutor', MagicMock(return_value='executor'))

    agent = create_agent()
    assert agent == 'executor'
    assert called['llm_kwargs']['model'] == 'gpt-4'
    assert called['llm_kwargs']['base_url'] == 'https://api.test'
    assert called['llm_kwargs']['proxy'] == 'http://proxy'


def test_cli_query(monkeypatch):
    runner = CliRunner()
    agent = MagicMock()
    agent.run.return_value = 'answer'
    monkeypatch.setattr('clinic_agent.main.create_agent', lambda: agent)
    result = runner.invoke(cli, ['hello'])
    assert result.exit_code == 0
    assert 'answer' in result.output


def test_cli_pdf(monkeypatch, tmp_path):
    src = Path('example/US11826325.pdf')
    pdf = tmp_path / 'input.pdf'
    shutil.copy(src, pdf)
    agent = MagicMock()
    agent.run.return_value = 'pdf result'
    monkeypatch.setattr('clinic_agent.main.create_agent', lambda: agent)
    result = CliRunner().invoke(cli, ['--pdf', str(pdf)])
    assert result.exit_code == 0
    assert 'pdf result' in result.output
