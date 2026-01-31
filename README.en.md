# LangGraph Researcher 2026

[Leia em Português](README.md)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-vv0.2-1C2C33?style=for-the-badge&color=28a745)
![LangChain](https://img.shields.io/badge/LangChain-v0.3-blueviolet?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-8E75B2?style=for-the-badge&logo=google&logoColor=white&color=ff6d00)
![Tavily](https://img.shields.io/badge/Tavily-Search%20API-FF0000?style=for-the-badge)

Repo for the LangGraph Researcher agent, equipped with ADK tools.

## ADK Skills Included

This agent is equipped with an "Agent Development Kit" (ADK) that gives it specialized skills. These skills are Python tools that the agent can call to perform complex tasks.

### 1. Git Commit Formatter (`git.py`)
Ensures version history is consistent and readable by enforcing **Conventional Commits**.
- **What it does**: Formats commit messages following the `type(scope): description` standard.
- **Example agent usage**: When you ask "create a commit message for the new login function", the agent calls this skill to generate the correct formatted string.

### 2. License Header Adder (`compliance.py`)
Automates legal compliance by checking and adding license headers to source files.
- **What it does**: Inserts the MIT license header at the top of files if it doesn't already exist.
- **Example agent usage**: If you ask "check the file licenses", the agent scans the files and uses this skill to apply the header where missing.

### 3. JSON to Pydantic (`codegen.py`)
Accelerates development by generating typed Pydantic models from raw JSON verification.
- **What it does**: Converts a JSON object into Python Pydantic classes.
- **Example agent usage**: Upon receiving a JSON from an API and asking "create the data model for this", the agent uses this skill to generate the corresponding Python code.

### 4. Database Schema Validator (`data.py`)
Strengthens data governance by validating schema definitions against best practices.
- **What it does**: Checks if tables have primary keys and if columns follow the `snake_case` convention.
- **Example agent usage**: When designing a database, the agent can use this skill to ensure the proposed schema follows best practices before generating SQL.

## How Skills Work in LangGraph

When you run the command `langgraph dev` (or `langgraph dev --allow-blocking`), the agent loads in **LangGraph Studio**, a visual interface in your browser.

1.  **Chat Interface**: In LangGraph Studio, you interact with the agent via chat.
2.  **Intent Detection**: When you make a request (e.g., "format this commit"), the AI model (Gemini) analyzes if it needs to use any tool to fulfill the request.
3.  **Skill Execution**: If necessary, the agent "calls" the corresponding Python function (the skill) behind the scenes.
4.  **Response**: The skill result (e.g., the formatted message or generated code) is returned to the agent, which then formulates the final response for you in the chat.

**Flow Summary:**
`User (Chat) -> Agent (Decision) -> Skill (Python Execution) -> Agent (Response)`

## How to Customize the Agent

In addition to the ADK skills, you can customize the agent's core behavior by editing `langgraph-101.py`.

### 1. Changing the System Prompt
The agent's personality and rules are defined in the **System Prompt** (variable `system_message` in code).
- **Location**: `langgraph-101.py` (lines 25-37 approximately).
- **How to modify**: Edit the text inside `SystemMessage(content="...")`. You can add new rules, change the tone, or instruct the agent to act as a specific persona.

### 2. Configuring Web Search (`search_web`)
The agent uses the `search_web` tool to find information online via **Tavily**.
- **Location**: `langgraph-101.py` (function `search_web`).
- **How to modify**:
    - The tool is defined as a Python function decorated with `@tool`.
    - Inside, it initializes `TavilySearch`. You can adjust parameters like `max_results` (to get more or fewer links) or `search_depth` (basic or advanced).
    - The docstring (`"""Busca informações..."""`) helps the LLM decide **when** to call this tool. modifying this description can change how often or in what contexts the agent searches the web.

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
- Defines the `search_web` tool and **ADK Skills**
- Creates a ReAct agent via `create_react_agent`

## Attention / Troubleshooting

Some users reported issues when using Windows.
The issue is usually resolved by running the command:
```bash
langgraph dev --allow-blocking
```

Remember that upon execution, the agent (LangGraph Studio) will be displayed in your default browser.
