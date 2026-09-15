"""
Módulo de Funciones Avanzadas en Python
=======================================
Este módulo contiene ejercicios sobre conceptos avanzados de funciones:
*args, **kwargs, funciones lambda, funciones como parámetros (higher-order),
y las funciones built-in map(), filter() y reduce().

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones
"""

# =============================================================================
# EJERCICIO 1: Funciones con *args y **kwargs
# Parámetros de longitud variable
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: *args y **kwargs")
print("=" * 60)


def sumar_todos(*args):
    """
    Suma una cantidad variable de números.

    *args empaqueta todos los argumentos posicionales extras en una TUPLA.
    Esto permite llamar a la función con cualquier cantidad de argumentos.

    Args:
        *args: Números a sumar (cantidad variable).

    Returns:
        float: La suma total de todos los argumentos.
    """
    total = 0
    for numero in args:
        total += numero
    return total


# Podemos pasar cualquier cantidad de argumentos
print(f"sumar_todos(1, 2, 3) = {sumar_todos(1, 2, 3)}")
print(f"sumar_todos(10, 20) = {sumar_todos(10, 20)}")
print(f"sumar_todos(5, 10, 15, 20, 25) = {sumar_todos(5, 10, 15, 20, 25)}")

print()


def crear_ficha(**kwargs):
    """
    Crea una ficha con información variable usando kwargs.

    **kwargs empaqueta todos los argumentos con nombre extras en un DICCIONARIO.
    Esto permite pasar cualquier combinación de datos clave-valor.

    Args:
        **kwargs: Pares clave-valor con la información de la ficha.

    Returns:
        str: La ficha formateada como texto.
    """
    ficha = "+--- FICHA ---+\n"
    for clave, valor in kwargs.items():
        ficha += f"| {clave.capitalize():>12}: {valor}\n"
    ficha += "+-------------+"
    return ficha


# Podemos pasar cualquier combinación de datos
print(crear_ficha(nombre="Simón", edad=20, carrera="ADSO"))
print()
print(crear_ficha(producto="Laptop", precio=2500000, marca="HP", stock=15))

print()


def funcion_flexible(titulo, *args, **kwargs):
    """
    Demuestra el uso combinado de parámetros normales, *args y **kwargs.

    Args:
        titulo (str): Título obligatorio.
        *args: Valores adicionales (posicionales).
        **kwargs: Opciones adicionales (con nombre).
    """
    print(f"\n  Título: {titulo}")
    print(f"  Args recibidos ({len(args)}): {args}")
    print(f"  Kwargs recibidos ({len(kwargs)}): {kwargs}")


funcion_flexible("Reporte", 1, 2, 3, formato="PDF", paginas=10)

print()


# =============================================================================
# EJERCICIO 2: Funciones lambda
# Funciones anónimas de una sola expresión
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: Funciones lambda")
print("=" * 60)

# Función tradicional
def cuadrado_normal(x):
    """Retorna el cuadrado de x."""
    return x ** 2

# Función lambda equivalente
# Sintaxis: lambda argumentos: expresión
cuadrado_lambda = lambda x: x ** 2

print(f"Función normal: cuadrado(5) = {cuadrado_normal(5)}")
print(f"Función lambda: cuadrado(5) = {cuadrado_lambda(5)}")

print()

# Lambda con múltiples parámetros
suma = lambda a, b: a + b
multiplicar = lambda a, b: a * b
maximo = lambda a, b: a if a > b else b

print(f"suma(3, 7) = {suma(3, 7)}")
print(f"multiplicar(4, 6) = {multiplicar(4, 6)}")
print(f"maximo(15, 23) = {maximo(15, 23)}")

print()

# Uso práctico de lambda: ordenamiento personalizado
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Carlos", "nota": 92},
    {"nombre": "Diana", "nota": 78},
    {"nombre": "Eduardo", "nota": 95},
]

# sorted() con key=lambda para ordenar por un criterio personalizado
por_nota = sorted(estudiantes, key=lambda e: e["nota"], reverse=True)
print("Estudiantes ordenados por nota (mayor a menor):")
for est in por_nota:
    print(f"  {est['nombre']}: {est['nota']}")

print()


