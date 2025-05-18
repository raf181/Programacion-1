import os
import time
import random
import sys

class Jugador:
    def __init__(self, id, nombre, apellidos, posicion, valor):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.posicion = posicion
        self.valor = valor  # en millones de euros
        self.equipo = None  # referencia al equipo al que pertenece (None si está libre)
    
    def __str__(self):
        return f"ID: {self.id} | {self.nombre} {self.apellidos} | Posición: {self.posicion} | Valor: {self.valor}M€"

class Equipo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.presupuesto = 30  # 30 millones de euros iniciales
        self.jugadores = []  # lista de objetos jugador (máximo 10)
    
    def agregar_jugador(self, jugador):
        if len(self.jugadores) >= 10:
            return False, "El equipo ya tiene el máximo de 10 jugadores."
        
        if jugador.valor > self.presupuesto:
            return False, f"No hay suficiente presupuesto. Necesitas {jugador.valor}M€ y solo tienes {self.presupuesto}M€."
        
        if jugador.equipo is not None:
            return False, "El jugador ya pertenece a un equipo."
        
        self.jugadores.append(jugador)
        self.presupuesto -= jugador.valor
        jugador.equipo = self
        return True, "Jugador agregado con éxito."
    
    def vender_jugador(self, jugador):
        if jugador not in self.jugadores:
            return False, "Este jugador no pertenece a este equipo."
        
        self.jugadores.remove(jugador)
        self.presupuesto += jugador.valor
        jugador.equipo = None
        return True, "Jugador vendido con éxito."
    
    def generar_alineacion(self):
        # Verificar si hay al menos un jugador en cada posición
        posiciones = ["Portero", "Cierre", "Ala Derecha", "Ala Izquierda", "Pivot"]
        jugadores_por_posicion = {posicion: [] for posicion in posiciones}
        
        for jugador in self.jugadores:
            if jugador.posicion in jugadores_por_posicion:
                jugadores_por_posicion[jugador.posicion].append(jugador)
        
        # Verificar si todas las posiciones tienen al menos un jugador
        for posicion, jugadores in jugadores_por_posicion.items():
            if not jugadores:
                return None, f"No hay jugadores en la posición {posicion}."
        
        # Seleccionar al mejor jugador (mayor valor) de cada posición
        alineacion = []
        for posicion in posiciones:
            mejor_jugador = max(jugadores_por_posicion[posicion], key=lambda j: j.valor)
            alineacion.append(mejor_jugador)
        
        return alineacion, "Alineación generada con éxito."
    
    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | Jugadores: {len(self.jugadores)}/10 | Presupuesto: {self.presupuesto}M€"


class FantasyUFV:
    def __init__(self, jugadores_mercado):
        self.mercado = jugadores_mercado  # Lista de jugadores disponibles
        self.equipos = {}  # Diccionario de equipos {id: objeto_equipo}
        self.contador_equipos = 1  # Para asignar IDs a los equipos nuevos
    
    def crear_equipo(self, nombre):
        equipo = Equipo(self.contador_equipos, nombre)
        self.equipos[self.contador_equipos] = equipo
        self.contador_equipos += 1
        return equipo
    
    def obtener_jugadores_libres(self):
        return [j for j in self.mercado if j.equipo is None]

    def generar_equipo_automatico(self, equipo):
        # Verificar si el equipo ya tiene jugadores
        if equipo.jugadores:
            return False, "El equipo ya tiene jugadores. Solo se puede generar automáticamente para equipos vacíos."
        
        posiciones = ["Portero", "Cierre", "Ala Derecha", "Ala Izquierda", "Pivot"]
        jugadores_por_posicion = {posicion: [] for posicion in posiciones}
        
        # Clasificar jugadores libres por posición
        jugadores_libres = self.obtener_jugadores_libres()
        for jugador in jugadores_libres:
            if jugador.posicion in posiciones:
                jugadores_por_posicion[jugador.posicion].append(jugador)
        
        # Verificar que haya al menos un jugador libre para cada posición
        for posicion, jugadores in jugadores_por_posicion.items():
            if not jugadores:
                return False, f"No hay jugadores libres en la posición {posicion}."
        
        # Seleccionar un jugador aleatorio de cada posición primero
        for posicion in posiciones:
            random.shuffle(jugadores_por_posicion[posicion])
            for jugador in jugadores_por_posicion[posicion]:
                if jugador.valor <= equipo.presupuesto:
                    exito, mensaje = equipo.agregar_jugador(jugador)
                    if exito:
                        break
            else:
                return False, f"No hay jugadores asequibles para la posición {posicion}."
        
        # Añadir jugadores adicionales hasta llegar a 10 o quedarse sin presupuesto
        jugadores_libres = self.obtener_jugadores_libres()
        random.shuffle(jugadores_libres)
        
        while len(equipo.jugadores) < 10 and equipo.presupuesto > 0:
            for jugador in jugadores_libres:
                if jugador.valor <= equipo.presupuesto:
                    exito, _ = equipo.agregar_jugador(jugador)
                    if exito:
                        break
            else:
                break  # No se pudo añadir ningún jugador más
        
        return True, f"Equipo generado con {len(equipo.jugadores)} jugadores y {equipo.presupuesto}M€ restantes."

