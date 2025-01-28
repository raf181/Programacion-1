
# Declaración de variables básicas para demostración
# nombre: almacena una cadena de texto
# edad: almacena un número entero
nombre = "Rafael"
edad = 19

# Demostración de funciones de información de objetos
# dir(): muestra todos los métodos y atributos disponibles para el objeto
print("=== Información de objetos ===")
# help(nombre)  # Muestra la documentación completa del objeto (comentado)
print(dir(edad))

# Demostración de asignación múltiple de variables
# Asigna tres valores diferentes a tres variables en una sola línea
print("\n=== Asignación múltiple ===")
x, y, z = "Amarillo", "Azul", "Rojo"
print(x)  # Imprime solo el primer valor
print(y, z)  # Imprime dos valores con salto de línea
print(y, z, end="")  # Imprime sin salto de línea al final

# Demostración de asignación del mismo valor a múltiples variables
print("\n\n=== Mismo valor para variables ===")
x = y = z = "Hola"  # Todas las variables reciben el mismo valor
print("El valor de x es: " + x)  # Concatenación tradicional
print(f"El valor de y es {y}")  # f-string (formato moderno)

# Demostración de diferentes tipos de datos en Python
print("\n=== Tipos de datos ===")
numero_entero = 10    # Tipo int
numero_decimal = 10.5 # Tipo float
texto = "Python"      # Tipo str
booleano = True       # Tipo bool

# Muestra el tipo de cada variable usando type()
print(f"Entero: {type(numero_entero)}")
print(f"Decimal: {type(numero_decimal)}")
print(f"Texto: {type(texto)}")
print(f"Booleano: {type(booleano)}")

# Demostración de operaciones básicas con cadenas
# ...existing code for string operations...

# Demostración de conversión de tipos (casting)
print("\n=== Casting ===")
x = int(1)    # Conversión a entero
y = float(3)  # Conversión a decimal
z = str(10)   # Conversión a cadena
print(f"x es {x} de tipo {type(x)}")
print(f"y es {y} de tipo {type(y)}")
print(f"z es {z} de tipo {type(z)}")

# Demostración de estructuras de control condicionales
print("\n=== Estructuras de control ===")
a = 5
b = 10

# Ejemplo de if-elif-else para comparación de números
if a < b:
    print("a es menor que b")
elif a > b:
    print("a es mayor que b")
else:
    print("a es igual a b")

# Sección para práctica de depuración
# Punto recomendado para colocar breakpoints
print("\n=== Sección para depuración ===")
x = 2
y = 2
if x == y:
    print("Los números son iguales")
else:
    print("Los números son diferentes")
