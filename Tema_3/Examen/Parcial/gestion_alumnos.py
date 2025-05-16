# Configuración dinámica de cursos y asignaturas
CONFIGURACION_CURSOS = {
    1: {
        "nombre": "Primer curso",
        "asignaturas": ["Matemáticas I", "Física I", "Programación I"]
    },
    2: {
        "nombre": "Segundo curso",
        "asignaturas": ["Matemáticas II", "Física II", "Programación II"]
    },
    3: {
        "nombre": "Tercer curso",
        "asignaturas": ["Inteligencia Artificial", "Bases de Datos", "Redes"]
    },
    4: {
        "nombre": "Cuarto curso",
        "asignaturas": ["Gestión de Proyectos", "Seguridad", "Trabajo Fin de Grado"]
    }
}

print("Configuración de cursos:")
print(CONFIGURACION_CURSOS)

# Función para generar el diccionario de alumnos
def GenerarAlumnos(alumnos, asignaturas, curso=None):
    """
    Genera un diccionario con la información de los alumnos.
    
    Args:
        alumnos: Lista de listas con la información de los alumnos
        asignaturas: Tupla de tuplas con las asignaturas por curso
        curso: Curso específico a filtrar (None para todos los cursos)
    
    Returns:
        Diccionario con la información de los alumnos
    """
    resultado = {}
    
    for alumno in alumnos:
        nombre, apellidos, dni, curso_alumno = alumno
        
        # Dividir los apellidos en apellido1 y apellido2
        apellidos_split = apellidos.split()
        apellido1 = apellidos_split[0]
        apellido2 = " ".join(apellidos_split[1:]) if len(apellidos_split) > 1 else ""
        
        # Si se especifica un curso, filtrar solo los alumnos de ese curso
        if curso is not None and curso_alumno != curso:
            continue
        
        # Obtener las asignaturas del curso del alumno
        asignaturas_alumno = asignaturas[curso_alumno - 1]
        
        # Crear la estructura del alumno
        resultado[dni] = {
            "nombre": nombre,
            "apellido1": apellido1,
            "apellido2": apellido2,
            "matricula": {
                "curso": curso_alumno,
                "asignaturas": list(asignaturas_alumno)
            }
        }
    
    return resultado

# Función para analizar y mostrar información sobre los alumnos
def AnalizarAlumnos(diccionario_alumnos):
    """
    Analiza y muestra información sobre los alumnos.
    
    Args:
        diccionario_alumnos: Diccionario con la información de los alumnos
    """
    # Crear diccionarios para almacenar la información
    alumnos_por_curso = {}
    alumnos_por_asignatura = {}
    
    # Inicializar contadores para DNI par/impar
    dni_par = 0
    dni_impar = 0
    
    # Procesar cada alumno
    for dni, info in diccionario_alumnos.items():
        nombre = info["nombre"]
        apellido1 = info["apellido1"]
        apellido2 = info["apellido2"]
        curso = info["matricula"]["curso"]
        asignaturas = info["matricula"]["asignaturas"]
        
        # Comprobar si la suma de cifras del DNI es par o impar
        suma_dni = sum(int(digit) for digit in dni if digit.isdigit())
        if suma_dni % 2 == 0:
            dni_par += 1
        else:
            dni_impar += 1
        
        # Añadir alumno a su curso
        if curso not in alumnos_por_curso:
            alumnos_por_curso[curso] = []
        alumnos_por_curso[curso].append(f"{nombre} {apellido1} {apellido2}")
        
        # Añadir alumno a sus asignaturas
        for asignatura in asignaturas:
            if asignatura not in alumnos_por_asignatura:
                alumnos_por_asignatura[asignatura] = []
            alumnos_por_asignatura[asignatura].append(f"{nombre} {apellido1} {apellido2}")
    
    # Mostrar listados de alumnos por curso
    print("\n=== LISTADOS DE ALUMNOS POR CURSO ===")
    for curso in sorted(alumnos_por_curso.keys()):
        print(f"\nCurso {curso}:")
        for i, alumno in enumerate(sorted(alumnos_por_curso[curso]), 1):
            print(f"  {i}. {alumno}")
    
    # Mostrar listados de alumnos por asignatura
    print("\n=== LISTADOS DE ALUMNOS POR ASIGNATURA ===")
    for asignatura in sorted(alumnos_por_asignatura.keys()):
        print(f"\nAsignatura: {asignatura}")
        for i, alumno in enumerate(sorted(alumnos_por_asignatura[asignatura]), 1):
            print(f"  {i}. {alumno}")
    
    # Mostrar número de alumnos por curso
    print("\n=== NÚMERO DE ALUMNOS POR CURSO ===")
    for curso in sorted(alumnos_por_curso.keys()):
        print(f"Curso {curso}: {len(alumnos_por_curso[curso])} alumnos")
    
    # Mostrar número de alumnos con DNI par/impar
    print("\n=== ANÁLISIS DE DNI ===")
    print(f"Alumnos con suma de cifras del DNI par: {dni_par}")
    print(f"Alumnos con suma de cifras del DNI impar: {dni_impar}")

