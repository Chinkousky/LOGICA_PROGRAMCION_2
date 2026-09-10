from datetime import datetime


def calcular_edad(fecha_nacimiento_str):
    # Convierte el texto ingresado a un objeto de fecha (Año-Mes-Día)
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")
    fecha_actual = datetime.now()

    # Resta los años de forma directa
    edad = fecha_actual.year - fecha_nacimiento.year

    # Resta un año si el mes o día actual es menor al de nacimiento
    ya_cumplio_anios = (fecha_actual.month, fecha_actual.day) >= (
        fecha_nacimiento.month,
        fecha_nacimiento.day,
    )

    if not ya_cumplio_anios:
        edad -= 1

    return edad