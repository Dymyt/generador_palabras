import itertools
import array

#dict =  open("listado-general.txt", "r", encoding="utf8")
dict = [line.rstrip('\n') for line in open("listado-general.txt", "r", encoding= "utf8")]

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

print (generadorPalabras("awoenfw", 3))


