import glob, os
from tkinter import filedialog
from tkinter import *

##Agradecimientos: 
# 
#  
#   https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

#Variables globales 
pathCarpetaD=""
pathCarpetaF=""


class Sync(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.cambiarVentana(VentanaInicio)
        

    def cambiarVentana(self, frame_class): #Elimina pantalla base y crea la siguiente
        new_frame = frame_class(self) 
        if self._frame is not None: 
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()



class VentanaInicio(Frame): #Clase de pantalla de inicio
    def __init__(self, master):
        Frame.__init__(self, master)
        global pathCarpetaD
        global pathCarpetaF

        #Funciones
        def seleccionarCarpetaD():
            global pathCarpetaD
            pathCarpetaD = filedialog.askdirectory(initialdir="/",  title='Seleccionar directorio')

        def seleccionarCarpetaF():
            global pathCarpetaF
            pathCarpetaF = filedialog.askdirectory(initialdir="/",  title='Seleccionar directorio') 
        

        #Etiquetas
        eCarpetaFuente = Label(self, text="Carpeta Fuente")
        eDestino = Label(self, text="Destino")

        #botones
        boton1 = Button(self, text = "Seleccionar Carpeta", command = seleccionarCarpetaF) #seleccionar carpeta fuente
        boton2 = Button(self, text = "Seleccionar Carpeta", command = seleccionarCarpetaD) #seleccionar carpeta destino
        botonSig =  Button(self, text = "Siguiente", command = lambda: master.cambiarVentana(VentanaSync)) #Botón siguiente

        #Orden de widgets en pantalla
        eCarpetaFuente.grid(row = 1, column = 1)
        eDestino.grid(row = 10, column = 1)
       
        boton1.grid(row = 1, column = 20)
        boton2.grid(row = 10, column = 20)
        botonSig.grid(row = 30, column = 30)
        
class VentanaSync(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        global pathCarpetaF     #acceso a variable global que almacena path de carpeta fuente
        listaCanciones = Listbox(self)      #Lista dinámica de canciones en carpeta
        os.chdir(pathCarpetaF)      #se establece como path la carpeta fuente
        for cancion in glob.glob("*.mp3"):
            listaCanciones.insert(END,cancion)
        listaCanciones.grid(row = 10, column =1)







#posiciones GUI pantalla selección carpetas



if __name__ == "__main__":
    app = Sync()
    app.mainloop()