# Datos de ejemplo
alumnos = [["Alejandro", "Gómez Fernández", "12345677Z", 1],["María", "López García", "23456789X", 2],["Carlos", "Pérez Martínez", "34567890T", 3],
           ["Laura", "Rodríguez Sánchez", "45678901R", 4],["David", "Fernández Gómez", "56789012W", 1],["Ana", "García López", "67890123Q", 2],
           ["Javier", "Sánchez Pérez", "78901234V", 1],["Sofía", "Martínez Rodríguez", "89012345N", 1],["Pablo", "Díaz Hernández", "90123456M", 1],
           ["Lucía", "Moreno Jiménez", "01234567L", 2],["Hugo", "Álvarez Ruiz", "12345098K", 2],["Martina", "Muñoz Torres", "23456109J", 4],
           ["Daniel", "Romero Flores", "34567210H", 1],["Valeria", "Navarro Ortega", "45678321G", 2],["Adrián", "Gutiérrez Castro", "56789432F", 3],
           ["Clara", "Molina Delgado", "67890543D", 4],["Diego", "Castillo Ortiz", "78901654C", 1],["Elena", "Vázquez Marín", "89012765B", 2],
           ["Fernando", "Ramos Iglesias", "90124876A", 3],["Isabel", "Herrera Reyes", "01234987Z", 4],["Rubén", "Aguilar Santos", "12345098Y", 1],
           ["Natalia", "Gómez Cruz", "23456109X", 2],["Andrés", "Vega Prieto", "34567210W", 3],["Eva", "Jiménez Núñez", "45678321T", 4],
           ["Sergio", "León Gómez", "56789432R", 1]]

asignaturas = (("Programación I", "HCP", "Fundamentos de Derecho", "Matemáticas Aplicadas"), 
               ("Programación II", "Fundamentos de Bases de Datos", "Fuentes de Datos", "Arquitectura de Sistemas y Datos"), 
               ("Fundamentos de Redes", "Inteligencia Artificial", "Seguridad en Bases de Datos", "Introducción al Gobierno de la Ciberseguridad"), 
               ("Gestión de Proyectos", "Seguridad en Redes", "Prácticas Profesionales", "Trabajo Fin de Grado"))

# Ejemplo de uso con todos los alumnos
print("\n=== EJEMPLO 1: Todos los alumnos ===")
resultado_todos = GenerarAlumnos(alumnos, asignaturas)
print(f"Total de alumnos: {len(resultado_todos)}")
print("Muestra del primer alumno:")
primer_dni = list(resultado_todos.keys())[0]
print(f"{primer_dni}: {resultado_todos[primer_dni]}")

# Ejemplo de uso filtrando por curso 1
print("\n=== EJEMPLO 2: Alumnos de curso 1 ===")
resultado_curso1 = GenerarAlumnos(alumnos, asignaturas, curso=1)
print(f"Total de alumnos de curso 1: {len(resultado_curso1)}")
print("Lista de DNIs de alumnos de curso 1:")
print(list(resultado_curso1.keys()))

# Análisis de alumnos
print("\n=== ANÁLISIS DE TODOS LOS ALUMNOS ===")
AnalizarAlumnos(resultado_todos)
