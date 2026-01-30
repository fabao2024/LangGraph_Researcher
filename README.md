# LangGraph Researcher 2026

[Leia em Português](README.pt-br.md)

Repo for the LangGraph Researcher agent, equipped with ADK tools.

## ADK Skills Included

### 1. Git Commit Formatter (`git.py`)
Ensures version history is consistent and readable by enforcing **Conventional Commits**.
- **Usage**: Invoke with parameters `type` (feat, fix, etc.), `scope`, `subject`, and optional `body`.
- **Output**: Returns a formatted string like `feat(auth): add login endpoint`.

### 2. License Header Adder (`compliance.py`)
Automates legal compliance by checking and adding license headers to source files.
- **Usage**: Provide a `file_path`.
- **Behavior**: Checks if the file exists and if it already has the standard copyright header. If missing, prepends the 2026 LangGraph Researcher MIT license header.

### 3. JSON to Pydantic (`codegen.py`)
Accelerates development by generating typed Pydantic models from raw JSON verification.
- **Usage**: Provide `json_input` (string or dict) and a `model_name`.
- **Tech**: Uses `datamodel-code-generator` under the hood.
- **Output**: Returns valid Python code defining the Pydantic models matching the input structure.

### 4. Database Schema Validator (`data.py`)
Strengthens data governance by validating schema definitions against best practices.
- **Usage**: Provide a `schema_definition` dict (with table name and columns).
- **Checks**:
    - **Primary Key**: Ensures the table has a primary key defined.
    - **Naming Convention**: Validates that column names are in `snake_case`.
- **Output**: A pass/fail report listing any violations found.

## How to Run

1. Open terminal in `Langgraph_researcher_2026`.
2. Activate venv: `.\.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Linux/Mac)
3. Run: `langgraph dev --allow-blocking`

## Prerequisites

- Python 3.10 or higher
- Google Generative AI API Key
- Tavily API Key

## Recommendations

Create and activate a virtual environment before installing the dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate # Linux/macOS
# .\.venv\Scripts\activate # Windows
```

## Installation

Enter the virtual environment and run: 

```bash
source .venv/bin/activate # Linux/macOS
# .\.venv\Scripts\activate # Windows
```

```bash
pip install -r requirements.txt
```

## Configuration

In the project root, create a `.env` file with the keys:

```dotenv
GOOGLE_API_KEY=your_api_key
TAVILY_API_KEY=your_tavily_key
```

## Usage

In the terminal, execute:

```bash
langgraph dev
```

The script:

- Uses `dotenv` to load environment variables
- Initializes the `gemini-2.5-flash` model
- Defines the `search_web` tool with Tavily
- Creates a ReAct agent via `create_react_agent`

## Attention / Troubleshooting

Some users reported issues when using Windows.
The issue is usually resolved by running the command:
```bash
langgraph dev --allow-blocking
```

Remember that upon execution, the agent (LangGraph Studio) will be displayed in your default browser.
