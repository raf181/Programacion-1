# Ejercicio 1
# 1. Imprime por pantalla tu nombre y apellidos capitalizados.
# Crea una variable de tipo int con tu año de nacimiento e imprime por pantalla tu edad en este año (Ej: "Mi edad
# es X años").
# Crea una variable de tipo bool que sea False e imprímela por pantalla.
# Crea dos variables de tipo float con 2 decimales y muestra por pantalla la resta
# de ambas.

print("\n--- Ejercicio 1 ---")
nombre_completo = "rafael perez garcia"
print(nombre_completo.title())  # Capitaliza cada palabra

año_nacimiento = 2000
edad = 2024 - año_nacimiento
print(f"Mi edad es {edad} años")

variable_booleana = False
print(variable_booleana)

float1 = 10.25
float2 = 5.75
print(f"La resta es: {float1 - float2:.2f}")

# Ejercicio 2
# 2. Crea una variable de tipo tupla, otra de tipo lista, otra de tipo cadena y otra que sea un float con los valores que quieras e imprímelos por pantalla siguiendo el siguiente orden:
# 1º float
# 2º Cadena
# 3º Lista
# 4º Tupla

print("\n--- Ejercicio 2 ---")
mi_float = 3.14
mi_cadena = "Hola Mundo"
mi_lista = [1, 2, 3, 4]
mi_tupla = (5, 6, 7, 8)

print(mi_float)
print(mi_cadena)
print(mi_lista)
print(mi_tupla)

# Ejercicio 3
# 3. Realiza una operación de suma, otra de resta, otra de multiplicación y otra de división e imprímelos en el siguiente orden:
# 1º Resta
# 2º Suma
# 3º Multiplicación
# 4º División

print("\n--- Ejercicio 3 ---")
num1 = 10
num2 = 5

print(f"Resta: {num1 - num2}")
print(f"Suma: {num1 + num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# Ejercicio 4
# 4. Crea 5 números enteros en una sola línea de código que tengan el valor 6.
# Incrementa en 2 el valor del 1º de ellos.
# Decrementa en 1 el valor del 2º de ellos.
# Multiplica por 3 valor del 3º de ellos.
# Divide entre 2 valor del 4º de ellos.
# Calcula el módulo 2 del 5º de ellos.
# Imprime todos los números resultantes por pantalla.

print("\n--- Ejercicio 4 ---")
num1, num2, num3, num4, num5 = 6, 6, 6, 6, 6

num1 += 2
num2 -= 1
num3 *= 3
num4 /= 2
num5 %= 2

print(f"Número 1: {num1}")
print(f"Número 2: {num2}")
print(f"Número 3: {num3}")
print(f"Número 4: {num4}")
print(f"Número 5: {num5}")

# Ejercicio 5

# 5. Escribe las siguientes condiciones e imprime el mensaje por pantalla en cada caso
# (Recuerda que deberás rellenar las variables y en algún caso, crear tú alguna)
# Si tu edad es mayor o igual que 10 -> Imprime: "Soy mayor o igual de 10".
# Si no: Imprime tu edad.
# Si tu equipo es igual a "Real Madrid CF" -> Imprime: "Soy madridista".
# Si no: Imprime tu equipo (o si no tienes dilo!).
# Si tu número de zapato es mayor que 44 pero menor que 46 -> Imprime: "Tengo un 45".
# Si no: Imprime tu número de zapato.
print("\n--- Ejercicio 5 ---")
edad = 20
if edad >= 10:
    print("Soy mayor o igual de 10")
else:
    print(edad)

equipo = "Barcelona FC"
if equipo == "Real Madrid CF":
    print("Soy madridista")
else:
    print(equipo)

numero_zapato = 42
if 44 < numero_zapato < 46:
    print("Tengo un 45")
else:
    print(numero_zapato)

ciudad = "Madrid"
if ciudad == "Pozuelo" or ciudad == "Majadahonda":
    print("Vivo cerca de la UFV")
else:
    print(ciudad)
