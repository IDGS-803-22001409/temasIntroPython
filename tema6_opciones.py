## Opciones
import os

def funcion1(opcion):
    if opcion == 1:
        print("Opcion 1")
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    else:
        print("Opcion incorrecta")

def funcion2():
    print("funcion 2")

## Opciones de calculadora
def volverMenu():
    print('')
    print('Desea hacer otra operacion?')
    print("1. Si    2.No")
    opc = int(input("Escribe la opcion: "))
    if opc == 1:
        run()
    elif opc == 2:
        exit()

def suma():
    os.system("cls")
    print('Dame dos numero')
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print("El resultado es {}".format(num1 + num2))
    volverMenu()

def resta():
    os.system("cls")
    print('Dame dos numero')
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    print("El resultado es {}".format(num1 - num2))
    volverMenu()

def mulpiplicacion():
    os.system("cls")
    print('Dame dos numero')
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print("El resultado es {}".format(num1 * num2))
    volverMenu()

def division():
    os.system("cls")
    print('Dame dos numero')
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print("El resultado es {}".format(num1 / num2))
    volverMenu()

def run():
    os.system("cls")
    print('Menu de opciones')
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    operacion = int(input("Escribe la opcion: "))
    if operacion == 1:
        suma()
    elif operacion == 2:
        resta()
    elif operacion == 3:
        mulpiplicacion()
    elif operacion == 4:
        division()
    elif operacion == 5:
        exit()
    else:
        print("Opcion incorrecta")
    run()

if __name__ == "__main__":
    run()
