from tkinter import filedialog
from tkinter import *

base = Tk() #Base del programa, gui

#Variables globales que almacenan el path de las carpetas.

pathCarpetaF = StringVar()
pathCarpetaD = StringVar()


#Funciones 
def seleccionarCarpetaD():
    global pathCarpetaD
    pathCarpetaD.set(filedialog.askdirectory(initialdir="/",  title='Seleccionar directorio'))

def seleccionarCarpetaF():
    global pathCarpetaF
    pathCarpetaF.set(filedialog.askdirectory(initialdir="/",  title='Seleccionar directorio'))   

#Etiquetas
eCarpetaFuente = Label(base, text="Carpeta Fuente")
eDestino = Label(base, text="Destino")

#botones
boton1 = Button(base, text = "Seleccionar Carpeta", command = seleccionarCarpetaF) #seleccionar carpeta fuente
boton2 = Button(base, text = "Seleccionar Carpeta", command = seleccionarCarpetaD) #seleccionar carpeta destino
botonSig =  Button(base, text = "Siguiente", command = seleccionarCarpetaD) #Botón siguiente

#entradas
entradaCD = Entry(base, textvariable = pathCarpetaD)
entradaCF = Entry(base, textvariable = pathCarpetaF)



#posiciones GUI pantalla selección carpetas

eCarpetaFuente.grid(row = 1, column = 1)
eDestino.grid(row = 10, column = 1)
boton1.grid(row = 1, column = 20)
boton2.grid(row = 10, column = 20)
botonSig.grid(row = 30, column = 30)

entradaCF.grid(row = 1, column = 10)
entradaCD.grid(row = 10, column = 10)


base.mainloop()