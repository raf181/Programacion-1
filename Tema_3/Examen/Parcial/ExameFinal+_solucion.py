import random

class Menu:
    def __init__(self, primero, segundo, postre, precio):
        self.id = random.randint(1, 1000)
        self.primero = primero
        self.segundo = segundo
        self.postre = postre
        self.precio = precio
    
    def GetPrecio(self):
        return self.precio - (self.precio * 0.2)

class MenuGenerator:
    def __init__(self, platos):
        self.platos = platos
        self.historico = {}
    
    def AddPlato(self, nombre, precio, alergenos, tipo):
        if nombre in self.platos:
            raise Exception(f"El plato {nombre} ya existe en la lista de platos.")
        
        self.platos[nombre] = {
            "precio": precio,
            "alergenos": alergenos,
            "tipo": tipo
        }
    
    def GetPlatos(self, tipo, alergeno):
        platos_filtrados = []
        
        for nombre, info in self.platos.items():
            # Verificamos si el plato es del tipo solicitado o de tipo "ambos"
            es_tipo_valido = info["tipo"] == tipo or info["tipo"] == "ambos"
            
            # Verificamos que el plato no contenga el alérgeno indicado
            no_tiene_alergeno = alergeno not in info["alergenos"]
            
            if es_tipo_valido and no_tiene_alergeno:
                platos_filtrados.append(nombre)
                
        return platos_filtrados
    
    def GetPrecioPlato(self, plato):
        if plato in self.platos:
            return self.platos[plato]["precio"]
        return 0
    
    def GenerarMenu(self, alergeno=None):
        # Obtener platos del primer tipo sin el alérgeno
        primeros = self.GetPlatos("primero", alergeno if alergeno else "")
        # También consideramos platos de tipo "ambos" como posibles primeros platos
        primeros_ambos = self.GetPlatos("ambos", alergeno if alergeno else "")
        primeros.extend(primeros_ambos)
        
        # Obtener platos del segundo tipo sin el alérgeno
        segundos = self.GetPlatos("segundo", alergeno if alergeno else "")
        # También consideramos platos de tipo "ambos" como posibles segundos platos
        segundos_ambos = self.GetPlatos("ambos", alergeno if alergeno else "")
        segundos.extend(segundos_ambos)
        
        # Obtener postres sin el alérgeno
        postres = self.GetPlatos("postre", alergeno if alergeno else "")
        
        # Seleccionar un plato aleatorio de cada tipo
        if not primeros or not segundos or not postres:
            raise Exception("No hay suficientes platos disponibles para generar un menú.")
        
        primero_seleccionado = random.choice(primeros)
        
        # Asegurarnos de que el segundo no es igual al primero
        segundos_disponibles = [s for s in segundos if s != primero_seleccionado]
        if not segundos_disponibles:
            # Si no hay segundos diferentes al primero, tomamos uno de los segundos originales
            segundo_seleccionado = random.choice(segundos)
        else:
            segundo_seleccionado = random.choice(segundos_disponibles)
            
        postre_seleccionado = random.choice(postres)
        
        # Calcular el precio total
        precio_total = (
            self.GetPrecioPlato(primero_seleccionado) + 
            self.GetPrecioPlato(segundo_seleccionado) + 
            self.GetPrecioPlato(postre_seleccionado)
        )
        
        # Crear el menú
        menu = Menu(primero_seleccionado, segundo_seleccionado, postre_seleccionado, precio_total)
        
        # Añadir el menú al histórico
        self.historico[menu.id] = menu
        
        return menu

class Camarero:
    def __init__(self, nombre, generador_menus):
        self.nombre = nombre
        self.generador_menus = generador_menus
        
        # Generar el ID con las tres primeras iniciales en mayúscula y un número aleatorio
        iniciales = ''.join([palabra[0] for palabra in nombre.split()[:3]]).upper()
        if len(iniciales) < 3:
            iniciales = iniciales.ljust(3, 'X')  # Rellenar con 'X' si es necesario
        self.id = iniciales + str(random.randint(1000, 9999))
        
        self.ventas = []
    
    def ProponerMenu(self, alergeno=None):
        return self.generador_menus.GenerarMenu(alergeno)
    
    def TomarPedido(self, menu):
        # Determinar el ID incremental
        nuevo_id = len(self.ventas) + 1
        
        # Añadir el pedido a las ventas
        pedido = {
            "id": nuevo_id,
            "menu": menu,
            "cobrado": False
        }
        
        self.ventas.append(pedido)
        return pedido
    
    def CobrarPedido(self, id_pedido):
        for pedido in self.ventas:
            if pedido["id"] == id_pedido:
                pedido["cobrado"] = True
                return
                
        # Si llegamos aquí, el pedido no existe
        raise Exception(f"El pedido con id {id_pedido} no existe.")

class Turno:
    def __init__(self, lista_camareros, fecha, hora_inicio, hora_fin):
        self.lista_camareros = lista_camareros
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    
    def MostrarVentas(self):
        total_ventas = 0
        
        for camarero in self.lista_camareros:
            for pedido in camarero.ventas:
                if pedido["cobrado"]:
                    total_ventas += pedido["menu"].GetPrecio()
        
        print(f"Total de ventas del turno: {total_ventas:.2f} €")
        return total_ventas
    
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
                    
            # Si llegamos aquí, el camarero no existe
            print(f"No se encontró un camarero con ID {id_camarero}.")
            return 0
        else:
            # Mostrar ventas de todos los camareros
            for camarero in self.lista_camareros:
                total_ventas = 0
                
                for pedido in camarero.ventas:
                    if pedido["cobrado"]:
                        total_ventas += pedido["menu"].GetPrecio()
                
                print(f"Total de ventas del camarero {camarero.nombre} ({camarero.id}): {total_ventas:.2f} €")
            
            return None

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un generador de menús con la lista de platos
    generador = MenuGenerator(platos)
    
    # Crear camareros
    camarero1 = Camarero("Juan Pérez", generador)
    camarero2 = Camarero("María López", generador)
    
    # Proponer menús y tomar pedidos
    menu1 = camarero1.ProponerMenu("lácteos")
    camarero1.TomarPedido(menu1)
    
    menu2 = camarero2.ProponerMenu("huevo")
    camarero2.TomarPedido(menu2)
    
    # Cobrar pedidos
    camarero1.CobrarPedido(1)
    
    # Crear un turno
    turno = Turno([camarero1, camarero2], "2025-05-16", "14:00", "22:00")
    
    # Mostrar ventas
    print("Ventas totales del turno:")
    turno.MostrarVentas()
    
    print("\nVentas por camarero:")
    turno.MostrarVentasPorCamarero()
