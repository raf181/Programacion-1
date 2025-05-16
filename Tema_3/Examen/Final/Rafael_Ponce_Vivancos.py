

# --- imports --- #
import random #para elegir un plato aleatorio de la lista

platos = {
    "Ensalada César": {
        "precio": 6.5,
        "alergenos": ["huevo", "lacteos", "gluten"],
        "tipo": "primero"
    },
    "Gazpacho andaluz": {
        "precio": 5.0,
        "alergenos": [],
        "tipo": "primero"
    },
    "Crema de calabacín": {
        "precio": 5.5,
        "alergenos": ["lacteos"],
        "tipo": "primero"
    },
    "Arroz con verduras": {
        "precio": 7.0,
        "alergenos": [],
        "tipo": "primero"
    },
    "Huevos rellenos": {
        "precio": 6.0,
        "alergenos": ["huevo", "lacteos"],
        "tipo": "primero"
    },
    "Ensalada de pasta": {
        "precio": 6.8,
        "alergenos": ["gluten"],
        "tipo": "primero"
    },
    "Entrecot de ternera": {
        "precio": 12.5,
        "alergenos": [],
        "tipo": "segundo"
    },
    "Salmon al horno": {
        "precio": 11.0,
        "alergenos": ["pescado"],
        "tipo": "segundo"
    },
    "Pollo al curry": {
        "precio": 9.5,
        "alergenos": ["lacteos"],
        "tipo": "segundo"
    },
    "Lentejas estofadas": {
        "precio": 8.0,
        "alergenos": [],
        "tipo": "segundo"
    },
    "Bacalao con tomate": {
        "precio": 10.5,
        "alergenos": ["pescado"],
        "tipo": "segundo"
    },
    "Filete de merluza": {
        "precio": 9.8,
        "alergenos": ["pescado", "gluten"],
        "tipo": "segundo"
    },
    "Tortilla española": {
        "precio": 7.0,
        "alergenos": ["huevo"],
        "tipo": "ambos"
    },
    "Croquetas de jamon": {
        "precio": 6.5,
        "alergenos": ["gluten", "lacteos"],
        "tipo": "ambos"
    },
    "Pasta boloñesa": {
        "precio": 8.0,
        "alergenos": ["gluten"],
        "tipo": "ambos"
    },
    "Risotto de setas": {
        "precio": 9.0,
        "alergenos": ["lacteos"],
        "tipo": "ambos"
    },
    "Flan de huevo": {
        "precio": 3.5,
        "alergenos": ["huevo", "lacteos"],
        "tipo": "postre"
    },
    "Tarta de queso": {
        "precio": 4.0,
        "alergenos": ["gluten", "lacteos", "huevo"],
        "tipo": "postre"
    },
    "Fruta del tiempo": {
        "precio": 2.5,
        "alergenos": [],
        "tipo": "postre"
    },
    "Helado de vainilla": {
        "precio": 3.0,
        "alergenos": ["lacteos"],
        "tipo": "postre"
    },
    "Arroz con leche": {
        "precio": 3.2,
        "alergenos": ["lacteos"],
        "tipo": "postre"
    }
}

# Estas desarrollando un prototipo de software que permita a la cadena de restaurantes FastMenu ser mas 
# eficientes en su gestion. Para ello, pondras al servicio de los camareros un generador de menus que les 
# permita, obtener un menu con los platos disponibles, teniendo en cuenta posibles alergias. 
# Para ello deberas implementar en Python las siguientes clases: 

# 1. (0,5 puntos) Crear la clase Menu: 
#   - Atributos: id, primero, segundo, postre, precio
#   - Métodos:
#       - Constructor: recibira los datos del menu, ademas definira un atributo id que sera un numero
#         aleatorio entre 1 y 1000.
#       - GetPrecio: no recibira nada y devolvera el precio del menu menos el 20%class Menu:
class Menu:
    def __init__(self, primero, segundo, postre, precio):
        self.id = random.randint(1, 1000)
        self.primero = primero
        self.segundo = segundo
        self.postre = postre
        self.precio = precio
    
    def GetPrecio(self):
        return self.precio - (self.precio * 0.2)

#2. (2,5 puntos) Crear la clase MenuGenerator:
#   - Atributos: platos, historico      
#   - Métodos:
#       - Constructor: recibira una lista de platos. Definira un atributo historico que sera un diccionario 
#       vacío.
class MenuGenerator:
    def __init__(self, platos):
        self.platos = platos
        self.historico = {}

