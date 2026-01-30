# LangGraph Researcher 2026

[Read in English](README.md)

Repositório para o agente LangGraph Researcher, equipado com ferramentas ADK.

## Habilidades ADK Incluídas

### 1. Formatador de Commit Git (`git.py`)
Garante que o histórico de versões seja consistente e legível ao impor **Conventional Commits**.
- **Uso**: Invoque com parâmetros `type` (feat, fix, etc.), `scope`, `subject`, e opcionalmente `body`.
- **Saída**: Retorna uma string formatada como `feat(auth): adicionar endpoint de login`.

### 2. Adicionador de Cabeçalho de Licença (`compliance.py`)
Automatiza a conformidade legal verificando e adicionando cabeçalhos de licença aos arquivos fonte.
- **Uso**: Forneça um `file_path`.
- **Comportamento**: Verifica se o arquivo existe e se já possui o cabeçalho de copyright padrão. Se faltar, adiciona o cabeçalho de licença MIT do LangGraph Researcher 2026 no início.

### 3. JSON para Pydantic (`codegen.py`)
Acelera o desenvolvimento gerando modelos Pydantic tipados a partir de JSON bruto.
- **Uso**: Forneça `json_input` (string ou dict) e um `model_name`.
- **Tecnologia**: Usa `datamodel-code-generator` internamente.
- **Saída**: Retorna código Python válido definindo os modelos Pydantic que correspondem à estrutura de entrada.

### 4. Validador de Schema de Banco de Dados (`data.py`)
Fortalece a governança de dados validando definições de esquema contra melhores práticas.
- **Uso**: Forneça um dicionário `schema_definition` (com nome da tabela e colunas).
- **Verificações**:
    - **Chave Primária**: Garante que a tabela tenha uma chave primária definida.
    - **Convenção de Nomenclatura**: Valida se os nomes das colunas estão em `snake_case`.
- **Saída**: Um relatório de aprovação/falha listando quaisquer violações encontradas.

## Como Executar

1. Abra o terminal em `Langgraph_researcher_2026`.
2. Ative o venv: `.\.venv\Scripts\activate` (Windows) ou `source .venv/bin/activate` (Linux/Mac)
3. Execute: `langgraph dev --allow-blocking`

## Requisitos

- Python 3.10 ou superior
- Chave de API do Google Generative AI
- Chave de API do Tavily

## Recomendações

Crie e ative um ambiente virtual antes de instalar as dependências:

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

## Atenção / Solução de Problemas

Alguns usuários relataram problemas ao usar no Windows.
O problema geralmente é resolvido através do comando:
```bash
langgraph dev --allow-blocking
```

Lembre-se que ao executar, o agente (LangGraph Studio) será exibido em seu navegador padrão.
