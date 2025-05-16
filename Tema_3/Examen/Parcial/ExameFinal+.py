# Estás desarrollando un prototipo de software que permita a la cadena de restaurantes FastMenu ser más 
# eficientes en su gestión. Para ello, pondrás al servicio de los camareros un generador de menús que les 
# permita, obtener un menú con los platos disponibles, teniendo en cuenta posibles alergias. 
# Para ello deberás implementar en Python las siguientes clases: 

# 1. (0,5 puntos) Crear la clase Menu: 
#   - Atributos: id, primero, segundo, postre, precio
#   - Métodos:
#       - Constructor: recibirá los datos del menú, además definirá un atributo id que será un número
#         aleatorio entre 1 y 1000.
#       - GetPrecio: no recibirá nada y devolverá el precio del menú menos el 20%

#2. (2,5 puntos) Crear la clase MenuGenerator:
#   - Atributos: platos, historico      
#   - Métodos:
#       - Constructor: recibirá una lista de platos. Definirá un atributo historico que será un diccionario 
#       vacío.
#       - AddPlato: recibirá los datos de un plato (nombre, precio, alérgenos y tipo) y lo añadirá a 
#       la lista de platos siempre que no exista ya en la lista. Si existe deberá lanzar una excepción.
#       - GetPlatos: recibirá el tipo y una alergeno y devolverá una lista de platos según que sean del 
#       tipo pedido o de tipo "ambos" (primero y segundo) y además que no tenga entre su lista de alérgenos el alérgeno
#       pasado como parámetro.
#       - GetPrecioPlato: recibirá un plato y devolverá el precio de ese plato.
#       - GenerarMenu: podrá recibir un alérgeno y devolverá un menú aleatorio con un plato de cada tipo (primer, segundo y postre {Primero y segudo no pueden seriguales})
#       (un objeto de tipo Menu). Además deberá añadir el menú al histórico.

#3. (1,5 puntos) Crear la clase Camarero:
#   - Atributos: nombre, generador_menus, id, ventas.
#   - Métodos:
#       - Constructor: recibirá el nombre del camarero y un objeto de tipo MenuGenerator y definirá un 
#         atributo id del camarero que se generará con las tres primeras iniciales del nombre en mayúsculas 
#         y un numero aleatorio entre 1000 y 9999. Además definirá un atributo llamado ventas que será una 
#         lista vacía.         
#       - ProponerMenu: podrá recibir un alérgeno y devolverá un menú aleatorio usando el objeto MenuGenerator.
#       - TomarPedido: recibirá un objeto Menu y lo añadirá a la lista de ventas del camarero con el siguiente 
#         formato:
#         { "id": NUMERO_INCREMENTAL, "menu": OBJETO_MENU, "cobrado": False }
#       - CobrarPedido: recibirá un id de pedido y lo marcará como cobrado (True). Si no existe el pedido 
#         deberá lanzar una excepción.

#4 (1,5 punto) Crear la clase Turno:
#   - Atributos: lista_camareros, fecha, hora_inicio, hora_fin
#   - Métodos:
#       - Constructor: recibirá una lista de camareros, la fecha y la hora de inicio y fin del turno.   
#       - MostrarVentas: no recibirá nada y mostrará el total del precio de los menús cobrados por todos
#         los camareros del turno.
#       - MostrarVentasPorCamarero: podrá recibir un id de camarero y devolverá el total del precio de 
#         los menús cobrados por ese camarero. Si no recibe id de camarero, mostrará por pantalla el total 
#         de los menús cobrados por cada uno de los camareros del turno.



platos = {
    "Ensalada César": {
        "precio": 6.5,
        "alergenos": ["huevo", "lácteos", "gluten"],
        "tipo": "primero"
    },
    "Gazpacho andaluz": {
        "precio": 5.0,
        "alergenos": [],
        "tipo": "primero"
    },
    "Crema de calabacín": {
        "precio": 5.5,
        "alergenos": ["lácteos"],
        "tipo": "primero"
    },
    "Arroz con verduras": {
        "precio": 7.0,
        "alergenos": [],
        "tipo": "primero"
    },
    "Huevos rellenos": {
        "precio": 6.0,
        "alergenos": ["huevo", "lácteos"],
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
    "Salmón al horno": {
        "precio": 11.0,
        "alergenos": ["pescado"],
        "tipo": "segundo"
    },
    "Pollo al curry": {
        "precio": 9.5,
        "alergenos": ["lácteos"],
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
    "Croquetas de jamón": {
        "precio": 6.5,
        "alergenos": ["gluten", "lácteos"],
        "tipo": "ambos"
    },
    "Pasta boloñesa": {
        "precio": 8.0,
        "alergenos": ["gluten"],
        "tipo": "ambos"
    },
    "Risotto de setas": {
        "precio": 9.0,
        "alergenos": ["lácteos"],
        "tipo": "ambos"
    },
    "Flan de huevo": {
        "precio": 3.5,
        "alergenos": ["huevo", "lácteos"],
        "tipo": "postre"
    },
    "Tarta de queso": {
        "precio": 4.0,
        "alergenos": ["gluten", "lácteos", "huevo"],
        "tipo": "postre"
    },
    "Fruta del tiempo": {
        "precio": 2.5,
        "alergenos": [],
        "tipo": "postre"
    },
    "Helado de vainilla": {
        "precio": 3.0,
        "alergenos": ["lácteos"],
        "tipo": "postre"
    },
    "Arroz con leche": {
        "precio": 3.2,
        "alergenos": ["lácteos"],
        "tipo": "postre"
    }
}

