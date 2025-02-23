
# Ejercicio 1
print("\n--- Ejercicio 1 ---")
asignaturas = ["Matemáticas", "Programación", "Historia", "Economía"]
asignaturas_filtradas = [asig for asig in asignaturas if 'o' not in asig.lower()]

print("Asignaturas sin la letra 'o':")
for asignatura in asignaturas_filtradas:
    print(asignatura)

# Ejercicio 2
print("\n--- Ejercicio 2 ---")
nombres = ["Juan", "Ana", "Pedro", "María", "Carlos", "Elena"]

print("Elementos sin el primero y último:")
for nombre in nombres[1:-1]:
    print(nombre)

print("\nBorrando los dos últimos elementos...")
nombres = nombres[:-2]
print("Lista final:", nombres)

# Ejercicio 3
print("\n--- Ejercicio 3 ---")
while True:
    try:
        n = int(input("Introduce un número entre 3 y 20: "))
        if 3 <= n <= 20:
            break
        print("El número debe estar entre 3 y 20")
    except ValueError:
        print("Por favor, introduce un número válido")

numeros = []
for i in range(n):
    while True:
        try:
            num = int(input(f"Introduce el número {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor, introduce un número válido")

numeros.sort()
print(f"\nLista ordenada: {numeros}")

# Calcular elementos centrales
if len(numeros) % 2 == 0:
    # Lista par - mostrar 2 elementos centrales
    medio = len(numeros) // 2
    print(f"Elementos centrales: {numeros[medio-1:medio+1]}")
else:
    # Lista impar - mostrar 3 elementos centrales
    medio = len(numeros) // 2
    print(f"Elementos centrales: {numeros[medio-1:medio+2]}")
