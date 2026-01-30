import os
from ..core import skill

LICENSE_HEADER = """# Copyright (c) 2026 Langgraph Researcher. All rights reserved.
# Licensed under the MIT License.
"""

@skill
def add_license_header(file_path: str) -> str:
    """
    Adds a license header to a file if it doesn't already have one.
    Adiciona um cabeçalho de licença a um arquivo se ele ainda não tiver um.
    
    Args:
        file_path: The absolute path to the file to check and modify.
                   O caminho absoluto para o arquivo verificar e modificar.
        
    Returns:
        A status message indicating whether the header was added or already present.
        Uma mensagem de status indicando se o cabeçalho foi adicionado ou já estava presente.
    """
    if not os.path.exists(file_path):
        return f"Error: File not found at {file_path} / Erro: Arquivo não encontrado em {file_path}"
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if LICENSE_HEADER.strip() in content:
            return f"License header already present in {os.path.basename(file_path)}. / Cabeçalho de licença já presente."
            
        new_content = LICENSE_HEADER + "\n" + content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        return f"License header added to {os.path.basename(file_path)}. / Cabeçalho de licença adicionado."
        
    except Exception as e:
        return f"Error adding license header: {str(e)} / Erro ao adicionar cabeçalho: {str(e)}"
