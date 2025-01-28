class Diccionario:
    archivo = "C:/Users/checo/Desktop/Phyton/temasIntroPython/diccionario.txt"

    def __init__(self, ruta_archivo):
        self.archivo = ruta_archivo
        self.palabras = []
        self.cargar_palabras()

    def cargar_palabras(self):
            with open(self.archivo, 'r') as archivo:
                for linea in archivo:
                    esp, ing = linea.strip().split(": ")
                    self.palabras.append((esp, ing))  

    def guardar_palabras(self):
        with open(self.archivo, 'w') as archivo:
            for esp, ing in self.palabras:
                archivo.write(f"{esp}: {ing}\n")

    def menu(self):
        while True:
            print("---Diccionario---")
            print("¿Qué deseas realizar en el diccionario de palabras?")
            print("1.- Capturar una nueva palabra")
            print("2.- Buscar una palabra")
            print("3.- Salir del diccionario")
            opcion = input("Opción: ")
            if opcion == "1":
                self.capturar_palabras()
            elif opcion == "2":
                self.buscar_palabra()
            elif opcion == "3":
                break
            else:
                print("Opción no encontrada")

    def capturar_palabras(self):
        español = input("Escribe la palabra en español: ")
        ingles = input("Escribe la palabra en inglés: ")
        self.palabras.append((español.capitalize(), ingles.capitalize()))
        self.guardar_palabras()
        print("Palabra capturada con éxito.")

    def buscar_palabra(self):
        opcion = input("Buscar palabra en:\n1.- Español\n2.- Inglés\nOpción: ")
        palabra = input("Palabra a buscar: ").capitalize()
        encontrada = False

        for esp, ing in self.palabras:
            if opcion == "1" and esp == palabra:
                print(f"Palabra encontrada: {ing}")
                encontrada = True
                break
            elif opcion == "2" and ing == palabra:
                print(f"Palabra encontrada: {esp}")
                encontrada = True
                break

        if not encontrada:
            print("Palabra no encontrada")

def main():
    diccionario = Diccionario('diccionario.txt')
    diccionario.menu()

if __name__ == "__main__":
    main()
