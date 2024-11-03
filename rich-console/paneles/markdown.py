from rich.markdown import Markdown
from rich.console import Console

mark = Markdown(
"""
# Encabezado
## lista de elementos
- Elemento 1
- Elemento 2
""")

con  = Console()
con.print(mark)
