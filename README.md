# LangGraph Researcher 2026

[Read in English](README.en.md)

Repositório para o agente LangGraph Researcher, equipado com ferramentas ADK.

## Habilidades ADK Incluídas

Este agente está equipado com um "Agent Development Kit" (ADK) que lhe confere habilidades especializadas. Estas habilidades são ferramentas Python que o agente pode chamar para realizar tarefas complexas.

### 1. Formatador de Commit Git (`git.py`)
Garante que o histórico de versões seja consistente e legível ao impor **Conventional Commits**.
- **O que faz**: Formata mensagens de commit seguindo o padrão `tipo(escopo): descrição`.
- **Exemplo de uso pelo agente**: Quando você pede "crie uma mensagem de commit para a nova função de login", o agente chama esta skill para gerar a string formatada correta.

### 2. Adicionador de Cabeçalho de Licença (`compliance.py`)
Automatiza a conformidade legal verificando e adicionando cabeçalhos de licença aos arquivos fonte.
- **O que faz**: Insere o cabeçalho de licença MIT no topo dos arquivos se ele ainda não existir.
- **Exemplo de uso pelo agente**: Se você pedir "verifique as licenças dos arquivos", o agente varre os arquivos e usa esta skill para aplicar o cabeçalho onde estiver faltando.

### 3. JSON para Pydantic (`codegen.py`)
Acelera o desenvolvimento gerando modelos Pydantic tipados a partir de JSON bruto.
- **O que faz**: Converte um objeto JSON em classes Python Pydantic.
- **Exemplo de uso pelo agente**: Ao receber um JSON de uma API e pedir "crie o modelo de dados para isso", o agente usa esta skill para gerar o código Python correspondente.

### 4. Validador de Schema de Banco de Dados (`data.py`)
Fortalece a governança de dados validando definições de esquema contra melhores práticas.
- **O que faz**: Verifica se tabelas têm chaves primárias e se colunas seguem a convenção `snake_case`.
- **Exemplo de uso pelo agente**: Ao projetar um banco de dados, o agente pode usar esta skill para garantir que o esquema proposto segue as boas práticas antes de gerar o SQL.

## Como as Skills Funcionam no LangGraph

Quando você executa o comando `langgraph dev` (ou `langgraph dev --allow-blocking`), o agente é carregado no **LangGraph Studio**, uma interface visual no seu navegador.

1.  **Interface de Chat**: No LangGraph Studio, você interage com o agente através de um chat.
2.  **Detecção de Intenção**: Quando você faz um pedido (ex: "formate este commit"), o modelo de IA (Gemini) analisa se precisa usar alguma ferramenta para atender ao pedido.
3.  **Execução da Skill**: Se necessário, o agente "chama" a função Python correspondente (a skill) nos bastidores.
4.  **Resposta**: O resultado da skill (ex: a mensagem formatada ou o código gerado) é devolvido ao agente, que então formula a resposta final para você no chat.

**Resumo do Fluxo:**
`Usuário (Chat) -> Agente (Decisão) -> Skill (Execução Python) -> Agente (Resposta)`

## Como Modificar o Agente

Além das skills do ADK, você pode personalizar o comportamento central do agente editando o arquivo `langgraph-101.py`.

### 1. Alterando o Prompt do Sistema (System Prompt)
A personalidade e as regras do agente são definidas no **System Message** (variável `system_message` no código).
- **Localização**: `langgraph-101.py` (linhas 25-37 aproximadamente).
- **Como modificar**: Edite o texto dentro de `SystemMessage(content="...")`. Você pode adicionar novas regras, mudar o tom de voz ou instruir o agente a agir como uma persona específica.

### 2. Configurando a Busca Web (`search_web`)
O agente usa a ferramenta `search_web` para buscar informações online via **Tavily**.
- **Localização**: `langgraph-101.py` (função `search_web`).
- **Como modificar**:
    - A ferramenta é definida como uma função Python decorada com `@tool`.
    - Dentro dela, inicializa-se o `TavilySearch`. Você pode ajustar parâmetros como `max_results` (para ter mais ou menos links) ou `search_depth` (busca básica ou avançada).
    - A docstring (`"""Busca informações..."""`) ajuda o LLM a decidir **quando** chamar esta ferramenta. Alterar esta descrição pode mudar a frequência ou contexto em que o agente busca na web.

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
- Define a ferramenta `search_web` e as **Skills ADK**
- Cria um agente ReAct via `create_react_agent`

## Atenção / Solução de Problemas

Alguns usuários relataram problemas ao usar no Windows.
O problema geralmente é resolvido através do comando:
```bash
langgraph dev --allow-blocking
```

Lembre-se que ao executar, o agente (LangGraph Studio) será exibido em seu navegador padrão.
