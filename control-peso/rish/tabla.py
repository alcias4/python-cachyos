from rich.console import Console
from rich.table import Table
from funciones.db import DataPeso





def mostrar_tabla():
    data = DataPeso()
    tabla = Table(title="Control de peso")
    console = Console()

    # Agregar columnas
    tabla.add_column("Día",justify="center", style="cyan")
    tabla.add_column("Peso", justify="center", style="magenta")
    tabla.add_column("Ejercicio", justify="center", style="green")

    # Agregar filas

    for i in data.consult():
        valor = "Si" if i[2] == 1 else "No"
        tabla.add_row(str(i[0]),str(i[1]),valor)
        
    console.print(tabla)



