"""
ADK Core Module

This module provides the @skill decorator for converting Python functions
into LangChain-compatible tools.

Example:
    @skill
    def my_tool(input: str) -> str:
        return f"Processed: {input}"
"""

from typing import Callable, Optional, Union
from langchain_core.tools import tool as langchain_tool


def skill(
    name_or_func: Optional[Union[Callable, str]] = None,
    description: Optional[str] = None
) -> Callable:
    """
    Decorator to mark a function as an ADK Skill.
    Supports both @skill and @skill(name="foo") usage.
    """
    if callable(name_or_func):
        # Called as @skill
        func = name_or_func
        t = langchain_tool(func)
        return t

    # Called as @skill(...)
    name = name_or_func
    def decorator(func: Callable) -> Callable:
        t = langchain_tool(name or func.__name__, description=description)(func)
        return t
    return decorator
