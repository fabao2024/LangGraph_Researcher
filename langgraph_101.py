from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from adk.skills import (
    format_commit_message, 
    add_license_header, 
    generate_pydantic_model, 
    validate_schema
)

from dotenv import load_dotenv

# Configuração do ambiente (chave API)
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2  # Reduzido para respostas mais precisas e focadas
)

# Define o prompt do sistema com instruções detalhadas
system_message = SystemMessage(content="""Você é um assistente especializado em pesquisa e análise de informações.

INSTRUÇÕES IMPORTANTES:
1. Sempre use a ferramenta search_web quando precisar de informações atualizadas ou específicas
2. Formule queries de busca claras e objetivas em português ou inglês
3. Analise criticamente os resultados antes de responder
4. Cite as fontes quando apresentar informações
5. Se os resultados não forem suficientes, faça buscas adicionais com termos diferentes
6. Priorize fontes confiáveis e informações verificáveis
7. Seja preciso e objetivo nas respostas

Seu objetivo é fornecer respostas precisas, bem fundamentadas e úteis.
Você agora possui ferramentas de desenvolvimento (ADK) para formatar commits, adicionar headers de licença, gerar modelos Pydantic e validar schemas de DB. Use-as quando apropriado.""")


@tool
def search_web(query: str = "") -> str:
    """Busca informações atualizadas e confiáveis na web usando busca avançada.
    
    Use esta ferramenta quando precisar de:
    - Informações atuais ou notícias recentes
    - Dados específicos sobre pessoas, empresas, produtos ou eventos
    - Fatos verificáveis e estatísticas
    - Explicações técnicas ou conceituais
    
    Args:
        query: Termos de busca claros e específicos (pode ser em português ou inglês)
        
    Returns:
        Resultados relevantes da busca web com conteúdo e URLs das fontes.
    """
    tavily_search = TavilySearch(
        max_results=5,  # Mais resultados para melhor cobertura
        search_depth="advanced"  # Busca mais profunda e precisa
    )
    search_docs = tavily_search.invoke(query)
    return search_docs


# Lista de ferramentas
tools = [
    search_web,
    format_commit_message,
    add_license_header,
    generate_pydantic_model,
    validate_schema
]

# Criação do agente ReAct com memória
graph = create_react_agent(
    model, 
    tools=tools,
    prompt=system_message
)

