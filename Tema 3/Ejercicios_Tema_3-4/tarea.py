

# 1. Crear diccionario con los elementos requeridos
mi_diccionario = {
    "numeros": [1, 2, 3, 4, 5],
    "precio": 19.99,
    "coordenadas": (10, 20, 30),
    "nombre": "Juan",
    "ciudad": "Madrid"
}

# 2. Imprimir valor float
print("\nValor float:", mi_diccionario["precio"])

# 3. Bucles para recorrer la lista
print("\nRecorriendo lista con for:")
for numero in mi_diccionario["numeros"]:
    print(numero)

print("\nRecorriendo lista con while:")
i = 0
while i < len(mi_diccionario["numeros"]):
    print(mi_diccionario["numeros"][i])
    i += 1

# 4. Añadir elemento a la lista
mi_diccionario["numeros"].append(6)
print("\nLista actualizada:", mi_diccionario["numeros"])

# 5. Modificar texto
mi_diccionario["nombre"] = "Pedro"
print("\nNuevo nombre:", mi_diccionario["nombre"])

# 6. Imprimir último valor de la tupla
print("\nÚltimo valor de la tupla:", mi_diccionario["coordenadas"][-1])

# 7. Imprimir parejas clave-valor
print("\nParejas clave-valor:")
for clave, valor in mi_diccionario.items():
    print(f"CLAVE: '{clave}' - VALOR: '{valor}'")

# 8. Añadir entero y eliminar tupla
del mi_diccionario["coordenadas"]
mi_diccionario["edad"] = 25
print("\nNueva pareja añadida - CLAVE: 'edad' - VALOR:", mi_diccionario["edad"])

# 9. Crear copia y modificar valores
diccionario_copia = mi_diccionario.copy()
diccionario_copia["nombre"] = "Ana"
diccionario_copia["ciudad"] = "Barcelona"

print("\nDiccionario original:", mi_diccionario)
print("Diccionario copia:", diccionario_copia)

# 10. Añadir diccionario anidado
diccionario_copia["datos_extra"] = {
    "telefono": "123456789",
    "email": "ejemplo@mail.com"
}

print("\nDiccionario con diccionario anidado:")
for clave, valor in diccionario_copia.items():
    print(f"CLAVE: '{clave}' - VALOR: '{valor}'")
