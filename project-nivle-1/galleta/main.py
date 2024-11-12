from rich.console import Console
from rich.prompt import Prompt
import random
import json
import os

file_path ="./ms.json"

with open(file_path, "r", encoding="utf-8" ) as file:
    data = json.load(file)



console = Console()
paro = True

while paro:
    os.system("clear")
    texto  = Prompt.ask("[bold green]Quieres abrir tu galleta (si/no): [/bold green]")      
    if texto == "si":
        repust  = random.choice(data)
        console.print(f"[bold]Mensaje:[bold] {repust}", style="magenta")
        input("enter")
    else:
        console.print("Chao !", style="bold red")
        paro=False



