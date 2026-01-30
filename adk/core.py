from langchain_core.tools import tool as langchain_tool
from functools import wraps

def skill(name_or_func=None, description=None):
    """
    Decorator to mark a function as an ADK Skill.
    Supports both @skill and @skill(name="foo") usage.
    """
    if callable(name_or_func):
        # Called as @skill
        func = name_or_func
        t = langchain_tool(func)
        # t.is_adk_skill = True
        return t

    # Called as @skill(...)
    name = name_or_func
    def decorator(func):
        t = langchain_tool(name or func.__name__, description=description)(func)
        # t.is_adk_skill = True
        return t
    return decorator
