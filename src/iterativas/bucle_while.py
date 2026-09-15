"""
Módulo de Bucle WHILE en Python
===============================
Este módulo contiene ejercicios prácticos sobre el uso del bucle while,
incluyendo: contadores, acumuladores, condiciones centinela, menús
interactivos con while True, y validación de entrada.

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones
"""

# =============================================================================
# EJERCICIO 1: While básico - Contador y acumulador
# Patrones fundamentales del bucle while
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: While básico - Contador y acumulador")
print("=" * 60)

# --- Patrón Contador ---
# Un contador incrementa una variable en cada iteración
print("Cuenta regresiva:")
contador = 10
while contador > 0:
    print(f"  {contador}...", end="")
    contador -= 1  # Decrementamos el contador
print(" ¡Despegue! !")

print()

# --- Patrón Acumulador ---
# Un acumulador suma valores en cada iteración
print("Acumulador - Suma de números:")
suma = 0
numero = 1
while numero <= 100:
    suma += numero  # Acumulamos el valor de 'numero'
    numero += 1

print(f"  La suma de 1 a 100 es: {suma}")

# Acumulador con producto (factorial)
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i  # Multiplicamos el acumulador por i
    i += 1

print(f"  El factorial de {n} es: {factorial}")
print()


# =============================================================================
# EJERCICIO 2: While con condición centinela
# El bucle se detiene cuando se encuentra un valor especial
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: While con condición centinela")
print("=" * 60)

# Simulamos una lista de entradas del usuario
# En un caso real se usaría input(), pero aquí usamos una lista
# para que el script sea ejecutable sin interacción
entradas_simuladas = [10, 25, 30, 15, 0]  # El 0 es el centinela
indice = 0

suma_notas = 0
cantidad = 0

print("Procesando notas (0 para terminar):")
# El centinela es el valor que indica "fin de datos"
while indice < len(entradas_simuladas):
    valor = entradas_simuladas[indice]
    indice += 1

    if valor == 0:
        # Encontramos el centinela, salimos del bucle
        print("  -> Se encontró el centinela (0), finalizando.")
        break

    suma_notas += valor
    cantidad += 1
    print(f"  Nota #{cantidad}: {valor}")

# Calculamos el promedio solo si hay datos
if cantidad > 0:
    promedio = suma_notas / cantidad
    print(f"\n  Total de notas: {cantidad}")
    print(f"  Suma: {suma_notas}")
    print(f"  Promedio: {promedio:.2f}")
else:
    print("  No se ingresaron notas.")

print()


# =============================================================================
# EJERCICIO 3: While True con break - Menú interactivo
# Patrón común para crear menús que se repiten hasta que el usuario decide salir
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: While True con break - Menú interactivo")
print("=" * 60)

# Simulamos las opciones que el usuario selecciona secuencialmente
opciones_usuario = [1, 2, 3, 4]
indice_opcion = 0

# Simulamos una lista de contactos
contactos = ["Ana - 3001234567", "Carlos - 3109876543"]

while True:
    # Mostramos el menú
    print("\n  --- MENÚ DE CONTACTOS ---")
    print("  1. Ver contactos")
    print("  2. Agregar contacto")
    print("  3. Contar contactos")
    print("  4. Salir")

    # Simulamos la selección del usuario
    if indice_opcion < len(opciones_usuario):
        opcion = opciones_usuario[indice_opcion]
        indice_opcion += 1
    else:
        break  # Seguridad: si se acaban las opciones simuladas

    print(f"  Opción seleccionada: {opcion}")

    if opcion == 1:
        print("\n  Contactos:")
        for i, contacto in enumerate(contactos, 1):
            print(f"    {i}. {contacto}")
    elif opcion == 2:
        nuevo = "Diana - 3205551234"
        contactos.append(nuevo)
        print(f"  Contacto agregado: {nuevo}")
    elif opcion == 3:
        print(f"  Total de contactos: {len(contactos)}")
    elif opcion == 4:
        print("  ¡Hasta luego!")
        break  # Sale del while True
    else:
        print("  Opción no válida, intente de nuevo")

print()


# =============================================================================
# EJERCICIO 4: Validación de entrada con while
# Asegurar que el usuario ingrese datos válidos
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: Validación de entrada con while")
print("=" * 60)

# Simulamos intentos del usuario para ingresar una edad válida
intentos_edad = [-5, 200, "abc", 25]  # Solo el último es válido
indice_intento = 0

edad_valida = None

print("Validación de edad (debe ser entre 0 y 120):")
while edad_valida is None:
    if indice_intento < len(intentos_edad):
        entrada = intentos_edad[indice_intento]
        indice_intento += 1
    else:
        break

    # Verificamos si la entrada es un número válido
    if not isinstance(entrada, int):
        print(f"  [X] '{entrada}' no es un número válido. Intente de nuevo.")
        continue  # Vuelve al inicio del while

    if entrada < 0 or entrada > 120:
        print(f"  [X] {entrada} está fuera de rango (0-120). Intente de nuevo.")
        continue

    # Si llegamos aquí, la entrada es válida
    edad_valida = entrada
    print(f"  [OK] Edad válida registrada: {edad_valida}")

print()


# =============================================================================
# EJERCICIO 5: Algoritmos clásicos con while
# Ejemplos de algoritmos que usan while de forma natural
# =============================================================================

print("=" * 60)
print("EJERCICIO 5: Algoritmos clásicos con while")
print("=" * 60)

# --- Algoritmo de Euclides para el MCD (Máximo Común Divisor) ---
a, b = 48, 18
a_original, b_original = a, b

print(f"MCD de {a} y {b}:")
while b != 0:
    print(f"  {a} = {b} × {a // b} + {a % b}")
    a, b = b, a % b  # Intercambio simultáneo

print(f"  MCD({a_original}, {b_original}) = {a}")
print()

# --- Número invertido ---
numero_original = 12345
numero = numero_original
invertido = 0

print(f"Invirtiendo el número {numero_original}:")
while numero > 0:
    # Extraemos el último dígito con módulo 10
    digito = numero % 10
    # Lo agregamos al número invertido multiplicando por 10
    invertido = invertido * 10 + digito
    # Eliminamos el último dígito con división entera
    numero //= 10

print(f"  Resultado: {invertido}")
print()

# --- Conversión decimal a binario ---
decimal = 42
decimal_original = decimal
binario = ""

print(f"Convirtiendo {decimal} a binario:")
while decimal > 0:
    residuo = decimal % 2
    binario = str(residuo) + binario  # Agregamos al inicio
    decimal //= 2

print(f"  {decimal_original} en binario es: {binario}")
# Verificación con función built-in de Python
print(f"  Verificación con bin(): {bin(decimal_original)}")

print()

print("=" * 60)
print("Fin del módulo de bucle while")
print("=" * 60)
