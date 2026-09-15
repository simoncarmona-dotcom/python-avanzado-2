"""
Módulo de Funciones Recursivas en Python
========================================
Este módulo contiene ejercicios prácticos sobre recursividad,
una técnica donde una función se llama a sí misma para resolver
un problema dividiéndolo en subproblemas más pequeños.

Cada función recursiva tiene dos componentes clave:
1. Caso base: condición que detiene la recursión.
2. Caso recursivo: la función se llama a sí misma con un problema más pequeño.

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones
"""

# =============================================================================
# EJERCICIO 1: Factorial recursivo
# n! = n × (n-1) × (n-2) × ... × 1
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: Factorial recursivo")
print("=" * 60)


def factorial(n):
    """
    Calcula el factorial de un número usando recursividad.

    El factorial de n (n!) se define como:
    - 0! = 1 (caso base)
    - n! = n × (n-1)! (caso recursivo)

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es negativo.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    # Validación de entrada
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    # Caso base: el factorial de 0 es 1
    if n == 0 or n == 1:
        return 1

    # Caso recursivo: n! = n × (n-1)!
    return n * factorial(n - 1)


# Probamos con varios valores
for i in range(8):
    print(f"  {i}! = {factorial(i)}")

# Mostramos el proceso paso a paso para factorial(5)
print(f"\n  Proceso de factorial(5):")
print(f"  5! = 5 × 4! = 5 × 4 × 3! = 5 × 4 × 3 × 2! = 5 × 4 × 3 × 2 × 1! = 120")

print()


# =============================================================================
# EJERCICIO 2: Fibonacci recursivo
# Cada número es la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13...
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: Fibonacci recursivo")
print("=" * 60)


def fibonacci(n):
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci.

    La secuencia de Fibonacci se define como:
    - F(0) = 0 (caso base)
    - F(1) = 1 (caso base)
    - F(n) = F(n-1) + F(n-2) (caso recursivo)

    Args:
        n (int): Posición en la secuencia (0-indexed).

    Returns:
        int: El n-ésimo número de Fibonacci.
    """
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Caso recursivo: la suma de los dos anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)


# Generamos los primeros 15 números de Fibonacci
print("  Secuencia de Fibonacci (primeros 15):")
secuencia = []
for i in range(15):
    secuencia.append(fibonacci(i))
print(f"  {secuencia}")

# También podemos usar list comprehension
print(f"\n  Verificación: {[fibonacci(i) for i in range(15)]}")

print()


# =============================================================================
# EJERCICIO 3: Suma de dígitos recursiva
# Suma los dígitos de un número: 12345 -> 1+2+3+4+5 = 15
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: Suma de dígitos recursiva")
print("=" * 60)


