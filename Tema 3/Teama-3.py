
# Variables y tipos básicos
nombre = "Rafael"
edad = 19

# Ejemplo de help() y dir()
print("=== Información de objetos ===")
# help(nombre)  # Comentado para no mostrar toda la ayuda
print(dir(edad))

# Asignación múltiple
print("\n=== Asignación múltiple ===")
x, y, z = "Amarillo", "Azul", "Rojo"
print(x)
print(y, z)
print(y, z, end="")

# Mismo valor para múltiples variables
print("\n\n=== Mismo valor para variables ===")
x = y = z = "Hola"
print("El valor de x es: " + x)
print(f"El valor de y es {y}")

# Tipos de datos
print("\n=== Tipos de datos ===")
numero_entero = 10
numero_decimal = 10.5
texto = "Python"
booleano = True

print(f"Entero: {type(numero_entero)}")
print(f"Decimal: {type(numero_decimal)}")
print(f"Texto: {type(texto)}")
print(f"Booleano: {type(booleano)}")

# Operaciones con strings
print("\n=== Operaciones con strings ===")
texto = "hola"
print(f"Original: {texto}")
print(f"Capitalize: {texto.capitalize()}")
print(f"Mayúsculas: {texto.upper()}")
print(f"Minúsculas: {texto.lower()}")
print(f"Reemplazar: {texto.replace('o', 'a')}")
print(f"Contar 'o': {texto.count('o')}")
print(f"Encontrar 'l': {texto.find('l')}")

# Casting
print("\n=== Casting ===")
x = int(1)
y = float(3)
z = str(10)
print(f"x es {x} de tipo {type(x)}")
print(f"y es {y} de tipo {type(y)}")
print(f"z es {z} de tipo {type(z)}")

# Estructuras de control
print("\n=== Estructuras de control ===")
a = 5
b = 10

if a < b:
    print("a es menor que b")
elif a > b:
    print("a es mayor que b")
else:
    print("a es igual a b")

# Punto de depuración recomendado
print("\n=== Sección para depuración ===")
x = 2
y = 2
if x == y:
    print("Los números son iguales")
else:
    print("Los números son diferentes")
