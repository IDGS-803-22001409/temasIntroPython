## leer

from io import open

text = ""

archivo = open("archivo.txt", "r")

text = archivo.readlines()
print(text)

archivo.close()

