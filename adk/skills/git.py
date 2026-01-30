from ..core import skill

@skill
def format_commit_message(type: str, scope: str, subject: str, body: str = "") -> str:
    """
    Formats a commit message according to Conventional Commits standards.
    Formata uma mensagem de commit de acordo com os padrões Conventional Commits.
    
    Args:
        type: The type of change (e.g., feat, fix, docs, style, refactor, perf, test, chore).
              O tipo de mudança (ex: feat, fix, docs, style, refactor, perf, test, chore).
        scope: The scope of the change (e.g., login, search, database).
               O escopo da mudança (ex: login, busca, banco_de_dados).
        subject: A short, imperative tense description of the change.
                 Uma descrição curta e imperativa da mudança.
        body: (Optional) A longer description of the change.
              (Opcional) Uma descrição mais longa da mudança.
        
    Returns:
        A formatted commit message string.
        Uma string de mensagem de commit formatada.
    """
    message = f"{type}({scope}): {subject}"
    if body:
        message += f"\n\n{body}"
    return message
