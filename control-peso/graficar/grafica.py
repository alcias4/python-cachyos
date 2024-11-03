from funciones.db import DataPeso

import termplotlib as tlp
# para usar termplotlib debe instalar gnuplot

def graficar():
    data = DataPeso()

    result = data.consult()

    x = []
    y = []


    for i in result:
        x.append(i[0])
        y.append(i[1])
    
    
    fig = tlp.figure()
    fig.plot(x,y, label="peso", width=50, height=15)
    fig.show()