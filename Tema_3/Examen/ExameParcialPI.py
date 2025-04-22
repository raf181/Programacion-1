print("--------------------- Ejercico 1 --------------------")
#1. (1,25 puntos) Crea una función llamada GestionarDatos que reciba tres parámetros, el primero de ellos debe ser una estructura 
# de datos avanzada (debe funcionar para todas las que hemos visto en clase), el segundo un tipo de datos a tu elección y el 
# tercero será un booleano que por defecto tendrá el valor verdadero. 
#   - Si el parámetro 3 es verdadero deberá insertar el parametro 2 dentro del primer parámetro. 
#   - Si el parámetro 3 es falso deberá buscar si el parámetro 2 está en el primer parámetro y deberá elminarla.
# En todos los casos devolverá la estructura avanzada resultante. 
# Incluir las llamadas con las diferentes estructuras de datos para ver el resultado. 
# Función para manejar datos con listas, conjuntos y diccionarios
def GestionarDatos(estructura_datos, dato, bool_valor=True):
    if isinstance(estructura_datos, list):
        if bool_valor:
            estructura_datos.append(dato)
        else:
            if dato in estructura_datos:
                estructura_datos.remove(dato)
        return estructura_datos
    
    elif isinstance(estructura_datos, tuple):
        lista_temporal = list(estructura_datos)  # tupla a una lista 
        if bool_valor:
            lista_temporal.append(dato)
        else:
            if dato in lista_temporal:
                lista_temporal.remove(dato)
        return tuple(lista_temporal)
    
    elif isinstance(estructura_datos, dict):
        if bool_valor:
            estructura_datos[dato] = None  # None para no tener que pasr tambien valor
        else:
            if dato in estructura_datos:
                del estructura_datos[dato]
        return estructura_datos
    
    else:
        raise ValueError("Tipo de estructura de datos no soportada")

# Ejemplos de uso con diferentes estructuras de datos

# Lista
lista = [1, 2, 3]
# Insertar 4 en la lista
print(GestionarDatos(lista, 4))  
# Eliminar 2 de la lista
print(GestionarDatos(lista, 2, False))  

# Tupla
tupla = (1, 2, 3)

print(GestionarDatos(tupla, 4))  
# Eliminar 2 de la lista temporal creada al convertir atupla
print(GestionarDatos(tupla, 2, False))  

# Diccionario
diccionario = {1: 'a', 2: 'b'}
# Insertar clave 3 en el diccionario
print(GestionarDatos(diccionario, 3)) 
# Eliminar clave 2 del diccionario 
print(GestionarDatos(diccionario, 2, False))   
    

#2. (2,25 puntos) Crea la función GenerarAlumnos que recibirá la siguiente lista de alumnos:
# 
# Nombre, Appellidos, DNI, Curso

print("--------------------- Ejercico 2 --------------------")
alumnos = [["Alejandro", "Gómez Fernández", "12345677Z", 1],["María", "López García", "23456789X", 2],["Carlos", "Pérez Martínez", "34567890T", 3],
           ["Laura", "Rodríguez Sánchez", "45678901R", 4],["David", "Fernández Gómez", "56789012W", 1],["Ana", "García López", "67890123Q", 2],
           ["Javier", "Sánchez Pérez", "78901234V", 1],["Sofía", "Martínez Rodríguez", "89012345N", 1],["Pablo", "Díaz Hernández", "90123456M", 1],
           ["Lucía", "Moreno Jiménez", "01234567L", 2],["Hugo", "Álvarez Ruiz", "12345098K", 2],["Martina", "Muñoz Torres", "23456109J", 4],
           ["Daniel", "Romero Flores", "34567210H", 1],["Valeria", "Navarro Ortega", "45678321G", 2],["Adrián", "Gutiérrez Castro", "56789432F", 3],
           ["Clara", "Molina Delgado", "67890543D", 4],["Diego", "Castillo Ortiz", "78901654C", 1],["Elena", "Vázquez Marín", "89012765B", 2],
           ["Fernando", "Ramos Iglesias", "90124876A", 3],["Isabel", "Herrera Reyes", "01234987Z", 4],["Rubén", "Aguilar Santos", "12345098Y", 1],
           ["Natalia", "Gómez Cruz", "23456109X", 2],["Andrés", "Vega Prieto", "34567210W", 3],["Eva", "Jiménez Núñez", "45678321T", 4],
           ["Sergio", "León Gómez", "56789432R", 1]]