# =============================================================================
# EJERCICIO 3: Funciones como parámetros (Higher-Order Functions)
# Funciones que reciben otras funciones como argumentos
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: Funciones de orden superior")
print("=" * 60)


def aplicar_operacion(numeros, operacion):
    """
    Aplica una función (operación) a cada elemento de una lista.

    Una función de orden superior es aquella que recibe otra función
    como parámetro o retorna una función.

    Args:
        numeros (list): Lista de números a procesar.
        operacion (callable): Función a aplicar a cada elemento.

    Returns:
        list: Nueva lista con los resultados.
    """
    resultados = []
    for num in numeros:
        resultados.append(operacion(num))
    return resultados


# Definimos diferentes operaciones
def al_cuadrado(x):
    """Retorna x al cuadrado."""
    return x ** 2

def doble(x):
    """Retorna el doble de x."""
    return x * 2

def es_par_texto(x):
    """Retorna si x es par como texto."""
    return f"{x} es par" if x % 2 == 0 else f"{x} es impar"


numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")
print(f"Al cuadrado:    {aplicar_operacion(numeros, al_cuadrado)}")
print(f"Al doble:       {aplicar_operacion(numeros, doble)}")
print(f"Par/Impar:      {aplicar_operacion(numeros, es_par_texto)}")

# También podemos pasar una lambda directamente
print(f"Al cubo:        {aplicar_operacion(numeros, lambda x: x ** 3)}")

print()


def crear_multiplicador(factor):
    """
    Función que retorna otra función (closure).

    Este es un patrón llamado 'closure' donde la función interna
    recuerda el valor de 'factor' incluso después de que la función
    externa haya terminado.

    Args:
        factor (int): El factor de multiplicación.

    Returns:
        function: Una función que multiplica su argumento por el factor.
    """
    def multiplicar(x):
        return x * factor
    return multiplicar


# Creamos funciones especializadas
doble = crear_multiplicador(2)
triple = crear_multiplicador(3)
por_diez = crear_multiplicador(10)

print(f"doble(5) = {doble(5)}")
print(f"triple(5) = {triple(5)}")
print(f"por_diez(5) = {por_diez(5)}")

print()


# =============================================================================
# EJERCICIO 4: map(), filter() y reduce()
# Funciones built-in de alto orden para procesamiento de datos
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: map(), filter() y reduce()")
print("=" * 60)

# --- map() ---
# Aplica una función a cada elemento de un iterable
# Retorna un iterador (lo convertimos a lista con list())
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() con lambda: elevar al cuadrado
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Originales:  {numeros}")
print(f"Cuadrados:   {cuadrados}")

# map() con función named
temperaturas_celsius = [0, 20, 37, 100]
temperaturas_fahrenheit = list(map(lambda c: c * 9/5 + 32, temperaturas_celsius))
print(f"\nCelsius:     {temperaturas_celsius}")
print(f"Fahrenheit:  {temperaturas_fahrenheit}")

print()

# --- filter() ---
# Filtra elementos de un iterable según una condición (función que retorna bool)
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Filtrar palabras largas
palabras = ["sol", "computadora", "gato", "programación", "if", "Python", "a"]
largas = list(filter(lambda p: len(p) > 4, palabras))
print(f"Palabras con más de 4 letras: {largas}")

print()

# --- reduce() ---
# Acumula un resultado aplicando una función a pares de elementos
# Necesita importarse desde functools
from functools import reduce

# Sumar todos los números
suma_total = reduce(lambda acumulador, x: acumulador + x, numeros)
print(f"Suma con reduce: {suma_total}")

# Encontrar el máximo
maximo = reduce(lambda a, b: a if a > b else b, numeros)
print(f"Máximo con reduce: {maximo}")

# Concatenar strings
palabras_concat = ["Python", " es", " un", " lenguaje", " genial"]
frase = reduce(lambda a, b: a + b, palabras_concat)
print(f"Concatenar con reduce: '{frase}'")

print()

# --- Combinando map() y filter() ---
print("Combinación de map() y filter():")
# Primero filtramos los pares, luego los elevamos al cuadrado
resultado = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros)))
print(f"Pares al cuadrado: {resultado}")

print()

print("=" * 60)
print("Fin del módulo de funciones avanzadas")
print("=" * 60)
