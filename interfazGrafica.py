#Importo tkinter para generar la interfaz gráfica y generadorPalabras como backEnd
from tkinter import *
from tkinter.ttk import *
from generadorPalabras import *

#Creación de la ventana y nombre
root = Tk()
root.geometry("650x500")
root.title ("GENERADOR DE PALABRAS")

#VARIABLES: inputLetras serán las letras de las que el usuario quiere generar palabras
#inputNumero es el numero de letras con el que queremos que se formen las palabras
#outputSolucion es la variable que albergará lo que queremos que se muestre por pantalla
inputLetras = StringVar()
inputNumero = IntVar()
outputSolucion = StringVar()

#FUNCIONES, input_letras e input_numero sirven a botonGenerar para dar a la función dentro de GENERADORDEPALABRAS 
#de los parámetros, luego borramos todo texto que pudiera haber en nuestro output e introducimos la solución a través
#de la variable outputSolucion
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

#ELEMENTOS de la interfaz:
escribeLetras = Label(root, text = "Escribe todas las letras seguidas: ").pack(pady = 20)
textoInput = Text(root, bg = "white", bd= 3, height =1, width = 10)
textoInput.pack()
escribeNumero = Label(root, text = "Escribe el número de letras de la palabra que buscas: ").pack(pady = 20)
numeroInput = Text(root, bg = "white", bd= 3, height =1, width = 5)
numeroInput.pack()

generarBoton = Button(root, text = "GENERAR", cursor = "cross", command = botonGenerar).pack(pady = 10)

textoOutput = Text(root, bg = "white", bd= 3, height =10, width = 70)
textoOutput.pack(pady = 20)

#Final
root.mainloop()
