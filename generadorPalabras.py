import itertools
import array

#Creo una lista con todas las palabras del diccionario de la RAE.
dict = [line.rstrip('\n') for line in open("listado-general.txt", "r", encoding= "utf8")]

#Esta función separa la palabra dada en una lista de Chars y genera todo las permutaciones posibles, compara estas con 
#la lista de las palabras de la RAE y devuelve solo las que existan en esta.
def generadorPalabras(letras, numero):
    listaLetras = list(letras)
    listaPosibles = []
    listaFinal = []
    for subset in itertools.permutations(listaLetras, numero):
        listaPosibles.append(''.join(subset))
    for palabra in listaPosibles:
        if palabra in dict:
            listaFinal.append(palabra)
    setFinal = set(listaFinal)
    return (', '.join(setFinal))


