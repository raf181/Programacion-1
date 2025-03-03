# Ejercicio 1
# Crea una lista con las asignaturas que tienes este cuatrimestre (al menos 4).
# Recorre la lista y todas las asignaturas que tengan la letra o, debes eliminarla de la lista.
# Muestra las asignaturas resultantes por pantalla por separado.
print("\n--- Ejercicio 1 ---")
asignaturas = ["Matemáticas", "Programación", "Historia", "Economía"]
# para crear una nueva lista solo con las asignaturas que no contienen 'o', lower() convierte el texto a minúsculas para detectar tanto 'o' como 'O'
asignaturas_filtradas = [asignatura for asignatura in asignaturas if 'o' not in asignatura.lower()]

print("Asignaturas sin la letra 'o':")
for asignatura in asignaturas_filtradas:
    print(asignatura)

# Ejercicio 2
# Crea una lista que contenga 6 nombres:
# - Imprime por pantalla todos los elementos menos el primero y el último.
# - Añade la operativa para que borre los 2 últimos elementos.

print("\n--- Ejercicio 2 ---")
nombres = ["Juan", "Ana", "Pedro", "María", "Carlos", "Elena"]

print("Elementos sin el primero y último:")
for nombre in nombres[1:-1]:
    print(nombre)

print("\nBorrando los dos últimos elementos...")
nombres = nombres[:-2]
for nombre in nombres:
    print(nombre)

# Ejercicio 3
# Haz un programa que pida al usuario (con input) un numero entre 3 y 20, ambos incluidos.
# Con ese número pedirá tantas veces como indique el número un valor numérico que almacenará en una lista.  
# Luego deberá ordenar la lista y mostrar los datos siguiendo la siguiente fórmula: 
#  - Si el numero de elementos de la lista es par, debe mostrar los dos elementos centrales de la lista. 
#  - Si es impar deberá mostrar los 3 elementos centrales de la lista. 
# Ejemplo: 
# - El usuario mete 5, y luego los valores 11, 3, 56, 34, 2. Deberá ordenarla, quedando la siguiente lista: [2, 3, 11, 34, 56]. Al tener 5 elementos debe mostrar por pantalla el 3, el 11 y el 34.
# - El usuario introduce 6, y luego los valores 11, 3, 56, 34, 2, 100. Deberá ordenarla, quedando la siguiente lista: [2, 3, 11, 34, 56, 100]. Al tener 6 elementos debe mostrar por pantalla el 11 y el 34.
print("\n--- Ejercicio 3 ---")
# Bucle principal que continúa hasta obtener una entrada válida
while True:
    try:
        n = int(input("Introduce un número entre 3 y 20: "))
        # Comprobar si el número "n" definida en el input está en el rango permitido
        if 3 <= n <= 20:
            # Salir del bucle si la entrada fue válida
            break
        print("El número debe estar entre 3 y 20")
    except ValueError:
        # ValueError se produce cuando int() no puede convertir la entrada a número
        # Por ejemplo, cuando el usuario introduce letras, símbolos o numeros fuera del rango
        print("Por favor, introduce un número válido")

numeros = []
for i in range(n):
    # Bucle que se repite hasta que se ingrese un número válido
    while True:
        try:
            # Solicitar y convertir la entrada del usuario a número entero
            num = int(input(f"Introduce el número {i+1}: "))
            numeros.append(num)
            # Salir del bucle si la entrada fue válida
            break
        except ValueError:
            # ValueError se produce cuando int() no puede convertir la entrada a número
            # Por ejemplo, cuando el usuario introduce letras o símbolos en vez de números
            print("Por favor, introduce un número válido")

numeros.sort()

# Calcular elementos centrales
medio = len(numeros) // 2
if len(numeros) % 2 == 0:
    # Lista par - mostrar 2 elementos centrales
    centrales = numeros[medio-1:medio+1]
    print(f"Al tener {len(numeros)} elementos (par) se muestran los dos del centro: {centrales[0]} y {centrales[1]}")
else:
    # Lista impar - mostrar 3 elementos centrales
    centrales = numeros[medio-1:medio+2]
    print(f"Al tener {len(numeros)} elementos (impar) se muestran los tres del centro: {centrales[0]}, {centrales[1]} y {centrales[2]}")