# las siguientes asignaturas (donde cada elemento es un curso):
asignaturas = (("Programación I", "HCP", "Fundamentos de Derecho", "Matemáticas Aplicadas"), 
               ("Programación II", "Fundamentos de Bases de Datos", "Fuentes de Datos", "Arquitectura de Sistemas y Datos"), 
               ("Fundamentos de Redes", "Inteligencia Artificial", "Seguridad en Bases de Datos", "Introducción al Gobierno de la Ciberseguridad"), 
               ("Gestión de Proyectos", "Seguridad en Redes", "Prácticas Profesionales", "Trabajo Fin de Grado"))  
#  y también recibirá un curso que por defecto será None. 
# La función deberá devolver un diccionario con la siguiente estructura: 
#  {
#        "12345678Z": {
#            "nombre": "Alejandro", 
#            "apellido1": "Gómez", 
#            "apellido2": "Fernández", 
#            "matricula": {
#                               "curso": 1, 
#                               "asignaturas": ["Programación I", "HCP", "Fundamentos de Derecho", "Matemáticas Aplicadas"] #asignaturas de su curso
#                       }
#        }, 
#        "23456789X": {
#               ...
#        }
#  }
# 
# Si el parámetro curso es None deberá rellenar el diccionario con todos los alumnos, si viene un número sólo incluirá en el diccionario 
# exclusivamente a los alumnos de ese curso. 

# Función para generar el grupo por curso
def GenerarAlumnos(alumnos, asignaturas):
    grupo_por_curso = {}
    
    for alumno in alumnos:
        curso = alumno[3]
        
        if curso not in grupo_por_curso:
            grupo_por_curso[curso] = []
        
        #asignaturas para el curso actual
        asignaturaCurso = [asignatura[curso-1] for i, asignatura in enumerate(asignaturas)] # enumerate para recorrer la lista de asignaturas, po las tuplas
        
        alumnoDict = {
            "Nombre": alumno[0],
            "Apellidos": alumno[1],
            "DNI": alumno[2],
            "Asignaturas": asignaturaCurso
        }
        
        grupo_por_curso[curso].append(alumnoDict)
    
    return grupo_por_curso

print("--------------------- Ejercico 3 --------------------")
#3. (2,5 puntos) Hacer un función que reciba el diccionario resultante del punto 2 y deberá hacer lo siguiente: 
# - Para cada curso, mostrar que alumnos (nombre y apellidos) están a modo listado de clase.
# - Para cada asignatura mostrar los alumnos que la tengan, a modo listado de clase.
# - Mostrar cuántos alumnos hay por curso. 
# - Mostrar para cuántos alumnos la suma de las cifras del DNI es impar y cuántos par. 

# Funcion de imprimir los resultados bonitos, de Ejercicios_Tema_3-4 entarea.py, editada para esto y sin los colores de la funcion original
n_alum_cur = 0 # No me da tiempo a toda la logica perdi demasiado en el 2

def print_bonito(select_diccionario):
    for clave, valor in select_diccionario.items():
        if isinstance(valor, (dict, list, tuple)):
            print(f"Curso:'{clave}' con {n_alum_cur}:")
            if isinstance(valor, dict):
                items = list(valor.items())
                for i, (subclave, subvalor) in enumerate(items):
                    branch = "└─" if i == len(items) - 1 else "├─"
                    print(f"  {branch} {subclave}: {subvalor}")
            else:
                for i, item in enumerate(valor):
                    branch = "└─" if i == len(valor) - 1 else "├─"
                    print(f"  {branch} {item}")
        else:
            print(f"Curso:'{clave}' → {valor}")

grupo_por_curso = GenerarAlumnos(alumnos, asignaturas)
print_bonito(grupo_por_curso)