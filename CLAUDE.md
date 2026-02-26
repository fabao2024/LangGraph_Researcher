# CLAUDE.md — LangGraph Researcher

This file provides guidance for AI assistants working in this repository.

## Project Overview

**LangGraph Researcher** is a ReAct (Reasoning + Acting) agent built with LangGraph and Google Gemini. It combines web search with four specialized developer tools — called **ADK Skills** — that help with software tasks like formatting commits, adding license headers, generating Pydantic models, and validating database schemas.

The agent is exposed via LangGraph's API server and communicates entirely through the LangGraph chat interface.

---

## Repository Structure

```
LangGraph_Researcher/
├── langgraph_101.py          # Agent entry point: LLM, tools, graph assembly
├── langgraph.json            # LangGraph configuration (graph name, version)
├── requirements.txt          # Python dependencies
├── verify_adk.py             # Test suite for all ADK skills
├── .env.example              # Required environment variables template
├── adk/
│   ├── __init__.py
│   ├── core.py               # @skill decorator (wraps functions as LangChain tools)
│   └── skills/
│       ├── __init__.py       # Re-exports all four skills
│       ├── git.py            # format_commit_message
│       ├── compliance.py     # add_license_header
│       ├── codegen.py        # generate_pydantic_model
│       └── data.py           # validate_schema
├── README.md                 # Documentation (Portuguese)
├── README.en.md              # Documentation (English)
└── CHANGELOG.md              # Version history (Keep a Changelog format)
```

---

## Architecture

### Agent (langgraph_101.py)

The agent is built with `create_react_agent` from `langgraph.prebuilt`. It:

- Uses **`gemini-2.0-flash`** via `ChatGoogleGenerativeAI` with `temperature=0.2`
- Has a Portuguese-language system prompt instructing it to search before answering, cite sources, and use ADK tools when appropriate
- Exposes **five tools** to the LLM:
  1. `search_web` — Tavily search (max 5 results, advanced depth)
  2. `format_commit_message` — Conventional Commits formatter
  3. `add_license_header` — MIT license header injector
  4. `generate_pydantic_model` — JSON → Pydantic converter
  5. `validate_schema` — DB schema governance checker

The `graph` object exported from `langgraph_101.py` is what LangGraph serves.

### ADK Skill System (adk/)

The `@skill` decorator in `adk/core.py` wraps any Python function as a LangChain tool using `langchain_core.tools.tool`. Skills support two call styles:

```python
@skill                          # bare decorator
@skill(name="my_name")          # with optional name/description
```

Skills are invoked by the LLM agent using `.invoke({...})` with a dict of named arguments.

---

## ADK Skills Reference

### `format_commit_message` (adk/skills/git.py)
Formats messages following [Conventional Commits](https://www.conventionalcommits.org/).

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | str | yes | `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore` |
| `scope` | str | yes | Area of change (e.g., `auth`, `search`, `database`) |
| `subject` | str | yes | Short imperative description |
| `body` | str | no | Longer explanation (blank by default) |

Output: `type(scope): subject\n\nbody`

### `add_license_header` (adk/skills/compliance.py)
Prepends a MIT license header to a file (idempotent — skips if already present).

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `file_path` | str | yes | Absolute path to the target file |

Header added:
```python
# Copyright (c) 2026 Fabio Pettian. All rights reserved.
# Licensed under the MIT License.
```

Returns an error string if the file does not exist.

### `generate_pydantic_model` (adk/skills/codegen.py)
Converts a JSON string into a Python Pydantic `BaseModel` class using `datamodel-code-generator`.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `json_input` | str | yes | Valid JSON string |
| `model_name` | str | no | Root class name (default: `"GeneratedModel"`) |

Returns generated Python source code as a string, or an error string on bad input.

### `validate_schema` (adk/skills/data.py)
Validates a database table schema against governance rules.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `schema_definition` | dict | yes | `{"table": "name", "columns": [{...}]}` |
| `rules` | list | no | Rules to apply; defaults to `["require_primary_key"]` |

Built-in checks:
- **`require_primary_key`** — at least one column must have `"primary_key": true`
- **snake_case enforcement** — all column names must match `^[a-z][a-z0-9_]*$` (always active)

Returns a human-readable validation report.

---

## Development Workflows

### Environment Setup

```bash
# 1. Copy environment template
cp .env.example .env
# Edit .env and fill in:
#   GOOGLE_API_KEY=...
#   TAVILY_API_KEY=...

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the Agent

```bash
# Standard (Linux/macOS)
langgraph dev

# Windows (required flag to avoid blocking I/O issues)
langgraph dev --allow-blocking

# Custom host/port
LANGGRAPH_PORT=8123 LANGGRAPH_HOST=0.0.0.0 langgraph dev
```

The LangGraph Studio UI will be available at the URL printed in the terminal.

### Running Tests

```bash
python verify_adk.py
```

Tests are plain Python with `assert` statements — no testing framework required. The script runs 8 test functions covering both happy paths and error cases for each skill. Expected output ends with `All tests passed!`.

---

## Key Conventions

### Python Style
- Follow **PEP 8** — underscores in file names (`langgraph_101.py`, not `langgraph-101.py`)
- All skill functions use **bilingual docstrings** (English first, then Portuguese)
- Return error messages in both English and Portuguese: `"Error: ... / Erro: ..."`

### Commit Messages
Follow **Conventional Commits**: `type(scope): subject`

Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

### Adding a New ADK Skill
1. Create `adk/skills/my_skill.py` with a function decorated with `@skill`
2. Re-export it from `adk/skills/__init__.py`
3. Import it in `langgraph_101.py` and add it to the `tools` list
4. Add test functions in `verify_adk.py` (positive and negative cases)

### License Headers
All Python source files should carry the MIT header (use `add_license_header` or add manually):
```python
# Copyright (c) 2026 Fabio Pettian. All rights reserved.
# Licensed under the MIT License.
```

### Schema Naming
Database column names must use `snake_case` (regex: `^[a-z][a-z0-9_]*$`). The `validate_schema` skill enforces this automatically.

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_API_KEY` | yes | Google Generative AI API key (for Gemini) |
| `TAVILY_API_KEY` | yes | Tavily Search API key |

Both are loaded at startup via `python-dotenv` (`load_dotenv()` in `langgraph_101.py`).

---

## Dependencies

| Package | Version Range | Purpose |
|---------|--------------|---------|
| `langchain-google-genai` | `>=2.0.0,<3.0.0` | Gemini LLM integration |
| `langchain-tavily` | `>=0.1.0,<1.0.0` | Web search tool |
| `langchain-community` | `>=0.3.0,<1.0.0` | LangChain community tools |
| `langgraph-cli[inmem]` | `>=0.2.0,<1.0.0` | Agent server + in-memory backend |
| `datamodel-code-generator` | `>=0.25.0,<1.0.0` | JSON → Pydantic model generation |
| `python-dotenv` | `>=1.0.0` | `.env` file loading |

---

## Files to Never Commit

The `.gitignore` excludes:
- `.env` — contains API keys
- `.langgraph_api/` and `*.pckl` — LangGraph runtime state files
- `__pycache__/`, `*.pyc` — Python bytecode
- `.venv/`, `venv/`, `env/` — virtual environments
- `.vscode/`, `.idea/` — IDE configuration

---

## LangGraph Configuration (langgraph.json)

```json
{
    "dependencies": ["."],
    "graphs": {
        "agent": "langgraph_101:graph"
    },
    "langgraph_version": "0.2.x"
}
```

The key `"agent"` maps to the `graph` object exported from `langgraph_101.py`. If you rename the graph variable or move the module, update this file accordingly.
