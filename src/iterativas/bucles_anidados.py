"""
Módulo de Bucles Anidados en Python
====================================
Este módulo demuestra el uso de bucles anidados (un bucle dentro de otro)
para resolver problemas que requieren recorrer estructuras bidimensionales
o generar patrones complejos.

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones
"""

# =============================================================================
# EJERCICIO 1: Tabla de multiplicar
# Uso clásico de bucles anidados para generar una tabla 2D
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: Tabla de multiplicar (1 al 5)")
print("=" * 60)

# El bucle externo controla las filas (multiplicando)
# El bucle interno controla las columnas (multiplicador)

# Encabezado de la tabla
print(f"{'×':>4}", end="")
for j in range(1, 6):
    print(f"{j:>5}", end="")
print()
print("    " + "-" * 25)

# Cuerpo de la tabla
for i in range(1, 6):          # Bucle externo: filas
    print(f"{i:>3} |", end="")
    for j in range(1, 6):      # Bucle interno: columnas
        resultado = i * j
        print(f"{resultado:>5}", end="")
    print()  # Salto de línea al final de cada fila

print()


# =============================================================================
# EJERCICIO 2: Patrones con asteriscos
# Generación de figuras geométricas usando bucles anidados
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: Patrones con asteriscos")
print("=" * 60)

# --- Patrón 1: Triángulo rectángulo ---
print("Triángulo rectángulo (5 filas):")
filas = 5
for i in range(1, filas + 1):
    # El bucle interno imprime 'i' asteriscos en la fila actual
    for j in range(i):
        print("* ", end="")
    print()  # Salto de línea al final de cada fila

print()

# --- Patrón 2: Triángulo invertido ---
print("Triángulo invertido:")
for i in range(filas, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()

print()

# --- Patrón 3: Pirámide centrada ---
print("Pirámide centrada:")
for i in range(1, filas + 1):
    # Espacios antes de los asteriscos para centrar
    espacios = filas - i
    print(" " * espacios, end="")
    # Asteriscos: (2*i - 1) para que sea simétrica
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print()

# --- Patrón 4: Diamante ---
print("Diamante:")
# Mitad superior (incluyendo la fila central)
for i in range(1, filas + 1):
    print(" " * (filas - i), end="")
    print("*" * (2 * i - 1))

# Mitad inferior
for i in range(filas - 1, 0, -1):
    print(" " * (filas - i), end="")
    print("*" * (2 * i - 1))

print()

# --- Patrón 5: Cuadrado hueco ---
print("Cuadrado hueco (5x5):")
lado = 5
for i in range(lado):
    for j in range(lado):
        # Imprimimos asterisco solo en los bordes
        if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
            print("* ", end="")
        else:
            print("  ", end="")  # Espacio interior
    print()

print()


# =============================================================================
# EJERCICIO 3: Búsqueda en una matriz (lista de listas)
# Recorrido de estructuras bidimensionales
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: Operaciones con matrices")
print("=" * 60)

# Definimos una matriz 3x4 (3 filas, 4 columnas)
matriz = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 25, 35]
]

# Imprimir la matriz de forma legible
print("Matriz original:")
for fila in matriz:
    for elemento in fila:
        print(f"{elemento:>4}", end="")
    print()

print()

# Buscar un valor específico en la matriz
valor_buscado = 70
encontrado = False

for i in range(len(matriz)):          # Recorremos filas
    for j in range(len(matriz[i])):   # Recorremos columnas
        if matriz[i][j] == valor_buscado:
            print(f"Valor {valor_buscado} encontrado en posición [{i}][{j}]")
            encontrado = True
            break  # Sale del bucle interno
    if encontrado:
        break  # Sale del bucle externo

if not encontrado:
    print(f"Valor {valor_buscado} no encontrado en la matriz")

print()

# Sumar todos los elementos de la matriz
suma_total = 0
for fila in matriz:
    for elemento in fila:
        suma_total += elemento

print(f"Suma de todos los elementos: {suma_total}")

# Encontrar el valor máximo y su posición
maximo = matriz[0][0]
pos_max = (0, 0)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maximo:
            maximo = matriz[i][j]
            pos_max = (i, j)

print(f"Valor máximo: {maximo} en posición [{pos_max[0]}][{pos_max[1]}]")
print()


# =============================================================================
# EJERCICIO 4: Ordenamiento burbuja (Bubble Sort)
# Algoritmo clásico que usa bucles anidados para ordenar
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: Ordenamiento burbuja")
print("=" * 60)

# Lista desordenada
numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original:  {numeros}")

# Creamos una copia para no modificar la original
lista_ordenada = numeros.copy()

# Algoritmo de burbuja:
# El bucle externo controla las pasadas
# El bucle interno compara elementos adyacentes
n = len(lista_ordenada)
for i in range(n):
    # En cada pasada, el elemento más grande "burbujea" al final
    for j in range(0, n - i - 1):
        if lista_ordenada[j] > lista_ordenada[j + 1]:
            # Intercambiamos los elementos si están en orden incorrecto
            lista_ordenada[j], lista_ordenada[j + 1] = (
                lista_ordenada[j + 1], lista_ordenada[j]
            )
    print(f"  Pasada {i + 1}: {lista_ordenada}")

print(f"\nLista ordenada:  {lista_ordenada}")
print()

print("=" * 60)
print("Fin del módulo de bucles anidados")
print("=" * 60)
