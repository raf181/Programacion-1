# Configuración dinámica de cursos y asignaturas
CONFIGURACION_CURSOS = {
    1: {
        "nombre": "Primer curso",
        "asignaturas": ["Matemáticas I", "Física I", "Programación I"]
# En todos los casos devolverá la estructura avanzada resultante. 
# Incluir las llamadas con las diferentes estructuras de datos para ver el resultado. 


#2. (2,25 puntos) Crea la función GenerarAlumnos que recibirá la siguiente lista de alumnos: 
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



#3. (2,5 puntos) Hacer un función que reciba el diccionario resultante del punto 2 y deberá hacer lo siguiente: 
# - Para cada curso, mostrar que alumnos (nombre y apellidos) están a modo listado de clase.
# - Para cada asignatura mostrar los alumnos que la tengan, a modo listado de clase.
# - Mostrar cuántos alumnos hay por curso. 
# - Mostrar para cuántos alumnos la suma de las cifras del DNI es impar y cuántos par. 

def GestionarDatos(estructura, elemento, insertar=True):
    if isinstance(estructura, (list, set)):
        if insertar:
            if isinstance(estructura, list):
                estructura.append(elemento)
            else:
                estructura.add(elemento)
        else:
            if elemento in estructura:
                if isinstance(estructura, list):
                    estructura.remove(elemento)
                else:
                    estructura.remove(elemento)
    elif isinstance(estructura, dict):
        if insertar:
            if isinstance(elemento, tuple) and len(elemento) == 2:
                estructura[elemento[0]] = elemento[1]
        else:
            if elemento in estructura:
                del estructura[elemento]
    elif isinstance(estructura, tuple):
        if insertar:
            estructura = estructura + (elemento,)
        else:
            temp = list(estructura)
            if elemento in temp:
                temp.remove(elemento)
            estructura = tuple(temp)
    return estructura

# Ejemplos de uso
print("Pruebas de GestionarDatos:")
# Lista
mi_lista = [1, 2, 3]
print("Lista original:", mi_lista)
mi_lista = GestionarDatos(mi_lista, 4)  # Añadir
print("Después de añadir 4:", mi_lista)
mi_lista = GestionarDatos(mi_lista, 4, False)  # Eliminar
print("Después de eliminar 4:", mi_lista)

# Conjunto
mi_conjunto = {1, 2, 3}
print("\nConjunto original:", mi_conjunto)
mi_conjunto = GestionarDatos(mi_conjunto, 4)  # Añadir
print("Después de añadir 4:", mi_conjunto)
mi_conjunto = GestionarDatos(mi_conjunto, 4, False)  # Eliminar
print("Después de eliminar 4:", mi_conjunto)

# Diccionario
mi_dict = {"a": 1, "b": 2}
print("\nDiccionario original:", mi_dict)
mi_dict = GestionarDatos(mi_dict, ("c", 3))  # Añadir
print("Después de añadir c:3:", mi_dict)
mi_dict = GestionarDatos(mi_dict, "c", False)  # Eliminar
print("Después de eliminar c:", mi_dict)

# Tupla
mi_tupla = (1, 2, 3)
print("\nTupla original:", mi_tupla)
mi_tupla = GestionarDatos(mi_tupla, 4)  # Añadir
print("Después de añadir 4:", mi_tupla)
mi_tupla = GestionarDatos(mi_tupla, 4, False)  # Eliminar
print("Después de eliminar 4:", mi_tupla)



def GenerarAlumnos(alumnos, asignaturas, curso=None):
    resultado = {}
    
    for alumno in alumnos:
        nombre, apellidos, dni, curso_alumno = alumno
        apellido1, apellido2 = apellidos.split()[0], apellidos.split()[1]
        
        # Si se especifica un curso y el alumno no está en ese curso, continuamos
        if curso is not None and curso_alumno != curso:
            continue
            
        # Obtener las asignaturas del curso del alumno
        asignaturas_curso = asignaturas[curso_alumno - 1]
        
        # Crear el diccionario para el alumno
        resultado[dni] = {
            "nombre": nombre,
            "apellido1": apellido1,
            "apellido2": apellido2,
            "matricula": {
                "curso": curso_alumno,
                "asignaturas": list(asignaturas_curso)
            }
        }
    
    return resultado

def ProcesarInformacionAlumnos(diccionario_alumnos):
    # 1. Mostrar alumnos por curso
    print("=== Listado de alumnos por curso ===")
    for curso in range(1, 5):
        print(f"\nCurso {curso}:")
        alumnos_curso = [f"{datos['nombre']} {datos['apellido1']} {datos['apellido2']}" 
                        for datos in diccionario_alumnos.values() 
                        if datos['matricula']['curso'] == curso]
        for alumno in sorted(alumnos_curso):
            print(f"- {alumno}")
    
    # 2. Mostrar alumnos por asignatura
    print("\n=== Listado de alumnos por asignatura ===")
    asignaturas_dict = {}
    for dni, datos in diccionario_alumnos.items():
        for asignatura in datos['matricula']['asignaturas']:
            if asignatura not in asignaturas_dict:
                asignaturas_dict[asignatura] = []
            asignaturas_dict[asignatura].append(
                f"{datos['nombre']} {datos['apellido1']} {datos['apellido2']}")
    
    for asignatura, alumnos in sorted(asignaturas_dict.items()):
        print(f"\n{asignatura}:")
        for alumno in sorted(alumnos):
            print(f"- {alumno}")
    
    # 3. Mostrar cantidad de alumnos por curso
    print("\n=== Cantidad de alumnos por curso ===")
    conteo_curso = {}
    for datos in diccionario_alumnos.values():
        curso = datos['matricula']['curso']
        conteo_curso[curso] = conteo_curso.get(curso, 0) + 1
    
    for curso in sorted(conteo_curso.keys()):
        print(f"Curso {curso}: {conteo_curso[curso]} alumnos")
    
    # 4. Contar DNIs con suma de cifras par/impar
    print("\n=== Análisis de DNIs ===")
    pares = impares = 0
    for dni in diccionario_alumnos.keys():
        # Sumamos solo los dígitos del DNI
        suma = sum(int(d) for d in dni if d.isdigit())
        if suma % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f"DNIs con suma par: {pares}")
    print(f"DNIs con suma impar: {impares}")

# Ejemplo de uso de las funciones
if __name__ == "__main__":
    # Generar el diccionario de todos los alumnos
    diccionario_completo = GenerarAlumnos(alumnos, asignaturas)
    print("\nProcesando información de todos los alumnos:")
    ProcesarInformacionAlumnos(diccionario_completo)
    
    # Ejemplo con un curso específico
    print("\nProcesando información de alumnos de primer curso:")
    diccionario_curso1 = GenerarAlumnos(alumnos, asignaturas, curso=1)
    ProcesarInformacionAlumnos(diccionario_curso1)