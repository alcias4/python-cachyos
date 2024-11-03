from funciones.db import DataPeso
import matplotlib
import matplotlib.pyplot as plt
# pip install PyGObject   para cachy os 


def graficar():
    data = DataPeso()
    matplotlib.use("GTK3Agg")
    result = data.consult()

    x = []
    y = []


    for i in result:
        x.append(i[0])
        y.append(i[1])
    
    
    plt.plot(x, y, color="blue", marker="o" ,label="Peso") # Graficar puntos con una linea

    # personalizar graficos
    plt.xlabel("Dias")
    plt.ylabel("Peso")
    plt.title("Grafico de peso vs dias")
    plt.legend()

    # mostrar 

    plt.show()