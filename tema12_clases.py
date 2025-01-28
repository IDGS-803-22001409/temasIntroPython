## Clases

class OperasBas:
    # Aclaracion de propiedades

    """
    _num1 = 0   #privado
    num2 = 0    #publico
    __res = 0   #protected
    """
    
    num1 = 0   
    num2 = 0    
    res = 0   

    # Aclaracion de constructor de la clase
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    # Aclaracion de metodos de la clase
    def suma(self):
        self.res = self.num1 + self.num2
        print("El resultado es {}".format(self.res))

    def resta(self):
        self.res = self.num1 - self.num2
        print("El resultado es {}".format(self.res))

    def multiplicacion(self):
        self.res = self.num1 * self.num2
        print("El resultado es {}".format(self.res))

    def division(self):
        self.res = self.num1 / self.num2
        print("El resultado es {}".format(self.res))

def main():
    object = OperasBas(3,5)
    object.suma()
    object.resta()
    object.multiplicacion()
    object.division()

if __name__ == "__main__":
    main()