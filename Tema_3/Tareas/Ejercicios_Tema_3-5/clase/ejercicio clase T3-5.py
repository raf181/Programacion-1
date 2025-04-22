contador = 0
def calculadora(op1, op2, op):
    try:
        if op == "+":
            result = (op1 + op2)
        elif op == "-":
            result = (op1 - op2)
        elif op == "*":
            result = (op1 * op2)
        elif op == "/":
            if op2 == 0:
                return "No se puede dividir por 0"
            result = (op1 / op2)
        else:
            return "Operador no válido"
        return result
    
    except Exception as e:
        return "Error en el operador"

def diccionario(op1, op2, op): 
    global contador  # Se declara la variable contador como global para poder modificarla dentro de la función diccionario 
    result = calculadora(op1, op2, op)  # Se llama a la función calculadora
    contador += 1
    d = {
        contador: {
            "op1": op1,
            "op2": op2,
            "op": op,
            "result": result
        }
    }
    print(d)

diccionario(5, 4, "+")
diccionario(5, 4, "-")
diccionario(5, 4, "*")
diccionario(5, 0, "/")
diccionario(5, 4, "a")