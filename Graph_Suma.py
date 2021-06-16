#Prueba Tausand - Ejercicio 1
#Grafica sumas acumuladas
#Programa grafica en vivo suma axumulada de valores ingrasados por teclado.
#Juan Camilo Bedoya

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation

#Inizializacion de la grafica

x = list(np.arange(-30,0.1,0.5))
y = list(np.zeros(len(x)))

fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
plt.ylim([0,10])
plt.xlabel("tiempo(s)")
plt.ylabel("suma acumulada")
l, = plt.plot(x,y)

acum = 0

#Actualizar grafica

def update(i):
    
    #Actualiza la grafica
    #Parametros:
    # i: parametro necesario para que FuncAnimation actualice la grafica en vivo

    y.pop(0)
    y.append(acum)
    l.set_ydata(y)
    plt.draw()


#Botones

def reset_counter(event):
    
    #Reinicia el acumulado
    global acum
    acum = 0

def close_graph(event):
    #Cierra la figura con la grafica
    plt.close(fig)

ax_reset = plt.axes([0.55, 0.05, 0.25, 0.075])
ax_close = plt.axes([0.81, 0.05, 0.1, 0.075])

btn_reset = Button(ax_reset,'Reinicar Contador')
btn_close = Button(ax_close,'Cerrar')

btn_reset.on_clicked(reset_counter)
btn_close.on_clicked(close_graph)

#Manejo de eventos de teclado eventos de teclado

def teclado(event):

    #Cambia el valor del acumulado segun evento de teclado
    #Parametros:
    # event: Evento que se va a manejar. Son acceptadas las teclas del '1' al '5'
    global acum
    if event.key == '1':
        acum = acum+1
    elif event.key == '2':
        acum = acum+2
    elif event.key == '3':
        acum = acum+3
    elif event.key == '4':
        acum = acum+4
    elif event.key == '5':
        acum = acum+5
    

fig.canvas.mpl_connect('key_press_event', teclado)

#Actualizacion en vivo

ani = FuncAnimation(plt.gcf(), update,interval =500)

#Mostrar grafica

plt.show()