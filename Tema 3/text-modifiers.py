# Imprime el encabezado para la sección de operaciones con cadenas
print("\n=== Operaciones con strings ===")

# Define una variable de texto para pruebas
texto = "holla"

# Imprime la cadena original sin modificaciones
print(f"Original: {texto}")

# capitalize(): Convierte el primer carácter a mayúscula, el resto a minúsculas
print(f"Primera letra en mayúscula: {texto.capitalize()}")

# upper(): Convierte todos los caracteres a mayúsculas
print(f"Todo en mayúsculas: {texto.upper()}")

# lower(): Convierte todos los caracteres a minúsculas
print(f"Todo en minúsculas: {texto.lower()}")

# replace(): Reemplaza todas las ocurrencias del primer argumento por el segundo
print(f"Reemplazar 'o' por 'a': {texto.replace('o', 'a')}")

# count(): Cuenta cuántas veces aparece una subcadena en el texto
print(f"Número de veces que aparece 'l': {texto.count('l')}")

# find(): Devuelve el índice de la primera aparición de la subcadena
print(f"Posición de la primera 'l': {texto.find('l')}")