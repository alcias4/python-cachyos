from rich.panel import Panel
from rich.console import Console

con = Console()
panel = Panel("Esto es un panel con contenido")

con.print(panel)

