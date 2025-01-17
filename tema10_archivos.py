## Archivos

from io import open

text = "Este es un archivo de texto"



archivo = open("archivo.txt", "w")
archivo.write(text)
text = "\n Este es otro linea"
archivo.write(text)
archivo.close()

