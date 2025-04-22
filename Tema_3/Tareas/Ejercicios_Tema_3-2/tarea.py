
# Ejercicio 1
# 1. Crea una lista con las asignaturas que tienes este cuatrimestre (al menos 4).
# Muestra por pantalla las asignaturas que están en índices pares, por separado.
# Muestra todas las asignaturas menos la primera, por separado.

print("\n--- Ejercicio 1 ---")
asignaturas = ["Matemáticas", "Programación", "Física", "Historia"]

print("Asignaturas en índices pares:")
print(asignaturas[0])
print(asignaturas[2])

print("\nTodas las asignaturas menos la primera:")
for asignatura in asignaturas[1:]:
    print(asignatura)

# Ejercicio 2
# 2. Crea una tupla con al menos 6 elementos.
# Muestra por pantalla el tamaño de la tupla.
# Muestra por pantalla cada uno de los valores de la tupla.

print("\n--- Ejercicio 2 ---")
mi_tupla = (1, "Python", 3.14, True, "Hola", [1, 2, 3])
print(f"Tamaño de la tupla: {len(mi_tupla)}")
print("\nElementos de la tupla:")
for elemento in mi_tupla:
    print(elemento)

# Ejercicio 3
# 3. Crea una lista que contenga:
# - Una tupla de ciudades (al menos 3).
# - Una lista de personas (al menos 3).
# - 1 número entero.
# - 1 cadena de texto.
# Imprime por pantalla los elementos de la tupla y de la lista por separado y con el siguiente formato para la tupla:
# "Elemento numero 1: Madrid"
# "Elemento numero 2: Santander"
# Para la lista deberá mostrar:
# "Alumno 0: Pedro"
# "Alumno 1: Ana"
# Además debe mostrar un texto indicando de que es cada tipo de la lista original. # 

print("\n--- Ejercicio 3 ---")
ciudades = ("Madrid", "Barcelona", "Valencia")
personas = ["Juan", "María", "Carlos"]
lista_mixta = [ciudades, personas, 42, "Texto de ejemplo"]

print("Elementos de la tupla:")
for i, ciudad in enumerate(ciudades, 1):
    print(f"Elemento numero {i}: {ciudad}")

print("\nElementos de la lista de personas:")
for i, persona in enumerate(personas):
    print(f"Alumno {i}: {persona}")

print("\nTipos de elementos en la lista original:")
for i, elemento in enumerate(lista_mixta):
    print(f"Elemento {i} es de tipo: {type(elemento)}")

# Ejercicio 4
# 4. Crea una lista con marcas (al menos 5).
# Imprime el contenido de la lista con los distintos tipos de bucles que hemos visto (cada marca en una línea).

print("\n--- Ejercicio 4 ---")
marcas = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour"]

print("Usando for:")
for marca in marcas:
    print(marca)

print("\nUsando while:")
i = 0
while i < len(marcas):
    print(marcas[i])
    i += 1

# Ejercicio 5
# 5. Crea un bucle for que vaya desde 66 al 122 y que imprima si el numero es divisible entre 2 o si lo es entre 3,
# En caso contrario indicará que no es divisible entre 2 ni 3. 

print("\n--- Ejercicio 5 ---")
for num in range(66, 123):
    if num % 2 == 0:
        print(f"{num} es divisible entre 2")
    elif num % 3 == 0:
        print(f"{num} es divisible entre 3")
    else:
        print(f"{num} no es divisible entre 2 ni 3")

# Ejercicio 6
# 6. Crea una variable de tipo cadena con el texto:
# "El episodio piloto se estrenó en más de 6 servicios en línea de video bajo demanda el 27 de mayo de 2015.
#  La temporada 1 se estrenó en USA Network el 24 de junio de 2015 y la segunda temporada el 13 de julio de 2016.
#  La tercera temporada, de 10 episodios, se estrenó el 11 de octubre de 2017.
#  En diciembre de 2017 se renovó la cuarta y última temporada de la serie,​ que fue estrenada el 6 de octubre de 2019."
#  - Muestra por pantalla cuantas aes aparecen en el texto.
#  - Muestra por pantalla cuantas veces aparece el año 2017 en el texto.
#  - Muestra por pantalla el numero total de letras que hay en el texto.
#  - Muestra cuantos espacios en blanco hay en el texto. 

print("\n--- Ejercicio 6 ---")
texto = """El episodio piloto se estrenó en más de 6 servicios en línea de video bajo demanda el 27 de mayo de 2015.
 La temporada 1 se estrenó en USA Network el 24 de junio de 2015 y la segunda temporada el 13 de julio de 2016.
 La tercera temporada, de 10 episodios, se estrenó el 11 de octubre de 2017.
 En diciembre de 2017 se renovó la cuarta y última temporada de la serie,​ que fue estrenada el 6 de octubre de 2019."""

print(f"Número de 'a' en el texto: {texto.lower().count('a')}")
print(f"Número de veces que aparece '2017': {texto.count('2017')}")
print(f"Número total de letras: {len(texto) - texto.count(' ')}")
print(f"Número de espacios en blanco: {texto.count(' ')}")