# --------------------- FUNCIONES DEL MENÚ ---------------------

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    print("\n" + "="*50)
    print(" "*15 + "FANTASY UFV - MENÚ PRINCIPAL")
    print("="*50)
    print("1. Gestión de Equipos")
    print("2. Mercado de Jugadores")
    print("3. Salir del programa")
    print("="*50)
    opcion = input("Seleccione una opción: ")
    return opcion

def mostrar_menu_equipos():
    print("\n" + "="*50)
    print(" "*15 + "GESTIÓN DE EQUIPOS")
    print("="*50)
    print("1. Mostrar equipos")
    print("2. Detalle equipo")
    print("3. Crear equipo")
    print("4. Generar equipo automáticamente")
    print("5. Mostrar alineación")
    print("6. Volver al menú principal")
    print("="*50)
    opcion = input("Seleccione una opción: ")
    return opcion

def mostrar_menu_mercado():
    print("\n" + "="*50)
    print(" "*15 + "MERCADO DE JUGADORES")
    print("="*50)
    print("1. Ver jugadores disponibles")
    print("2. Comprar jugador")
    print("3. Vender jugador")
    print("4. Volver al menú principal")
    print("="*50)
    opcion = input("Seleccione una opción: ")
    return opcion

def seleccionar_equipo(fantasy):
    if not fantasy.equipos:
        print("\nNo hay equipos creados.")
        time.sleep(2)
        return None
        
    print("\nEquipos disponibles:")
    for id_equipo, equipo in fantasy.equipos.items():
        print(f"{id_equipo}. {equipo}")
    
    while True:
        try:
            id_equipo = int(input("\nSeleccione el ID del equipo (0 para cancelar): "))
            if id_equipo == 0:
                return None
            if id_equipo in fantasy.equipos:
                return fantasy.equipos[id_equipo]
            print("ID de equipo no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def mostrar_jugadores_disponibles(fantasy):
    jugadores_libres = fantasy.obtener_jugadores_libres()
    
    if not jugadores_libres:
        print("\nNo hay jugadores disponibles en el mercado.")
        time.sleep(2)
        return
        
    print("\nJugadores disponibles en el mercado:")
    print("-" * 80)
    print(f"{'ID':<5} | {'Nombre':<15} | {'Apellidos':<20} | {'Posición':<15} | {'Valor':<10}")
    print("-" * 80)
    
    for jugador in jugadores_libres:
        print(f"{jugador.id:<5} | {jugador.nombre:<15} | {jugador.apellidos:<20} | {jugador.posicion:<15} | {jugador.valor:<10}M€")
    
    print("-" * 80)
    input("\nPresione Enter para continuar...")

def comprar_jugador(fantasy):
    equipo = seleccionar_equipo(fantasy)
    if not equipo:
        return
    
    print(f"\nEquipo seleccionado: {equipo.nombre}")
    print(f"Presupuesto disponible: {equipo.presupuesto}M€")
    print(f"Jugadores actuales ({len(equipo.jugadores)}/10):")
    
    if equipo.jugadores:
        for idx, j in enumerate(equipo.jugadores, 1):
            print(f"{idx}. {j}")
    else:
        print("El equipo no tiene jugadores.")
    
    # Mostrar jugadores disponibles
    jugadores_libres = fantasy.obtener_jugadores_libres()
    
    if not jugadores_libres:
        print("\nNo hay jugadores disponibles en el mercado.")
        time.sleep(2)
        return
        
    print("\nJugadores disponibles en el mercado:")
    print("-" * 80)
    print(f"{'ID':<5} | {'Nombre':<15} | {'Apellidos':<20} | {'Posición':<15} | {'Valor':<10}")
    print("-" * 80)
    
    for jugador in jugadores_libres:
        print(f"{jugador.id:<5} | {jugador.nombre:<15} | {jugador.apellidos:<20} | {jugador.posicion:<15} | {jugador.valor:<10}M€")
    
    print("-" * 80)
    
    while True:
        try:
            id_jugador = int(input("\nSeleccione el ID del jugador a comprar (0 para cancelar): "))
            if id_jugador == 0:
                return
                
            # Buscar jugador por ID
            jugador_seleccionado = None
            for jugador in jugadores_libres:
                if jugador.id == id_jugador:
                    jugador_seleccionado = jugador
                    break
            
            if jugador_seleccionado:
                exito, mensaje = equipo.agregar_jugador(jugador_seleccionado)
                print(mensaje)
                if exito:
                    print(f"{jugador_seleccionado.nombre} {jugador_seleccionado.apellidos} ha sido fichado por {equipo.nombre}.")
                time.sleep(2)
                return
            else:
                print("ID de jugador no válido o no está disponible.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def vender_jugador(fantasy):
    equipo = seleccionar_equipo(fantasy)
    if not equipo:
        return
    
    print(f"\nEquipo seleccionado: {equipo.nombre}")
    print(f"Presupuesto actual: {equipo.presupuesto}M€")
    
    if not equipo.jugadores:
        print("El equipo no tiene jugadores para vender.")
        time.sleep(2)
        return
        
    print("\nJugadores del equipo:")
    for idx, jugador in enumerate(equipo.jugadores, 1):
        print(f"{idx}. {jugador}")
    
    while True:
        try:
            idx = int(input("\nSeleccione el número del jugador a vender (0 para cancelar): "))
            if idx == 0:
                return
                
            if 1 <= idx <= len(equipo.jugadores):
                jugador = equipo.jugadores[idx - 1]
                exito, mensaje = equipo.vender_jugador(jugador)
                print(mensaje)
                if exito:
                    print(f"{jugador.nombre} {jugador.apellidos} ha sido vendido. Presupuesto actualizado: {equipo.presupuesto}M€")
                time.sleep(2)
                return
            else:
                print("Número de jugador no válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def mostrar_alineacion(fantasy):
    equipo = seleccionar_equipo(fantasy)
    if not equipo:
        return
    
    alineacion, mensaje = equipo.generar_alineacion()
    
    if not alineacion:
        print(mensaje)
        time.sleep(2)
        return
    
    print("\n" + "="*60)
    print(f"MEJOR ALINEACIÓN PARA {equipo.nombre}".center(60))
    print("="*60)
    
    # Mostrar la alineación de forma más visual
    print("\n" + " "*25 + "PORTERO")
    print(" "*25 + f"{alineacion[0].nombre} {alineacion[0].apellidos}")
    print(" "*25 + f"({alineacion[0].valor}M€)")
    
    print("\n" + " "*25 + "CIERRE")
    print(" "*25 + f"{alineacion[1].nombre} {alineacion[1].apellidos}")
    print(" "*25 + f"({alineacion[1].valor}M€)")
    
    print("\nALA IZQUIERDA" + " "*10 + "PIVOT" + " "*10 + "ALA DERECHA")
    print(f"{alineacion[3].nombre}" + " "*10 + f"{alineacion[4].nombre}" + " "*10 + f"{alineacion[2].nombre}")
    print(f"{alineacion[3].apellidos}" + " "*10 + f"{alineacion[4].apellidos}" + " "*10 + f"{alineacion[2].apellidos}")
    print(f"({alineacion[3].valor}M€)" + " "*10 + f"({alineacion[4].valor}M€)" + " "*10 + f"({alineacion[2].valor}M€)")
    
    print("\n" + "="*60)
    print(f"Valor total de la alineación: {sum(j.valor for j in alineacion)}M€")
    print("="*60)
    
    input("\nPresione Enter para continuar...")

def crear_jugadores_mercado():
    nombres = ["Juan", "Pedro", "Miguel", "Carlos", "Antonio", "Luis", "Javier", "David", 
               "Francisco", "José", "Daniel", "Manuel", "Alejandro", "Raúl", "Sergio", 
               "Alberto", "Mario", "Fernando", "Andrés", "Diego", "Rafael", "Rubén", 
               "Jorge", "Iván", "Pablo", "Roberto", "Óscar", "Guillermo", "Adrián", "Marcos"]
    
    apellidos = ["García", "Rodríguez", "González", "Fernández", "López", "Martínez", 
                "Sánchez", "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", 
                "Díaz", "Moreno", "Álvarez", "Romero", "Alonso", "Gutiérrez", "Navarro", 
                "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", 
                "Blanco", "Molina", "Morales", "Suárez", "Ortega", "Delgado", "Castro", "Ortiz"]
    
    posiciones = ["Portero", "Cierre", "Ala Derecha", "Ala Izquierda", "Pivot"]
    
    # Crear al menos 30 jugadores
    jugadores = []
    for i in range(1, 41):  # Crear 40 jugadores
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        posicion = random.choice(posiciones)
        
        # El valor depende de la posición
        if posicion == "Portero":
            valor = round(random.uniform(1, 7), 1)
        elif posicion == "Cierre":
            valor = round(random.uniform(2, 8), 1)
        else:  # Alas y Pivot suelen ser los más caros
            valor = round(random.uniform(3, 10), 1)
        
        jugadores.append(Jugador(i, nombre, apellido, posicion, valor))
    
    return jugadores

# --------------------- FUNCIÓN PRINCIPAL ---------------------

def modo_interactivo(fantasy):
    # Menú principal
    while True:
        limpiar_pantalla()
        opcion = mostrar_menu_principal()
        
        if opcion == "1":  # Gestión de Equipos
            gestion_equipos(fantasy)
        elif opcion == "2":  # Mercado de Jugadores
            gestion_mercado(fantasy)
        elif opcion == "3":  # Salir
            print("\n¡Gracias por jugar a FantasyUFV!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            time.sleep(1.5)

def modo_demostracion(fantasy):
    print("\n" + "="*50)
    print(" "*10 + "DEMOSTRACIÓN DE FANTASY UFV")
    print("="*50)
    
    # 1. Crear equipos de demostración
    print("\n1. Creando equipos de demostración...")
    equipo1 = fantasy.crear_equipo("Real Madrid Sala")
    equipo2 = fantasy.crear_equipo("Barça Futsal")
    print(f"Equipos creados: {equipo1.nombre} (ID: {equipo1.id}) y {equipo2.nombre} (ID: {equipo2.id})")
    
    # 2. Mostrar jugadores disponibles
    print("\n2. Jugadores disponibles en el mercado (primeros 5):")
    jugadores_libres = fantasy.obtener_jugadores_libres()
    print("-" * 80)
    print(f"{'ID':<5} | {'Nombre':<15} | {'Apellidos':<20} | {'Posición':<15} | {'Valor':<10}")
    print("-" * 80)
    
    for jugador in jugadores_libres[:5]:
        print(f"{jugador.id:<5} | {jugador.nombre:<15} | {jugador.apellidos:<20} | {jugador.posicion:<15} | {jugador.valor:<10}M€")
    print("-" * 80)
    
    # 3. Generar equipo automático
    print("\n3. Generando equipo automático para Real Madrid Sala...")
    exito, mensaje = fantasy.generar_equipo_automatico(equipo1)
    print(mensaje)
    
    # 4. Mostrar detalle del equipo generado
    print("\n4. Detalle del equipo Real Madrid Sala:")
    print(f"Presupuesto: {equipo1.presupuesto}M€")
    print(f"Jugadores ({len(equipo1.jugadores)}/10):")
    
    if equipo1.jugadores:
        print("\n" + "-" * 80)
        print(f"{'ID':<5} | {'Nombre':<15} | {'Apellidos':<20} | {'Posición':<15} | {'Valor':<10}")
        print("-" * 80)
        
        for jugador in equipo1.jugadores:
            print(f"{jugador.id:<5} | {jugador.nombre:<15} | {jugador.apellidos:<20} | {jugador.posicion:<15} | {jugador.valor:<10}M€")
        
        print("-" * 80)
    
    # 5. Comprar jugadores para el Barça Futsal
    print("\n5. Comprando jugadores para el Barça Futsal...")
    jugadores_a_comprar = []
    posiciones = ["Portero", "Cierre", "Ala Derecha", "Ala Izquierda", "Pivot"]
    
    # Buscar jugadores por posición
    for posicion in posiciones:
        for jugador in jugadores_libres:
            if jugador.posicion == posicion and jugador not in jugadores_a_comprar:
                jugadores_a_comprar.append(jugador)
                break
    
    # Comprar los jugadores
    for jugador in jugadores_a_comprar:
        exito, mensaje = equipo2.agregar_jugador(jugador)
        print(f"Compra de {jugador.nombre} {jugador.apellidos} ({jugador.posicion}): {mensaje}")
    
    print(f"\nBarça Futsal tiene ahora {len(equipo2.jugadores)} jugadores y {equipo2.presupuesto}M€ de presupuesto.")
    
    # 6. Mostrar alineación
    print("\n6. Mejor alineación para Real Madrid Sala:")
    alineacion, mensaje = equipo1.generar_alineacion()
    
    if alineacion:
        print("\n" + "="*60)
        print(f"MEJOR ALINEACIÓN PARA {equipo1.nombre}".center(60))
        print("="*60)
        
        # Mostrar la alineación de forma más visual
        print("\n" + " "*25 + "PORTERO")
        print(" "*25 + f"{alineacion[0].nombre} {alineacion[0].apellidos}")
        print(" "*25 + f"({alineacion[0].valor}M€)")
        
        print("\n" + " "*25 + "CIERRE")
        print(" "*25 + f"{alineacion[1].nombre} {alineacion[1].apellidos}")
        print(" "*25 + f"({alineacion[1].valor}M€)")
        
        print("\nALA IZQUIERDA" + " "*10 + "PIVOT" + " "*10 + "ALA DERECHA")
        print(f"{alineacion[3].nombre}" + " "*10 + f"{alineacion[4].nombre}" + " "*10 + f"{alineacion[2].nombre}")
        print(f"{alineacion[3].apellidos}" + " "*10 + f"{alineacion[4].apellidos}" + " "*10 + f"{alineacion[2].apellidos}")
        print(f"({alineacion[3].valor}M€)" + " "*10 + f"({alineacion[4].valor}M€)" + " "*10 + f"({alineacion[2].valor}M€)")
        
        print("\n" + "="*60)
        print(f"Valor total de la alineación: {sum(j.valor for j in alineacion)}M€")
        print("="*60)
    else:
        print(mensaje)
    
    # 7. Demostración de venta de jugadores
    if equipo1.jugadores:
        jugador_a_vender = equipo1.jugadores[0]
        print(f"\n7. Vendiendo a {jugador_a_vender.nombre} {jugador_a_vender.apellidos} del {equipo1.nombre}...")
        presupuesto_anterior = equipo1.presupuesto
        exito, mensaje = equipo1.vender_jugador(jugador_a_vender)
        print(mensaje)
        if exito:
            print(f"Presupuesto anterior: {presupuesto_anterior}M€")
            print(f"Presupuesto actual: {equipo1.presupuesto}M€ (ganancia de {jugador_a_vender.valor}M€)")
    
    print("\n" + "="*50)
    print(" "*10 + "FIN DE LA DEMOSTRACIÓN")
    print("="*50)
    print("\nPara acceder al modo interactivo, ejecute el programa con el flag --interactive")

def main():
    # Inicializar el juego con jugadores para el mercado
    jugadores_mercado = crear_jugadores_mercado()
    fantasy = FantasyUFV(jugadores_mercado)
    
    # Comprobar si se usa el modo interactivo
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        modo_interactivo(fantasy)
    else:
        modo_demostracion(fantasy)

def gestion_equipos(fantasy):
    while True:
        limpiar_pantalla()
        opcion = mostrar_menu_equipos()
        
        if opcion == "1":  # Mostrar equipos
            if fantasy.equipos:
                print("\nEquipos disponibles:")
                for id_equipo, equipo in fantasy.equipos.items():
                    print(equipo)
            else:
                print("\nNo hay equipos creados.")
            input("\nPresione Enter para continuar...")
            
        elif opcion == "2":  # Detalle equipo
            equipo = seleccionar_equipo(fantasy)
            if equipo:
                print(f"\nDetalle del equipo: {equipo.nombre}")
                print(f"Presupuesto: {equipo.presupuesto}M€")
                print(f"Jugadores ({len(equipo.jugadores)}/10):")
                
                if equipo.jugadores:
                    print("\n" + "-" * 80)
                    print(f"{'ID':<5} | {'Nombre':<15} | {'Apellidos':<20} | {'Posición':<15} | {'Valor':<10}")
                    print("-" * 80)
                    
                    for jugador in equipo.jugadores:
                        print(f"{jugador.id:<5} | {jugador.nombre:<15} | {jugador.apellidos:<20} | {jugador.posicion:<15} | {jugador.valor:<10}M€")
                    
                    print("-" * 80)
                else:
                    print("El equipo no tiene jugadores.")
                
                input("\nPresione Enter para continuar...")
                
        elif opcion == "3":  # Crear equipo
            nombre = input("\nIngrese el nombre del nuevo equipo: ")
            if nombre.strip():
                equipo = fantasy.crear_equipo(nombre)
                print(f"\nEquipo '{nombre}' creado con éxito. ID: {equipo.id}")
            else:
                print("\nDebe ingresar un nombre válido.")
            time.sleep(2)
            
        elif opcion == "4":  # Generar equipo automáticamente
            equipo = seleccionar_equipo(fantasy)
            if equipo:
                exito, mensaje = fantasy.generar_equipo_automatico(equipo)
                print(mensaje)
                time.sleep(2)
                
        elif opcion == "5":  # Mostrar alineación
            mostrar_alineacion(fantasy)
            
        elif opcion == "6":  # Volver al menú principal
            return
            
        else:
            print("\nOpción no válida. Intente de nuevo.")
            time.sleep(1.5)

def gestion_mercado(fantasy):
    while True:
        limpiar_pantalla()
        opcion = mostrar_menu_mercado()
        
        if opcion == "1":  # Ver jugadores disponibles
            mostrar_jugadores_disponibles(fantasy)
            
        elif opcion == "2":  # Comprar jugador
            comprar_jugador(fantasy)
            
        elif opcion == "3":  # Vender jugador
            vender_jugador(fantasy)
            
        elif opcion == "4":  # Volver al menú principal
            return
            
        else:
            print("\nOpción no válida. Intente de nuevo.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()