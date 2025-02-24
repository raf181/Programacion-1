# Define codigos de colo solo para output en terminal
# Pa mi que es mas facil hacer debug, lo he sacado de stak overflow
DEBUG_COLOR = '\033[38;5;208m'  # Orange 
NORMAL_COLOR = '\033[94m'       # Blue
RESET_COLOR = '\033[0m'         # Reset to default

# 1. Crear diccionario con los elementos requeridos
mi_diccionario = {
    "numeros": [1, 2, 3, 4, 5],
    "precio": 19.99,
    "coordenadas": (10, 20, 30),
    "nombre": "Juan",
    "ciudad": "Madrid"
}

# 2. Imprimir valor float
print(f"\n{NORMAL_COLOR}Valor float:{RESET_COLOR}", mi_diccionario["precio"])

# 3. Bucles para recorrer la lista
print(f"\n{NORMAL_COLOR}Recorriendo lista con for:{RESET_COLOR}")
for numero in mi_diccionario["numeros"]:
    print(f"  {numero}")

print(f"\n{NORMAL_COLOR}Recorriendo lista with while:{RESET_COLOR}")
i = 0
while i < len(mi_diccionario["numeros"]):
    print(f"  {mi_diccionario['numeros'][i]}")
    i += 1

# 4. Añadir elemento a la lista
mi_diccionario["numeros"].append(6)
print(f"\n{NORMAL_COLOR}Lista actualizada:{RESET_COLOR}", mi_diccionario["numeros"])

# 5. Modificar texto
mi_diccionario["nombre"] = "Pedro"
print(f"\n{NORMAL_COLOR}Nuevo nombre:{RESET_COLOR}", mi_diccionario["nombre"])

# 6. Imprimir último valor de la tupla
print(f"\n{NORMAL_COLOR}Último valor de la tupla:{RESET_COLOR}", mi_diccionario["coordenadas"][-1])

# 7. Imprimir parejas clave-valor
print(f"\n{NORMAL_COLOR}Parejas clave-valor:{RESET_COLOR}")
for clave, valor in mi_diccionario.items():
    print(f"{NORMAL_COLOR}CLAVE:{RESET_COLOR} '{clave}' → {valor}")

# 8. Añadir entero y eliminar tupla
del mi_diccionario["coordenadas"]
mi_diccionario["edad"] = 25
print(f"\n{NORMAL_COLOR}Nueva pareja añadida:{RESET_COLOR}")
print(f"{NORMAL_COLOR}CLAVE:{RESET_COLOR} 'edad' → {mi_diccionario['edad']}")

# 9. Crear copia y modificar valores
diccionario_copia = mi_diccionario.copy()
diccionario_copia["nombre"] = "Ana"
diccionario_copia["ciudad"] = "Barcelona"

print(f"\n{DEBUG_COLOR}Debug:{RESET_COLOR} Diccionario original → {mi_diccionario}")
print(f"{DEBUG_COLOR}Debug:{RESET_COLOR} Diccionario copia → {diccionario_copia}")

# 10. Añadir diccionario anidado
diccionario_copia["datos_extra"] = {
    "telefono": "123456789",
    "email": "ejemplo@mail.com"
}

print(f"\n{NORMAL_COLOR}Diccionario con diccionario anidado:{RESET_COLOR}")
for clave, valor in diccionario_copia.items():
    if isinstance(valor, dict):
        print(f"{NORMAL_COLOR}\nCLAVE:{RESET_COLOR} '{clave}':")
        for subclave, subvalor in valor.items():
            # "├─" es un carácter especial para representar rama de definiciones en un diccionario
            print(f"{NORMAL_COLOR}  ├─ {RESET_COLOR}{subclave}: {subvalor}")
    else:
        print(f"{NORMAL_COLOR}CLAVE:{RESET_COLOR} '{clave}' → {valor}")