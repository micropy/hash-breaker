from core.engine import *
from rich.console import Console
from rich.prompt import IntPrompt
from rich.panel import Panel
import os

console = Console()

def main():
    os.system("clear || cls")
    console.print(Panel("[bold cyan]1.[/] Dehash single hash\n[bold cyan]2.[/] Dehash from TXT", title="Options"))
    try:
        option = IntPrompt.ask("Select an option")
        engine(option)
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")

main()