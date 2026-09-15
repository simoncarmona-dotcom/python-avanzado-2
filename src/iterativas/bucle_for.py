"""
Módulo de Bucle FOR en Python
=============================
Este módulo contiene ejercicios prácticos sobre el uso del bucle for,
incluyendo: range(), iteración sobre colecciones, enumerate(), zip(),
comprensiones de listas, y control de flujo con break/continue.

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones
"""

# =============================================================================
# EJERCICIO 1: for con range() - Diferentes variantes
# range(stop), range(start, stop), range(start, stop, step)
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: for con range() - Variantes")
print("=" * 60)

# range(stop): genera números desde 0 hasta stop-1
print("range(5) -> ", end="")
for i in range(5):
    print(i, end=" ")
print()  # Salto de línea

# range(start, stop): genera números desde start hasta stop-1
print("range(2, 8) -> ", end="")
for i in range(2, 8):
    print(i, end=" ")
print()

# range(start, stop, step): genera números con un paso definido
print("range(0, 20, 3) -> ", end="")
for i in range(0, 20, 3):
    print(i, end=" ")
print()

# range con paso negativo: cuenta regresiva
print("range(10, 0, -2) -> ", end="")
for i in range(10, 0, -2):
    print(i, end=" ")
print()

# Uso práctico: sumar los primeros N números
n = 10
suma = 0
for i in range(1, n + 1):
    suma += i
print(f"\nSuma de 1 a {n} = {suma}")

print()


# =============================================================================
# EJERCICIO 2: for con listas, tuplas y strings
# Iteración sobre diferentes tipos de colecciones
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: for con colecciones")
print("=" * 60)

# Iteración sobre una lista
frutas = ["manzana", "banana", "cereza", "durazno", "uva"]
print("Frutas disponibles:")
for fruta in frutas:
    # Accedemos directamente a cada elemento de la lista
    print(f"  * {fruta.capitalize()}")

print()

# Iteración sobre una tupla (inmutable)
coordenadas = (10.5, 20.3, 30.1)
print("Coordenadas (x, y, z):")
ejes = ["x", "y", "z"]
for i in range(len(coordenadas)):
    print(f"  {ejes[i]} = {coordenadas[i]}")

print()

# Iteración sobre un string (carácter por carácter)
palabra = "Python"
print(f"Caracteres de '{palabra}':")
for caracter in palabra:
    print(f"  '{caracter}' -> código ASCII: {ord(caracter)}")

print()


# =============================================================================
# EJERCICIO 3: for con enumerate()
# enumerate() agrega un contador automático a la iteración
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: for con enumerate()")
print("=" * 60)

# enumerate() devuelve tuplas (índice, elemento)
# Esto evita tener que usar range(len(lista))
lenguajes = ["Python", "JavaScript", "Java", "C++", "Go"]

print("Lenguajes de programación (con índice):")
for indice, lenguaje in enumerate(lenguajes):
    print(f"  [{indice}] {lenguaje}")

print()

# enumerate() con inicio personalizado (start=1)
print("Lista de tareas pendientes:")
tareas = ["Estudiar Python", "Hacer ejercicios", "Subir a GitHub", "Documentar"]
for numero, tarea in enumerate(tareas, start=1):
    print(f"  {numero}. {tarea}")

print()


# =============================================================================
# EJERCICIO 4: for con zip()
# zip() permite iterar sobre múltiples colecciones simultáneamente
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: for con zip()")
print("=" * 60)

# zip() combina elementos de dos o más listas por posición
nombres = ["Ana", "Carlos", "Diana", "Eduardo"]
edades = [25, 30, 22, 28]
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla"]

print("Registro de personas:")
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre} tiene {edad} años y vive en {ciudad}")

print()

# zip() para crear un diccionario a partir de dos listas
claves = ["nombre", "edad", "carrera"]
valores = ["Simón", 20, "Análisis y Desarrollo de Software"]

# dict() + zip() es una forma elegante de crear diccionarios
datos_estudiante = dict(zip(claves, valores))
print("Diccionario creado con zip():")
for clave, valor in datos_estudiante.items():
    print(f"  {clave}: {valor}")

print()


# =============================================================================
# EJERCICIO 5: Comprensión de listas (List Comprehension)
# Forma concisa y pythónica de crear listas
# =============================================================================

print("=" * 60)
print("EJERCICIO 5: Comprensión de listas")
print("=" * 60)

# Forma tradicional con for:
cuadrados_tradicional = []
for x in range(1, 11):
    cuadrados_tradicional.append(x ** 2)

# Forma con list comprehension (equivalente, pero más concisa):
# Sintaxis: [expresión for variable in iterable]
cuadrados = [x ** 2 for x in range(1, 11)]
print(f"Cuadrados del 1 al 10: {cuadrados}")

# List comprehension con condición (filtrado)
# Sintaxis: [expresión for variable in iterable if condición]
pares = [x for x in range(1, 21) if x % 2 == 0]
print(f"Números pares del 1 al 20: {pares}")

# List comprehension con transformación de strings
palabras = ["hola", "mundo", "python", "es", "genial"]
mayusculas = [p.upper() for p in palabras if len(p) > 2]
print(f"Palabras en mayúsculas (>2 chars): {mayusculas}")

# List comprehension con operación ternaria
numeros = [1, -2, 3, -4, 5, -6, 7]
absolutos = [n if n >= 0 else -n for n in numeros]
print(f"Valores absolutos: {absolutos}")

print()


# =============================================================================
# EJERCICIO 6: break y continue en ciclos for
# Control del flujo de iteración
# =============================================================================

print("=" * 60)
print("EJERCICIO 6: break y continue")
print("=" * 60)

# break: sale del bucle completamente cuando se cumple la condición
print("Buscando el primer múltiplo de 7 mayor a 50:")
for i in range(1, 100):
    if i * 7 > 50:
        print(f"  Encontrado: {i} × 7 = {i * 7}")
        break  # Detiene el bucle inmediatamente

print()

# continue: salta a la siguiente iteración sin ejecutar el resto del bloque
print("Números del 1 al 15 (omitiendo múltiplos de 3):")
for i in range(1, 16):
    if i % 3 == 0:
        continue  # Salta esta iteración y pasa a la siguiente
    print(f"  {i}", end="")
print()  # Salto de línea al final

print()

# for...else: el bloque else se ejecuta SOLO si el for terminó normalmente
# (es decir, sin encontrar un break)
print("Búsqueda de número primo:")
numero_prueba = 17
for i in range(2, numero_prueba):
    if numero_prueba % i == 0:
        print(f"  {numero_prueba} NO es primo (divisible por {i})")
        break
else:
    # Este bloque solo se ejecuta si el for NO encontró un divisor
    print(f"  {numero_prueba} ES primo")

print()

print("=" * 60)
print("Fin del módulo de bucle for")
print("=" * 60)
