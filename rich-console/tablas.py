from rich.console import Console
from rich.table import Table


table = Table(title="Ejemplo de tablas")

hola = 2
table.add_column("ID", justify="center", style="cyan", no_wrap=True)
table.add_column("Nombre",style="magenta")
table.add_column("Edad", justify="center", style="green")


table.add_row("1", "Camilo andrade","24")
table.add_row("2", "jose maritnez","54")
table.add_row("3", "Maria Gomez","45")

# Imprimir datos

console = Console()

console.print(table)


