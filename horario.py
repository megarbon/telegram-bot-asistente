from asignaturas import cliente_asignatura, servidor_asignatura, movil_asignatura

# Diccionario de días de la semana con asignaturas
dias_semana = {
    "lunes": [cliente_asignatura, servidor_asignatura, movil_asignatura],
    "martes": [movil_asignatura, servidor_asignatura],
    "miércoles": [cliente_asignatura, servidor_asignatura],
    # ... asigna las asignaturas a cada día de la semana
}

# Obtener el día de la semana ingresado por el usuario
dia = input("Ingrese un día de la semana: ")

# Buscar las asignaturas correspondientes al día ingresado
asignaturas_del_dia = dias_semana.get(dia.lower())

# Imprimir las asignaturas del día ingresado
if asignaturas_del_dia:
    print(f"Asignaturas del {dia.capitalize()}:")
    for asignatura in asignaturas_del_dia:
        print(f"Nombre: {asignatura.nombre}")
        print(f"Profesor: {asignatura.profesor}")
        print(f"Correo: {asignatura.correo}")
        print()
else:
    print("No se encontraron asignaturas para el día ingresado.")