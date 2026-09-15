"""
Módulo de Estructuras Condicionales Básicas en Python
=====================================================
Este módulo contiene ejercicios prácticos sobre el uso de las estructuras
de control condicional: if, elif, else, operadores lógicos y operador ternario.

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones
"""

# =============================================================================
# EJERCICIO 1: Estructura if/elif/else básica
# Clasificación de calificaciones según el rango numérico
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: Clasificación de calificaciones")
print("=" * 60)

# Definimos la nota del estudiante
nota = 85

# Evaluamos la nota usando if/elif/else para determinar la categoría
# Se evalúan las condiciones de arriba hacia abajo; la primera que sea
# verdadera ejecutará su bloque y saltará el resto.
if nota >= 90:
    clasificacion = "Excelente"
elif nota >= 80:
    clasificacion = "Sobresaliente"
elif nota >= 70:
    clasificacion = "Bueno"
elif nota >= 60:
    clasificacion = "Aceptable"
else:
    # Si ninguna condición anterior se cumple, la nota es menor a 60
    clasificacion = "Reprobado"

print(f"Nota: {nota}")
print(f"Clasificación: {clasificacion}")
print()


# =============================================================================
# EJERCICIO 2: Operadores lógicos en condicionales (and, or, not)
# Verificación de requisitos para acceder a un sistema
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: Operadores lógicos (and, or, not)")
print("=" * 60)

# Variables que representan el estado del usuario
edad = 25
tiene_cuenta = True
esta_bloqueado = False

# Usamos 'and' para verificar que TODAS las condiciones se cumplan
# Usamos 'not' para negar una condición (no está bloqueado)
if edad >= 18 and tiene_cuenta and not esta_bloqueado:
    print(f"Acceso concedido - Edad: {edad}, Cuenta activa, No bloqueado")
else:
    print("Acceso denegado")

# Usamos 'or' para verificar que AL MENOS UNA condición se cumpla
es_administrador = False
es_moderador = True

if es_administrador or es_moderador:
    print("Tiene permisos especiales (es admin o moderador)")
else:
    print("Usuario regular sin permisos especiales")

print()


# =============================================================================
# EJERCICIO 3: Condicionales con input() del usuario
# Verificación de número par o impar
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: Verificación par/impar con input")
print("=" * 60)

# Usamos un valor fijo para que el script sea ejecutable sin interacción
# En un caso real se usaría: numero = int(input("Ingrese un número: "))
numero = 17

# El operador módulo (%) devuelve el residuo de la división
# Si el residuo de dividir entre 2 es 0, el número es par
if numero % 2 == 0:
    print(f"El número {numero} es PAR")
else:
    print(f"El número {numero} es IMPAR")

# Verificación adicional: positivo, negativo o cero
if numero > 0:
    print(f"El número {numero} es POSITIVO")
elif numero < 0:
    print(f"El número {numero} es NEGATIVO")
else:
    print(f"El número es CERO")

print()


# =============================================================================
# EJERCICIO 4: Operador ternario (expresión condicional en una línea)
# Forma compacta de escribir un if/else simple
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: Operador ternario")
print("=" * 60)

# Sintaxis: valor_si_verdadero if condición else valor_si_falso
edad_usuario = 20

# En lugar de escribir un if/else de 4 líneas, usamos el operador ternario
estado = "Mayor de edad" if edad_usuario >= 18 else "Menor de edad"
print(f"Edad: {edad_usuario} -> {estado}")

# Otro ejemplo: determinar el mayor de dos números
a = 15
b = 23
mayor = a if a > b else b
print(f"El mayor entre {a} y {b} es: {mayor}")

# Ejemplo con strings: verificar si una cadena está vacía
nombre = "Python"
mensaje = f"Hola, {nombre}" if nombre else "Nombre no proporcionado"
print(f"Mensaje: {mensaje}")

print()


# =============================================================================
# EJERCICIO 5: Condicionales con operadores de comparación combinados
# Verificación de rango (encadenamiento de comparaciones)
# =============================================================================

print("=" * 60)
print("EJERCICIO 5: Comparaciones encadenadas y rangos")
print("=" * 60)

# Python permite encadenar comparaciones de forma elegante
temperatura = 22

# En lugar de: if temperatura >= 15 and temperatura <= 25:
# Python permite escribirlo así:
if 15 <= temperatura <= 25:
    print(f"{temperatura}°C -> Temperatura agradable")
elif temperatura < 15:
    print(f"{temperatura}°C -> Hace frío")
else:
    print(f"{temperatura}°C -> Hace calor")

# Verificar si un carácter es una vocal
letra = "a"
# Usamos 'in' para verificar si un elemento está en una secuencia
if letra.lower() in "aeiou":
    print(f"'{letra}' es una VOCAL")
else:
    print(f"'{letra}' es una CONSONANTE")

# Verificar tipo de triángulo según sus lados
lado_a, lado_b, lado_c = 5, 5, 5

if lado_a == lado_b == lado_c:
    tipo_triangulo = "Equilátero (3 lados iguales)"
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    tipo_triangulo = "Isósceles (2 lados iguales)"
else:
    tipo_triangulo = "Escaleno (3 lados diferentes)"

print(f"Triángulo con lados ({lado_a}, {lado_b}, {lado_c}): {tipo_triangulo}")
print()

print("=" * 60)
print("Fin del módulo de condicionales básicas")
print("=" * 60)