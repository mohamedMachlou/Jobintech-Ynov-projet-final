from rich.console import Console

# from rich.spinner import Spinner
from contextlib import contextmanager

console = Console()


def info(msg: str):
    console.print(f"ℹ️ [bold cyan]{msg}[/bold cyan]")


def success(msg: str):
    console.print(f"✅ [bold green]{msg}[/bold green]")


def error(msg: str):
    console.print(f"❌ [bold red]{msg}[/bold red]")

def warn(msg: str):
    console.print(f"⚠️ [bold red]{msg}[/bold red]")


@contextmanager
def loading(msg: str = "Loading...", spinner_style: str = "dots"):
    with console.status(
        f"[bold cyan]{msg}[/bold cyan]", spinner=spinner_style
    ) as status:
        yield status
