from ..core import skill

@skill
def format_commit_message(type: str, scope: str, subject: str, body: str = "") -> str:
    """
    Formats a commit message according to Conventional Commits standards.
    
    Args:
        type: The type of change (e.g., feat, fix, docs, style, refactor, perf, test, chore).
        scope: The scope of the change (e.g., login, search, database).
        subject: A short, imperative tense description of the change.
        body: (Optional) A longer description of the change.
        
    Returns:
        A formatted commit message string.
    """
    message = f"{type}({scope}): {subject}"
    if body:
        message += f"\n\n{body}"
    return message