def suma_digitos(n):
    """
    Calcula la suma de los dígitos de un número entero positivo.

    Estrategia recursiva:
    - Caso base: si n tiene un solo dígito (n < 10), retornar n.
    - Caso recursivo: sumar el último dígito (n % 10) con la suma de
      los dígitos restantes (n // 10).

    Args:
        n (int): Número entero positivo.

    Returns:
        int: La suma de sus dígitos.

    Examples:
        >>> suma_digitos(12345)
        15
        >>> suma_digitos(9)
        9
    """
    # Trabajamos con el valor absoluto por si es negativo
    n = abs(n)

    # Caso base: número de un solo dígito
    if n < 10:
        return n

    # Caso recursivo:
    # n % 10 -> último dígito (ej: 12345 % 10 = 5)
    # n // 10 -> número sin el último dígito (ej: 12345 // 10 = 1234)
    return (n % 10) + suma_digitos(n // 10)


# Pruebas
numeros_prueba = [12345, 999, 100, 7, 54321]
for num in numeros_prueba:
    resultado = suma_digitos(num)
    digitos = " + ".join(str(d) for d in str(num))
    print(f"  suma_digitos({num}) = {digitos} = {resultado}")

print()


# =============================================================================
# EJERCICIO 4: Potencia recursiva
# Calcular base^exponente usando recursividad
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: Potencia recursiva")
print("=" * 60)


def potencia(base, exponente):
    """
    Calcula base elevado a exponente de forma recursiva.

    Definición recursiva:
    - base^0 = 1 (caso base)
    - base^n = base × base^(n-1) (caso recursivo)

    Args:
        base (float): La base de la potencia.
        exponente (int): El exponente (entero no negativo).

    Returns:
        float: El resultado de base^exponente.
    """
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1

    # Caso recursivo: multiplicamos base por base^(exponente-1)
    return base * potencia(base, exponente - 1)


# Pruebas
print(f"  2^10  = {potencia(2, 10)}")
print(f"  3^4   = {potencia(3, 4)}")
print(f"  5^0   = {potencia(5, 0)}")
print(f"  10^3  = {potencia(10, 3)}")

# Verificamos contra el operador ** de Python
print(f"\n  Verificación: 2**10 = {2**10}, 3**4 = {3**4}")

print()


# =============================================================================
# EJERCICIO 5: Búsqueda binaria recursiva
# Buscar un elemento en una lista ordenada dividiendo a la mitad
# =============================================================================

print("=" * 60)
print("EJERCICIO 5: Búsqueda binaria recursiva")
print("=" * 60)


def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    """
    Busca un elemento en una lista ordenada usando búsqueda binaria recursiva.

    La búsqueda binaria divide repetidamente el espacio de búsqueda a la mitad:
    1. Compara el elemento central con el objetivo.
    2. Si es igual, lo encontramos.
    3. Si el objetivo es menor, busca en la mitad izquierda.
    4. Si el objetivo es mayor, busca en la mitad derecha.

    Args:
        lista (list): Lista ordenada de elementos.
        objetivo: El elemento a buscar.
        inicio (int): Índice inicial del rango de búsqueda.
        fin (int): Índice final del rango de búsqueda.

    Returns:
        int: El índice del elemento si se encuentra, -1 si no.
    """
    if fin is None:
        fin = len(lista) - 1

    # Caso base: el rango es inválido (no encontrado)
    if inicio > fin:
        return -1

    # Calculamos el punto medio
    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio  # ¡Encontrado!
    elif lista[medio] > objetivo:
        # El objetivo está en la mitad izquierda
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        # El objetivo está en la mitad derecha
        return busqueda_binaria(lista, objetivo, medio + 1, fin)


# Lista ordenada para buscar
numeros_ordenados = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"  Lista: {numeros_ordenados}")

# Buscar varios valores
valores_buscar = [23, 72, 5, 50]
for valor in valores_buscar:
    indice = busqueda_binaria(numeros_ordenados, valor)
    if indice != -1:
        print(f"  Buscar {valor}: encontrado en índice [{indice}]")
    else:
        print(f"  Buscar {valor}: no encontrado")

print()


# =============================================================================
# EJERCICIO 6: Recursión vs Iteración - Comparación
# Mismo problema resuelto de ambas formas
# =============================================================================

print("=" * 60)
print("EJERCICIO 6: Recursión vs Iteración - Comparación")
print("=" * 60)


def contar_digitos_recursivo(n):
    """
    Cuenta los dígitos de un número de forma recursiva.

    Args:
        n (int): Número entero.

    Returns:
        int: Cantidad de dígitos.
    """
    n = abs(n)
    if n < 10:
        return 1
    return 1 + contar_digitos_recursivo(n // 10)


def contar_digitos_iterativo(n):
    """
    Cuenta los dígitos de un número de forma iterativa.

    Args:
        n (int): Número entero.

    Returns:
        int: Cantidad de dígitos.
    """
    n = abs(n)
    contador = 0
    while n > 0:
        contador += 1
        n //= 10
    return max(contador, 1)  # Al menos 1 dígito (para n=0)


# Comparamos ambos enfoques
numeros_prueba = [5, 42, 100, 12345, 999999]
print(f"  {'Número':>10} | {'Recursivo':>10} | {'Iterativo':>10}")
print(f"  {'-' * 10} | {'-' * 10} | {'-' * 10}")

for num in numeros_prueba:
    rec = contar_digitos_recursivo(num)
    ite = contar_digitos_iterativo(num)
    print(f"  {num:>10} | {rec:>10} | {ite:>10}")

print()

print("=" * 60)
print("Fin del módulo de funciones recursivas")
print("=" * 60)
