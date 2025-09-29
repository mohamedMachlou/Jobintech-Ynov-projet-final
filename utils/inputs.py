from typing import Any, Optional
from prompt_toolkit.lexers import Lexer
from questionary import Style, select as questionary_select, text, checkbox as questionary_checkbox
from questionary.constants import DEFAULT_QUESTION_PREFIX


def input(
    message: str,
    default: str = "",
    validate: Any = None,
    qmark: str = DEFAULT_QUESTION_PREFIX,
    style: Optional[Style] = None,
    multiline: bool = False,
    instruction: Optional[str] = None,
    lexer: Optional[Lexer] = None,
    **kwargs: Any,
):
    return text(
        message,
        default,
        validate,
        qmark,
        style,
        multiline,
        instruction,
        lexer,
        **kwargs,
    ).ask()


def radio(prompt: str, choices: list) -> str:
    return questionary_select(prompt, choices=choices).ask()


def checkbox(prompt: str, choices: list) -> list:
    return questionary_checkbox(prompt, choices=choices).ask()


def select(prompt: str, choices: list) -> str:
    selected = questionary_select(prompt, choices=choices).ask()
    return selected