#       - AddPlato: recibira los datos de un plato (nombre, precio, alérgenos y tipo) y lo añadira a 
#       la lista de platos siempre que no exista ya en la lista. Si existe debera lanzar una excepcion.
    def AddPlato(self, nombre, precio, alergenos, tipo):
        if nombre in self.platos:
            raise Exception(f"El plato {nombre} ya existe en la lista de platos")
        
        self.platos[nombre] = {
            "precio": precio,
            "alergenos": alergenos,
            "tipo": tipo
        }
#       - GetPlatos: recibira el tipo y una alergeno y devolvera una lista de platos segun que sean del 
#       tipo pedido o de tipo "ambos" y ademas que no tenga entre su lista de alérgenos el alérgeno
#       pasado como parametro.
    def GetPlatos(self, tipo, alergeno):
        platos_filtrados = []
    
        # Verificamos si el plato es del tipo que se le da y sin los alergenos
        for nombre, info in self.platos.items():
            es_tipo_valido = info["tipo"] == tipo or info["tipo"] == "ambos"
            
            no_tiene_alergeno = alergeno not in info["alergenos"]
            if es_tipo_valido and no_tiene_alergeno:
                platos_filtrados.append(nombre)

        return platos_filtrados
    
#       - GetPrecioPlato: recibira un plato y devolvera el precio de ese plato.
    def GetPrecioPlato(self, plato):
        if plato in self.platos:
            return self.platos[plato]["precio"]
        return 0

#       - GenerarMenu: podra recibir un alérgeno y devolvera un menu aleatorio con un plato de cada tipo 
#       (un objeto de tipo Menu). Ademas debera añadir el menu al historico.
    def GenerarMenu(self, alergeno=None):
        # Crear lista de Primeros - aler
        primeros = self.GetPlatos("primero", alergeno if alergeno else "")
        primeros_ambos = self.GetPlatos("ambos", alergeno if alergeno else "")
        primeros.extend(primeros_ambos) # sumar ambas lstas de platos validos como primeros
        
        # Crear lista de Segundos - aler
        segundos = self.GetPlatos("segundo", alergeno if alergeno else "")
        segundos_ambos = self.GetPlatos("ambos", alergeno if alergeno else "")
        segundos.extend(segundos_ambos) # sumar ambas lstas de platos validos como primeros
        
        # Postre - aler
        postres = self.GetPlatos("postre", alergeno if alergeno else "") 

        # Por si no hay lista con suficientes tipos (extra)
        if not primeros or not segundos or not postres:
            raise Exception("No hay suficientes platos disponibles para generar un menu")
        
        # Selec Primero de la lista de Primeros - aler
        primero_seleccionado = random.choice(primeros)

        # Selec Primero de la lista de Seguro - aler - Primero select 
        segundos_disponibles = [s for s in segundos if s != primero_seleccionado] # segundos - primero selec
        if not segundos_disponibles:
            segundo_seleccionado = random.choice(segundos)
        else:
            segundo_seleccionado = random.choice(segundos_disponibles)
        postre_seleccionado = random.choice(postres)
        
        precio_total = (self.GetPrecioPlato(primero_seleccionado) + self.GetPrecioPlato(segundo_seleccionado) + self.GetPrecioPlato(postre_seleccionado))
        menu = Menu(primero_seleccionado, segundo_seleccionado, postre_seleccionado, precio_total)
        self.historico[menu.id] = menu 
        return menu

#3. (1,5 puntos) Crear la clase Camarero:
#   - Atributos: nombre, generador_menus, id, ventas.
#   - Métodos:
#       - Constructor: recibira el nombre del camarero y un objeto de tipo MenuGenerator y definira un 
#         atributo id del camarero que se generara con las tres primeras iniciales del nombre en mayusculas 
#         y un numero aleatorio entre 1000 y 9999. Ademas definira un atributo llamado ventas que sera una 
#         lista vacía.
class Camarero:
    def __init__(self, nombre, generador_menus):
        self.nombre = nombre
        self.generador_menus = generador_menus
        
        # Generar el ID 
        iniciales = ''.join([palabra[0] for palabra in nombre.split()[:3]]).upper()
        if len(iniciales) < 3:
            iniciales = iniciales.ljust(3, 'X')  # 'X' si es necesario
        self.id = iniciales + str(random.randint(1000, 9999))
        self.ventas = []

