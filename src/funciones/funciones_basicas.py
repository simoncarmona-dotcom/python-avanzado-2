"""
Módulo de Funciones Básicas en Python
=====================================
Este módulo contiene ejercicios prácticos sobre la definición y uso de
funciones, incluyendo: parámetros posicionales, parámetros con nombre,
valores por defecto, retorno múltiple y scope de variables.

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones
"""

# =============================================================================
# EJERCICIO 1: Funciones con docstrings completas
# Buenas prácticas de documentación de funciones
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: Funciones con docstrings")
print("=" * 60)


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    El área se calcula usando la fórmula: A = π × r²

    Args:
        radio (float): El radio del círculo. Debe ser un número positivo.

    Returns:
        float: El área del círculo.

    Raises:
        ValueError: Si el radio es negativo.

    Examples:
        >>> calcular_area_circulo(5)
        78.53981633974483
        >>> calcular_area_circulo(0)
        0.0
    """
    import math

    if radio < 0:
        raise ValueError("El radio no puede ser negativo")

    return math.pi * radio ** 2


def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo (base × altura).
    """
    return base * altura


# Usamos las funciones y mostramos sus docstrings
area_c = calcular_area_circulo(5)
print(f"Área del círculo (radio=5): {area_c:.2f}")

area_r = calcular_area_rectangulo(10, 5)
print(f"Área del rectángulo (10×5): {area_r:.2f}")

# Accedemos al docstring de una función con __doc__
print(f"\nDocstring de calcular_area_circulo:")
print(f"  {calcular_area_circulo.__doc__[:80]}...")
print()


# =============================================================================
# EJERCICIO 2: Parámetros posicionales y con nombre (keyword arguments)
# Diferentes formas de pasar argumentos a una función
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: Parámetros posicionales y con nombre")
print("=" * 60)


def crear_perfil(nombre, edad, ciudad, profesion="Estudiante"):
    """
    Crea un diccionario con el perfil de un usuario.

    Args:
        nombre (str): Nombre completo del usuario.
        edad (int): Edad del usuario.
        ciudad (str): Ciudad de residencia.
        profesion (str, optional): Profesión del usuario.
            Por defecto es "Estudiante".

    Returns:
        dict: Diccionario con los datos del perfil.
    """
    return {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
        "profesion": profesion
    }


# Llamada con argumentos posicionales (por orden)
perfil1 = crear_perfil("Simón", 20, "Bogotá")
print(f"Perfil 1 (posicional): {perfil1}")

# Llamada con argumentos por nombre (keyword) - el orden no importa
perfil2 = crear_perfil(ciudad="Medellín", nombre="Ana", edad=25, profesion="Ingeniera")
print(f"Perfil 2 (keyword):    {perfil2}")

# Mezcla de posicionales y con nombre
# Los posicionales SIEMPRE deben ir antes de los keyword
perfil3 = crear_perfil("Carlos", 30, ciudad="Cali")
print(f"Perfil 3 (mixto):      {perfil3}")

print()


# =============================================================================
# EJERCICIO 3: Funciones con valores por defecto
# Parámetros opcionales que tienen un valor predefinido
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: Valores por defecto")
print("=" * 60)


def formatear_precio(precio, moneda="COP", decimales=2, con_simbolo=True):
    """
    Formatea un precio numérico como string legible.

    Args:
        precio (float): El valor numérico del precio.
        moneda (str, optional): Código de la moneda. Default: "COP".
        decimales (int, optional): Cantidad de decimales. Default: 2.
        con_simbolo (bool, optional): Si incluir el símbolo $. Default: True.

    Returns:
        str: El precio formateado como cadena de texto.
    """
    simbolo = "$" if con_simbolo else ""
    precio_formateado = f"{precio:,.{decimales}f}"
    return f"{simbolo}{precio_formateado} {moneda}"


# Usando solo el parámetro obligatorio (los demás toman valores por defecto)
print(formatear_precio(1500000))

# Cambiando solo la moneda
print(formatear_precio(99.99, moneda="USD"))

# Sin decimales y sin símbolo
print(formatear_precio(250000, decimales=0, con_simbolo=False))

# Cambiando todos los valores por defecto
print(formatear_precio(1234.5, moneda="EUR", decimales=1, con_simbolo=True))

print()


