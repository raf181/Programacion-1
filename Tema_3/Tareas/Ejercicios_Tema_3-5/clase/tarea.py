# Diccionario para almacenar el historial de operaciones
historial = {}
contador = 0

def Calculadora(op1, op2, op):
    global contador
    contador += 1
    
    # Inicializar el registro para esta operación
    registro = { "op1": op1, "op2": op2, "op": op}
    
    try:
        # Realizar la operación según el operador
        if op == "+":
            resultado = op1 + op2
        elif op == "-":
            resultado = op1 - op2
        elif op == "*":
            resultado = op1 * op2
        elif op == "/":
            if op2 == 0:
                raise ZeroDivisionError("División por cero")
            resultado = op1 / op2
        else:
            raise ValueError(f"Operador no válido: {op}")
        
        # Registrar el resultado
        registro["result"] = resultado
        
    except Exception as e:
        # Registrar el error
        registro["error"] = str(e)
        resultado = None
    
    # Guardar el registro en el historial
    historial[str(contador)] = registro
    
    return resultado

# Ejemplos de uso (una llamada por cada tipo de operación)
suma = Calculadora(5, 4, "+")
resta = Calculadora(10, 3, "-")
multiplicacion = Calculadora(6, 7, "*")
division = Calculadora(20, 4, "/")
division_error = Calculadora(8, 0, "/")
operacion_invalida = Calculadora(5, 5, "?")

# Mostrar el historial completo
print("Historial de operaciones:")
for clave, valor in historial.items():
    print(f"{clave}: {valor}")
