def son_multiplos(num1, num2):
    if num1 == 0 or num2 == 0:
        return False
    return num1 % num2 == 0 or num2 % num1 == 0


def buscar_elemento(lista, elemento):
    try:
        posicion = lista.index(elemento)
        return True, posicion
    except ValueError:
        return False, -1


def calcular_media(*numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


def espaciar_texto(texto):
    resultado = ""
    for letra in texto:
        resultado += letra + "  "
    return resultado


def encontrar_extremo(lista_numeros, maximo=True):
    if not lista_numeros:
        return None
    if maximo:
        return max(lista_numeros)
    else:
        return min(lista_numeros)


# ====== PRUEBAS DE LAS FUNCIONES ======

# 1.Pruebas para son_multiplos
print("===== PRUEBA DE LA FUNCIÓN SON_MULTIPLOS =====")
print(f"son_multiplos(10, 5) = {son_multiplos(10, 5)}") # True, 10 es múltiplo de 5
print(f"son_multiplos(7, 3) = {son_multiplos(7, 3)}")   # False
print(f"son_multiplos(0, 5) = {son_multiplos(0, 5)}")   # False, cero es un caso especial
print(f"son_multiplos(15, 3) = {son_multiplos(15, 3)}") # True, 15 es múltiplo de 3
print()

# 2.Pruebas para buscar_elemento
print("===== PRUEBA DE LA FUNCIÓN BUSCAR_ELEMENTO =====")
mi_lista = [10, 20, 30, 40, 50]
print(f"Lista de prueba: {mi_lista}")
print(f"buscar_elemento(mi_lista, 30) = {buscar_elemento(mi_lista, 30)}") # (True, 2)
print(f"buscar_elemento(mi_lista, 60) = {buscar_elemento(mi_lista, 60)}") # (False, -1)
print(f"buscar_elemento(mi_lista, 10) = {buscar_elemento(mi_lista, 10)}") # (True, 0)
print()

# 3.Pruebas para calcular_media
print("===== PRUEBA DE LA FUNCIÓN CALCULAR_MEDIA =====")
print(f"calcular_media(10, 20, 30, 40, 50) = {calcular_media(10, 20, 30, 40, 50)}") # 30.0
print(f"calcular_media(5, 10) = {calcular_media(5, 10)}") # 7.5
print(f"calcular_media() = {calcular_media()}") # 0
print(f"calcular_media(100) = {calcular_media(100)}") # 100.0
print()

# 4.Pruebas para espaciar_texto
print("===== PRUEBA DE LA FUNCIÓN ESPACIAR_TEXTO =====")
texto_prueba = "Hola"
print(f"Texto original: '{texto_prueba}'")
print(f"Texto espaciado: '{espaciar_texto(texto_prueba)}'") # 'H  o  l  a  '
print(f"espaciar_texto('Python') = '{espaciar_texto('Python')}'") # 'P  y  t  h  o  n  '
print()

# 5.Pruebas para encontrar_extremo
print("===== PRUEBA DE LA FUNCIÓN ENCONTRAR_EXTREMO =====")
numeros = [15, 7, 23, 4, 42, 8]
print(f"Lista de números: {numeros}")
print(f"encontrar_extremo(numeros) = {encontrar_extremo(numeros)}") # 42 (máximo por defecto)
print(f"encontrar_extremo(numeros, False) = {encontrar_extremo(numeros, False)}") # 4 (mínimo)
print(f"encontrar_extremo([]) = {encontrar_extremo([])}") # None (lista vacía)
print(f"encontrar_extremo([100]) = {encontrar_extremo([100])}") # 100 (un solo elemento)