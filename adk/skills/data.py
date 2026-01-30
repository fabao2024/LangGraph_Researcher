from ..core import skill
from typing import List, Dict, Any

@skill
def validate_schema(schema_definition: Dict[str, Any], rules: List[str] = None) -> str:
    """
    Validates a database schema definition against a set of governance rules.
    Valida uma definição de esquema de banco de dados contra um conjunto de regras de governança.
    
    Args:
        schema_definition: A dictionary representing the table schema (e.g., {'table': 'users', 'columns': [...]}).
                           Um dicionário representando o esquema da tabela.
        rules: A list of rules to check (e.g., ['require_primary_key', 'no_reserved_words']).
               Uma lista de regras para verificar.
               Defaults to basic checks if not provided.
        
    Returns:
        A validation report string.
        Um relatório de validação em string.
    """
    if rules is None:
        rules = ['require_primary_key']
        
    violations = []
    
    table_name = schema_definition.get('table', 'Unknown')
    columns = schema_definition.get('columns', [])
    
    # Basic Rule: Check for Primary Key
    if 'require_primary_key' in rules:
        has_pk = any(col.get('primary_key', False) for col in columns)
        if not has_pk:
            violations.append(f"Table '{table_name}' is missing a Primary Key. / Tabela '{table_name}' está sem Chave Primária.")

    # Basic Rule: Check for snake_case column names ( governance best practice)
    for col in columns:
        col_name = col.get('name', '')
        if not col_name.islower() or ' ' in col_name:
             violations.append(f"Column '{col_name}' in table '{table_name}' should be snake_case. / Coluna '{col_name}' deve estar em snake_case.")

    if not violations:
        return f"Schema validation passed for table '{table_name}'. / Validação de esquema aprovada."
    else:
        return f"Schema validation failed for table '{table_name}':\n- " + "\n- ".join(violations)
