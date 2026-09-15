"""
Módulo de Match/Case (Structural Pattern Matching) en Python
============================================================
Este módulo demuestra la estructura match/case introducida en Python 3.10,
que permite hacer coincidencia de patrones de forma elegante y legible,
similar al switch/case de otros lenguajes pero más poderosa.

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones

Nota: Requiere Python 3.10 o superior para ejecutarse.
"""

# =============================================================================
# EJERCICIO 1: Match/case básico - Menú de opciones
# Similar a un switch/case tradicional
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: Match/case básico - Menú de opciones")
print("=" * 60)

# Simulamos la opción seleccionada por el usuario
opcion = 2

# La estructura match evalúa el valor de 'opcion'
# y ejecuta el bloque del case que coincida
match opcion:
    case 1:
        print("Seleccionaste: Ver perfil")
    case 2:
        print("Seleccionaste: Editar configuración")
    case 3:
        print("Seleccionaste: Ver historial")
    case 4:
        print("Seleccionaste: Cerrar sesión")
    case _:
        # El guion bajo '_' es el caso por defecto (wildcard)
        # Se ejecuta cuando ningún otro case coincide
        print(f"Opción {opcion} no válida")

print()


# =============================================================================
# EJERCICIO 2: Match/case con strings
# Sistema de respuesta según el día de la semana
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: Match/case con strings - Días de la semana")
print("=" * 60)

dia = "martes"

match dia.lower():
    case "lunes":
        print(f"{dia.capitalize()}: Inicio de semana laboral")
        tipo_dia = "laborable"
    case "martes" | "miercoles" | "jueves":
        # El operador '|' permite agrupar múltiples patrones
        # Es equivalente a un OR entre los cases
        print(f"{dia.capitalize()}: Día laboral regular")
        tipo_dia = "laborable"
    case "viernes":
        print(f"{dia.capitalize()}: ¡Último día laboral!")
        tipo_dia = "laborable"
    case "sabado" | "domingo":
        print(f"{dia.capitalize()}: Fin de semana")
        tipo_dia = "fin de semana"
    case _:
        print(f"'{dia}' no es un día válido")
        tipo_dia = "desconocido"

print(f"Tipo de día: {tipo_dia}")
print()


# =============================================================================
# EJERCICIO 3: Match/case con patrones de tuplas
# Procesamiento de coordenadas 2D
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: Match/case con patrones de tuplas")
print("=" * 60)

# Lista de puntos para analizar su ubicación en el plano cartesiano
puntos = [(0, 0), (3, 5), (-2, 4), (7, 0), (0, -3), (-1, -1)]

for punto in puntos:
    # Match puede descomponer (destructurar) una tupla en sus componentes
    match punto:
        case (0, 0):
            ubicacion = "Origen"
        case (x, 0):
            # 'x' captura el valor de la primera posición
            ubicacion = f"Eje X (x={x})"
        case (0, y):
            # 'y' captura el valor de la segunda posición
            ubicacion = f"Eje Y (y={y})"
        case (x, y) if x > 0 and y > 0:
            # Se puede agregar una condición (guard) con 'if'
            ubicacion = f"Cuadrante I (x={x}, y={y})"
        case (x, y) if x < 0 and y > 0:
            ubicacion = f"Cuadrante II (x={x}, y={y})"
        case (x, y) if x < 0 and y < 0:
            ubicacion = f"Cuadrante III (x={x}, y={y})"
        case (x, y):
            ubicacion = f"Cuadrante IV (x={x}, y={y})"

    print(f"  Punto {punto} -> {ubicacion}")

print()


# =============================================================================
# EJERCICIO 4: Match/case con diccionarios
# Procesamiento de comandos de un chatbot
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: Match/case con diccionarios - Chatbot")
print("=" * 60)

# Simulamos comandos que recibe un chatbot
comandos = [
    {"accion": "saludo", "nombre": "Simón"},
    {"accion": "consulta", "tema": "horarios"},
    {"accion": "compra", "producto": "laptop", "cantidad": 2},
    {"accion": "despedida"},
    {"accion": "desconocido"},
]

for comando in comandos:
    # Match puede hacer coincidencia parcial con diccionarios
    match comando:
        case {"accion": "saludo", "nombre": nombre}:
            # Extrae el valor de 'nombre' del diccionario
            print(f"  Bot: ¡Hola, {nombre}! ¿En qué puedo ayudarte?")
        case {"accion": "consulta", "tema": tema}:
            print(f"  Bot: Buscando información sobre '{tema}'...")
        case {"accion": "compra", "producto": prod, "cantidad": cant}:
            print(f"  Bot: Procesando compra de {cant} unidad(es) de '{prod}'")
        case {"accion": "despedida"}:
            print(f"  Bot: ¡Hasta luego! Fue un placer ayudarte.")
        case _:
            print(f"  Bot: No entiendo ese comando: {comando}")

print()


# =============================================================================
# EJERCICIO 5: Match/case con tipos de datos
# Función que procesa diferentes tipos de entrada
# =============================================================================

print("=" * 60)
print("EJERCICIO 5: Match/case con tipos de datos")
print("=" * 60)


def procesar_dato(dato):
    """
    Procesa un dato según su tipo usando match/case.

    Args:
        dato: Cualquier valor de Python a procesar.

    Returns:
        str: Descripción del procesamiento realizado.
    """
    match dato:
        case int(n) if n > 0:
            return f"Entero positivo: {n} -> cuadrado = {n**2}"
        case int(n) if n < 0:
            return f"Entero negativo: {n} -> valor absoluto = {abs(n)}"
        case int(n):
            return f"Entero cero"
        case float(n):
            return f"Flotante: {n} -> redondeado = {round(n, 2)}"
        case str(s) if len(s) > 0:
            return f"Cadena: '{s}' -> mayúsculas = '{s.upper()}'"
        case str():
            return "Cadena vacía"
        case list(items):
            return f"Lista con {len(items)} elementos: {items}"
        case _:
            return f"Tipo no reconocido: {type(dato).__name__}"


# Probamos con diferentes tipos de datos
datos_prueba = [42, -7, 0, 3.14159, "python", "", [1, 2, 3], True]

for dato in datos_prueba:
    resultado = procesar_dato(dato)
    print(f"  {resultado}")

print()

print("=" * 60)
print("Fin del módulo de match/case")
print("=" * 60)
