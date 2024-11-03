from rish.tabla import mostrar_tabla
from rich.table import Table
from rich.console import Console
from funciones.db import DataPeso
from graficar.grafica2 import graficar as gf2
from graficar.grafica import graficar as gf1
import os

tabla = Table(title="Menu de Opciones")
console = Console()
data = DataPeso()
# Menu
tabla.add_column("Numero",justify="center" ,style="cyan")
tabla.add_column("Funciones", justify="left", style="magenta")

tabla.add_row("1", "Consultar datos.")
tabla.add_row("2", "Agregar datos.")
tabla.add_row("3", "Eliminar dato.")
tabla.add_row("4", "Actualizar datos.")
tabla.add_row("5", "Eliminar todos los datos.")
tabla.add_row("6", "Graficar datos por consola.")
tabla.add_row("7", "Graficar datos por gtk gui.")
tabla.add_row("8", "Salir.")

def menu():
    opciones = ""
    while opciones != "8":
        
        os.system("clear")
        console.print(tabla)


        opciones = input("Ingresa una opcion: ")

        if opciones == "1":

            os.system("clear")
            mostrar_tabla()
   
        elif opciones == "2":

            os.system("clear")
            mostrar_tabla()
            data.insert_data()
            print("Se ha Creado correctamente!")
        elif opciones == "3":

            os.system("clear")
            mostrar_tabla()
            id = input("Ingrese el id del o el dia: ")
            data.delete_date(id)
            print("Se ha Aliminado el dato!")
            
        elif opciones == "4":
            os.system("clear")
            mostrar_tabla()
            data.update()
            print("Se ha Actualizado!")
            
        elif opciones == "5":
            os.system("clear")
            data.delete_all()
            print("Se ha eleminado todo!")
        
        elif opciones == "6":
            os.system("clear")
            gf1()

        elif opciones == "7":
            os.system("clear")
            gf2()        

        if opciones != "8": input("Volver: ")