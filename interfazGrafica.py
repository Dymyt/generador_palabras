from tkinter import *
from tkinter.ttk import *
from generadorPalabras import *

root = Tk()
root.geometry("650x500")
root.title ("GENERADOR DE PALABRAS")

#Variables

inputLetras = StringVar()
inputNumero = IntVar()
outputSolucion = StringVar()
#Funciones
def retrieve_input_letras():
    inputLetras.set(textoInput.get("1.0",END))
def retrieve_input_numero():
    inputNumero.set(numeroInput.get("1.0",END))
def botonGenerar():
    retrieve_input_letras()
    retrieve_input_numero()
    outputSolucion.set(generadorPalabras(inputLetras.get(), inputNumero.get()))
    textoOutput.delete('1.0', END)
    textoOutput.insert(INSERT,  outputSolucion.get())




#ELEMENTOS
escribeLetras = Label(root, text = "Escribe todas las letras seguidas: ").pack(pady = 20)
textoInput = Text(root, bg = "white", bd= 3, height =1, width = 10)
textoInput.pack()
escribeNumero = Label(root, text = "Escribe el número de letras de la palabra que buscas: ").pack(pady = 20)
numeroInput = Text(root, bg = "white", bd= 3, height =1, width = 5)
numeroInput.pack()

generarBoton = Button(root, text = "GENERAR", cursor = "cross", command = botonGenerar).pack(pady = 10)

textoOutput = Text(root, bg = "white", bd= 3, height =10, width = 70)
textoOutput.pack(pady = 20)


root.mainloop()