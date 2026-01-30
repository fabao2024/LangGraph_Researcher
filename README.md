# LangGraph Researcher 2026

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
2. Activate venv: `.\.venv\Scripts\activate`
3. Run: `langgraph dev --allow-blocking`


## Requisitos

- Python 3.10 ou superior
- Google Generative AI API Key
- Tavily API Key

## Recomendações

Crie e ative um ambiente virtual antes de instalar as dependências:

No vídeo
```bash
python3.12 -m venv .venv
source .venv/bin/activate # Linux/macOS
# .\.venv\Scripts\activate # Windows
```

## Instalação

Entre no ambiente virtual e execute: 

```bash
source .venv/bin/activate # Linux/macOS
# .\.venv\Scripts\activate # Windows
```

```bash
pip install -r requirements.txt
```

## Configuração

Na raiz do projeto, crie o arquivo `.env` com as chaves:

```dotenv
GOOGLE_API_KEY=sua_chave_api
TAVILY_API_KEY=sua_chave_tavily
```

## Uso

No terminal, execute:

```bash
langgraph dev
```

O script:

- Usa `dotenv` para carregar variáveis de ambiente
- Inicializa o modelo `gemini-2.5-flash`
- Define a ferramenta `search_web` com Tavily
- Cria um agente ReAct via `create_react_agent`

## Atenção

Alguns usuários relataram problemas com uso de windows.
O problema foi resolvido através do comando.
```bash
langgraph dev --allow-blocking
```

Lembresse que ao executar o agente será exibido em seu navegador padrão.
