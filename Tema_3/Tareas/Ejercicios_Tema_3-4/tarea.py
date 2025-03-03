# 1. Crea un diccionario con 5 parejas clave-valor. Tiene que haber:
#         - Una lista.
#         - Una variable de tipo float.
#         - Una tupla.
#         - Dos variables de tipo texto.
# 2. Imprime el contenido de la variable de tipo float que has creado dentro del diccionario.
# 3. Mediante un bucle for, imprime cada uno de los elementos de la lista que has creado dentro del diccionario.
# Haz lo mismo con un bucle while (usa la imaginación).
# 4. Añade un nuevo elemento a la lista que has creado dentro del diccionario e imprime la lista.
# 5. Modifica el valor de una de las variables de tipo texto que has creado dentro del diccionario e imprime su nuevo valor por pantalla.
# 6. Imprime el último valor de la tupla que has creado dentro del diccionario.
# 7. Mediante un bucle for imprime todas las parejas clave-valor del diccionario.
# Ejemplo de la salida esperada de una pareja de clave valor -> CLAVE: 'Apellido1' - VALOR: 'Carreras'.
# RESPETAD ESTE EJEMPLO.
# 8. Añade una nueva pareja clave-valor de tipo entero y elimina completamente la tupla que ya existía en el diccionario. Imprime solo la nueva pareja clave-valor añadida.
# 9. Crea una copia del diccionario y modifica el valor de 2 parejas clave-valor. Imprime el nuevo diccionario y el original.
# 10. En el nuevo diccionario, añade dentro de él otro diccionario con al menos 2 parejas clave-valor.
#  Imprime por pantalla el diccionario que tiene otro diccionario dentro, mediante un bucle for.

# Define codigos de colo solo para output en terminal
# Pa mi que es mas facil hacer debug, lo he sacado de stak overflow
DEBUG_COLOR = '\033[38;5;208m'  # Orange 
NORMAL_COLOR = '\033[94m'       # Blue
RESET_COLOR = '\033[0m'         # Reset to default

# 1. ...
mi_diccionario = {
    "numeros": [1, 2, 3, 4, 5],
    "precio": 19.99,
    "coordenadas": (10, 20, 30),
    "nombre": "Pepe",
    "ciudad": "Cadiz"
}

# 2. ...
print(f"\n{NORMAL_COLOR}Valor float:{RESET_COLOR}", mi_diccionario["precio"])

# 3. ...
print(f"\n{NORMAL_COLOR}Recorriendo lista con for:{RESET_COLOR}")
for numero in mi_diccionario["numeros"]:
    print(f"  {numero}")

print(f"\n{NORMAL_COLOR}Recorriendo lista con while:{RESET_COLOR}")
# Iicializar contador
i = 0
while i < len(mi_diccionario["numeros"]):
    print(f"  {mi_diccionario['numeros'][i]}")
    i += 1 # Incrementar contador

# 4. ...
mi_diccionario["numeros"].append(6)
print(f"\n{NORMAL_COLOR}Lista actualizada:{RESET_COLOR}")
i = 0 # Reiniciar contador
while i < len(mi_diccionario["numeros"]):
    print(f"  {mi_diccionario['numeros'][i]}")
    i += 1 # Incrementar contador
i = None # Liberar variable

# 5. ...
mi_diccionario["nombre"] = "Pedro"
print(f"\n{NORMAL_COLOR}Nuevo nombre:{RESET_COLOR}", mi_diccionario["nombre"])

# 6. ...
print(f"\n{NORMAL_COLOR}Último valor de la tupla:{RESET_COLOR}", mi_diccionario["coordenadas"][-1])

# 7. ...
print(f"\n{NORMAL_COLOR}Diccionario con diccionario anidado:{RESET_COLOR}")
# Esto lo hice para el 10 (No era necesario), por eso tiene tambien para manejar el caso de que el valor de una clave sea un diccionario
for clave, valor in mi_diccionario.items():
    if isinstance(valor, (dict, list, tuple)):
        # la variable clave se imprime entre comillas simples para que sea mas claro que es una clave, por comodidad pero se que no es necesario
        print(f"{NORMAL_COLOR}CLAVE:{RESET_COLOR} '{clave}':")
        # Si es un diccionario, lista o tupla, recorrer sus elementos y imprimirlos con un formato decente
        if isinstance(valor, dict):
            # Convertir el diccionario a una lista de tuplas para recorrerlo
            items = list(valor.items())
            for i, (subclave, subvalor) in enumerate(items):
                # "└─" si es el último elemento, "├─" si no; "Idea" de ChatGPT
                branch = "└─" if i == len(items) - 1 else "├─"
                print(f"{NORMAL_COLOR}  {branch} {RESET_COLOR}{subclave}: {subvalor}")
        else:  # Para las listas y tuplas
            for i, item in enumerate(valor):
                # "└─" si es el último elemento, "├─" si no; "Idea" de ChatGPT
                branch = "└─" if i == len(valor) - 1 else "├─"
                print(f"{NORMAL_COLOR}  {branch} {RESET_COLOR}{item}")
    else:
        # Si no es un diccionario, lista o tupla, imprimir la clave y el valor de forma simple
        print(f"{NORMAL_COLOR}CLAVE:{RESET_COLOR} '{clave}' → {valor}")

# 8. ...
del mi_diccionario["coordenadas"]
mi_diccionario["edad"] = 25
print(f"\n{NORMAL_COLOR}Nueva pareja añadida:{RESET_COLOR}")
print(f"{NORMAL_COLOR}CLAVE:{RESET_COLOR} 'edad' → {mi_diccionario['edad']}")

# 9. ...
diccionario_copia = mi_diccionario.copy()
# mi_diccionario = None # Liberar variable
diccionario_copia["nombre"] = "Paco"
diccionario_copia["ciudad"] = "Barcelona"

print(f"\n{NORMAL_COLOR}Diccionario original {RESET_COLOR} → {mi_diccionario}") # 
print(f"{NORMAL_COLOR}Diccionario copia {RESET_COLOR} → {diccionario_copia}")

# 10. ...
diccionario_copia["datos_extra"] = {
    "telefono": "123456789",
    "email": "ejemplo@dominio.com"
}

print(f"\n{NORMAL_COLOR}Diccionario con diccionario anidado:{RESET_COLOR}")
# Solo mostrar el diccionario anidado
for clave, valor in diccionario_copia.items():
    # Is instance para manejar el caso de que el valor de una clave sea un diccionario
    if isinstance(valor, dict):
        print(f"{NORMAL_COLOR}CLAVE:{RESET_COLOR} '{clave}':")
        items = list(valor.items())
        for i, (subclave, subvalor) in enumerate(items):
            branch = "└─" if i == len(items) - 1 else "├─"
            print(f"{NORMAL_COLOR}  {branch} {RESET_COLOR}{subclave}: {subvalor}")