#       - ProponerMenu: podra recibir un alergeno y devolvera un menu aleatorio usando el objeto MenuGenerator.
    def ProponerMenu(self, alergeno=None):
        return self.generador_menus.GenerarMenu(alergeno)

#       - TomarPedido: recibira un objeto Menu y lo añadira a la lista de ventas del camarero con el siguiente 
#         formato:
#         { "id": NUMERO_INCREMENTAL, "menu": OBJETO_MENU, "cobrado": False }
    def TomarPedido(self, menu):
        nuevo_id = len(self.ventas) + 1
        
        pedido = {
            "id": nuevo_id,
            "menu": menu,
            "cobrado": False
        }
        
        self.ventas.append(pedido)
        return pedido

#       - CobrarPedido: recibira un id de pedido y lo marcara como cobrado (True). Si no existe el pedido 
#         debera lanzar una excepcion.
    def CobrarPedido(self, id_pedido):
        for pedido in self.ventas:
            if pedido["id"] == id_pedido:
                pedido["cobrado"] = True
                return
        raise Exception(f"El pedido {id_pedido} no esta en la lista de ventas")


#4 (1,5 punto) Crear la clase Turno:
#   - Atributos: lista_camareros, fecha, hora_inicio, hora_fin
#   - Métodos:
#       - Constructor: recibira una lista de camareros, la fecha y la hora de inicio y fin del turno.
class Turno:
    def __init__(self, lista_camareros, fecha, hora_inicio, hora_fin):
        self.lista_camareros = lista_camareros
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

#       - MostrarVentas: no recibira nada y mostrara el total del precio de los menus cobrados por todos
#         los camareros del turno.
    def MostrarVentas(self):
        total_ventas = 0
        for camarero in self.lista_camareros:
            for pedido in camarero.ventas:
                if pedido["cobrado"]:
                    total_ventas += pedido["menu"].GetPrecio()
        print(f"Total de ventas del turno: {total_ventas:.2f} €")
        return total_ventas

#       - MostrarVentasPorCamarero: podra recibir un id de camarero y devolvera el total del precio de 
#         los menus cobrados por ese camarero. Si no recibe id de camarero, mostrara por pantalla el total 
#         de los menus cobrados por cada uno de los camareros del turno.
    def MostrarVentasPorCamarero(self, id_camarero=None):
        if id_camarero:
            # Mostrar ventas de un camarero específico
            for camarero in self.lista_camareros:
                if camarero.id == id_camarero:
                    total_ventas = 0
                    for pedido in camarero.ventas:
                        if pedido["cobrado"]:
                            total_ventas += pedido["menu"].GetPrecio()
                    print(f"Total de ventas del camarero {camarero.nombre} ({camarero.id}): {total_ventas:.2f} €")
                    return total_ventas
            print(f"No se encontro un camarero con ID {id_camarero}")
            return 0
        
        else: # Mostrar ventas de todos los camareros si no se le da id_camarero
            for camarero in self.lista_camareros:
                total_ventas = 0
                for pedido in camarero.ventas:
                    if pedido["cobrado"]:
                        total_ventas += pedido["menu"].GetPrecio()
                print(f"Total de ventas del camarero {camarero.nombre} ({camarero.id}): {total_ventas:.2f} €")
            return None

# ------------------------------- = Test = -------------------------------
if __name__ == "__main__":
    generador = MenuGenerator(platos)
    
    camarero1 = Camarero("Juan Pérez", generador)
    camarero2 = Camarero("María López", generador)
    
    # Proponer menús y tomar pedidos
    print("Generando menú 1 (sin lácteos)...")
    menu1 = camarero1.ProponerMenu("lácteos")
    print(f"Menú 1: Primero={menu1.primero}, Segundo={menu1.segundo}, Postre={menu1.postre}, Precio original={menu1.precio}€, Precio con descuento={menu1.GetPrecio()}€")
    pedido1 = camarero1.TomarPedido(menu1)
    print(f"Pedido registrado con ID: {pedido1['id']}")
    
    print("\nGenerando menú 2 (sin huevo)...")
    menu2 = camarero2.ProponerMenu("huevo")
    pedido2 = camarero2.TomarPedido(menu2)
    print(f"Pedido registrado con ID: {pedido2['id']}")
    
    camarero1.CobrarPedido(1)
    
    turno = Turno([camarero1, camarero2], "2025-05-16", "14:00", "22:00")
    
    print("\nVentas totales del turno:")
    turno.MostrarVentas()
    
    print("\nVentas por camarero:")
    turno.MostrarVentasPorCamarero()