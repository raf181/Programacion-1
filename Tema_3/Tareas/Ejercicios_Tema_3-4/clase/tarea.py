# Diccionario de alumnos
alumnos = {
    "12345678": {
        "Nombre": "Ramón",
        "Apellidos": "Pérez Gómez",
        "Asignaturas": None
    },
    "87654321": {
        "Nombre": "María",
        "Apellidos": "García López",
        "Asignaturas": None
    }
}

# Diccionario de asignaturas
asignaturas = {
    "Programación I": {
        "ECTS": 6.0,
        "Curso": 1,
        "Cuatrimestre": 2
    },
    "Matemáticas": {
        "ECTS": 6.0,
        "Curso": 1,
        "Cuatrimestre": 1
    }
}

# Añadir asignaturas a cada alumno y establecer nota predeterminada a 10.0
for dni, alumno in alumnos.items():
    alumno["Asignaturas"] = {}
    for asig_nombre, asig_info in asignaturas.items():
        alumno["Asignaturas"][asig_nombre] = asig_info.copy()
        alumno["Asignaturas"][asig_nombre]["Nota"] = 10.0

# Cambiar notas a 5.0 para alumnos con último dígito del DNI impar en primer cuatrimestre
for dni, alumno in alumnos.items():
    if int(dni[-1]) % 2 != 0:  # Comprobar si el último dígito es impar
        for asig_nombre, asig_info in alumno["Asignaturas"].items():
            if asignaturas[asig_nombre]["Cuatrimestre"] == 1:
                alumno["Asignaturas"][asig_nombre]["Nota"] = 5.0

# Mostrar alumnos con notas de 10.0
print("Alumnos con notas de 10.0:")
for dni, alumno in alumnos.items():
    for asig_nombre, asig_info in alumno["Asignaturas"].items():
        if asig_info["Nota"] == 10.0:
            print(f"Alumno: {alumno['Nombre']} {alumno['Apellidos']}")
            print(f"Asignatura: {asig_nombre}")
            print(f"Nota: {asig_info['Nota']}")
            print("-" * 30)


print(alumnos)