from rich.console import Console
from rich.prompt import Prompt
import os

console = Console()



while True: 
    command = Prompt.ask("[bold green] Ingresa un comando [/bold green]")
    os.system(command)

