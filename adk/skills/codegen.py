from ..core import skill
from datamodel_code_generator import InputFileType, generate
import json
from pathlib import Path

@skill
def generate_pydantic_model(json_input: str, model_name: str = "GeneratedModel") -> str:
    """
    Generates a Pydantic model from a JSON string or dictionary.
    Gera um modelo Pydantic a partir de uma string JSON ou dicionário.
    
    Args:
        json_input: A valid JSON string representing the data structure.
                    Uma string JSON válida representando a estrutura de dados.
        model_name: The name of the root model class to generate.
                    O nome da classe modelo raiz a ser gerada.
        
    Returns:
        A string containing the generated Python code with Pydantic models.
        Uma string contendo o código Python gerado com modelos Pydantic.
    """
    try:
        # Validate JSON first
        if isinstance(json_input, str):
            json_data = json.loads(json_input)
            input_text = json_input
        else:
            json_data = json_input
            input_text = json.dumps(json_input)

        output = generate(
            input_text,
            input_file_type=InputFileType.Json,
            input_filename="example.json",
            class_name=model_name,
        )
        return output
    except json.JSONDecodeError:
        return "Error: Invalid JSON input. / Erro: Entrada JSON inválida."
    except Exception as e:
        return f"Error generating model: {str(e)} / Erro ao gerar modelo: {str(e)}"
