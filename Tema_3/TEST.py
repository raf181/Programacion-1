class Calculadora:
    def __init__(self, numero1=None, numero2=None, operador=None):
        self.numero1 = numero1
        self.numero2 = numero2
        self.operador = operador
    
    def calcular(self, numero1=None, numero2=None, operador=None):
        # Si no se proporcionan argumentos, solicitar al usuario
        if numero1 is None:
            try:
                numero1 = int(input("Introduce el primer número: "))
            except ValueError:
                return "Error: Debe introducir un número"
                
        if numero2 is None:
            try:
                numero2 = int(input("Introduce el segundo número: "))
            except ValueError:
                return "Error: Debe introducir un número"
                
        if operador is None:
            operador = input("Introduce el operador (+, -, *, /): ")
            
        # Realizar la operación según el operador
        if operador == "+":
            return numero1 + numero2
        elif operador == "-":
            return numero1 - numero2
        elif operador == "*":
            return numero1 * numero2
        elif operador == "/":
            if numero2 == 0:
                return "Error: No se puede dividir entre cero"
            return numero1 / numero2
        else:
            return "Error: Operador no válido. Use +, -, * o /"