def saludar(nombre, saludo="Hola", despedida=False):
    """
    Genera un mensaje de saludo o despedida personalizado.

    Args:
        nombre (str): Nombre de la persona.
        saludo (str, optional): Palabra de saludo. Default: "Hola".
        despedida (bool, optional): Si es despedida. Default: False.

    Returns:
        str: Mensaje generado.
    """
    if despedida:
        return f"¡Adiós, {nombre}! Fue un gusto."
    return f"¡{saludo}, {nombre}! Bienvenido/a."


print(saludar("Simón"))
print(saludar("Ana", saludo="Buenos días"))
print(saludar("Carlos", despedida=True))

print()


# =============================================================================
# EJERCICIO 4: Funciones con retorno múltiple
# Python permite retornar varios valores usando tuplas
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: Retorno múltiple")
print("=" * 60)


def calcular_estadisticas(numeros):
    """
    Calcula estadísticas básicas de una lista de números.

    Args:
        numeros (list): Lista de números para analizar.

    Returns:
        tuple: Tupla con (minimo, maximo, promedio, suma, cantidad).
            - minimo (float): Valor mínimo de la lista.
            - maximo (float): Valor máximo de la lista.
            - promedio (float): Promedio aritmético.
            - suma (float): Suma total de los valores.
            - cantidad (int): Cantidad de elementos.
    """
    if not numeros:
        return 0, 0, 0, 0, 0

    minimo = min(numeros)
    maximo = max(numeros)
    suma = sum(numeros)
    cantidad = len(numeros)
    promedio = suma / cantidad

    # Retornamos múltiples valores separados por coma
    # Python los empaqueta automáticamente como una tupla
    return minimo, maximo, promedio, suma, cantidad


# Desempaquetamos los valores retornados en variables individuales
datos = [85, 92, 78, 95, 88, 70, 93, 81]
minimo, maximo, promedio, suma, cantidad = calcular_estadisticas(datos)

print(f"Datos: {datos}")
print(f"  Mínimo:   {minimo}")
print(f"  Máximo:   {maximo}")
print(f"  Promedio:  {promedio:.2f}")
print(f"  Suma:      {suma}")
print(f"  Cantidad:  {cantidad}")

print()


def dividir(dividendo, divisor):
    """
    Realiza una división y retorna cociente y residuo.

    Args:
        dividendo (int): El número a dividir.
        divisor (int): El número por el cual dividir.

    Returns:
        tuple: (cociente, residuo) o (None, None) si el divisor es 0.
    """
    if divisor == 0:
        print("  [!] Error: no se puede dividir por cero")
        return None, None

    cociente = dividendo // divisor
    residuo = dividendo % divisor
    return cociente, residuo


cociente, residuo = dividir(17, 5)
print(f"17 ÷ 5 = {cociente} con residuo {residuo}")

cociente, residuo = dividir(100, 0)

print()


# =============================================================================
# EJERCICIO 5: Scope de variables (local vs global)
# Ámbito de visibilidad de las variables
# =============================================================================

print("=" * 60)
print("EJERCICIO 5: Scope de variables (local vs global)")
print("=" * 60)

# Variable global: definida fuera de cualquier función
mensaje_global = "Soy una variable global"
contador_global = 0


def demostrar_scope_local():
    """
    Demuestra que las variables locales solo existen dentro de la función.
    """
    # Esta variable 'mensaje_local' solo existe dentro de esta función
    mensaje_local = "Soy una variable local"
    print(f"  Dentro de la función: {mensaje_local}")
    # Podemos LEER la variable global
    print(f"  Leyendo variable global: {mensaje_global}")


demostrar_scope_local()

# Intentar acceder a la variable local desde fuera causaría error:
# print(mensaje_local)  # NameError: name 'mensaje_local' is not defined

print()


def modificar_global():
    """
    Demuestra el uso de la palabra clave 'global' para modificar
    una variable global desde dentro de una función.
    """
    global contador_global  # Declaramos que vamos a usar la variable global
    contador_global += 1
    print(f"  Contador global dentro de función: {contador_global}")


print(f"Contador global antes: {contador_global}")
modificar_global()
modificar_global()
modificar_global()
print(f"Contador global después: {contador_global}")

print()


# Demostración de shadowing (sombreado de variables)
x = 100  # Variable global


def demostrar_shadowing():
    """
    Demuestra que una variable local puede 'ocultar' una variable global
    del mismo nombre (shadowing).
    """
    x = 50  # Variable LOCAL que "oculta" la global
    print(f"  x dentro de la función (local): {x}")


print(f"x fuera de la función (global): {x}")
demostrar_shadowing()
print(f"x fuera de la función (no cambió): {x}")

print()

print("=" * 60)
print("Fin del módulo de funciones básicas")
print("=" * 60)
