"""
Módulo de Condicionales Anidados en Python
==========================================
Este módulo demuestra el uso de estructuras condicionales anidadas,
es decir, condicionales dentro de otros condicionales, para resolver
problemas que requieren múltiples niveles de decisión.

Autor: Simón Carmona
Actividad: GA1-220501093-04-AA1-EV02
Tema: Fundamentos de Python - Estructuras de control y funciones
"""

# =============================================================================
# EJERCICIO 1: Menú de opciones con sub-opciones
# Sistema de menú de una tienda virtual
# =============================================================================

print("=" * 60)
print("EJERCICIO 1: Menú de tienda con condicionales anidados")
print("=" * 60)

# Simulamos las selecciones del usuario
categoria = "electronica"
subcategoria = "celulares"

# Primer nivel: selección de categoría
if categoria == "electronica":
    print("Categoría: Electrónica")

    # Segundo nivel (anidado): selección de subcategoría
    if subcategoria == "celulares":
        print("  -> Subcategoría: Celulares")
        print("  -> Productos disponibles: iPhone, Samsung, Xiaomi")
    elif subcategoria == "computadores":
        print("  -> Subcategoría: Computadores")
        print("  -> Productos disponibles: Laptop HP, MacBook, Dell")
    else:
        print(f"  -> Subcategoría '{subcategoria}' no encontrada en Electrónica")

elif categoria == "ropa":
    print("Categoría: Ropa")

    if subcategoria == "hombre":
        print("  -> Subcategoría: Hombre")
    elif subcategoria == "mujer":
        print("  -> Subcategoría: Mujer")
    else:
        print(f"  -> Subcategoría '{subcategoria}' no encontrada en Ropa")

else:
    print(f"Categoría '{categoria}' no disponible")

print()


# =============================================================================
# EJERCICIO 2: Validación de datos con múltiples condiciones
# Registro de usuario con validaciones escalonadas
# =============================================================================

print("=" * 60)
print("EJERCICIO 2: Validación escalonada de registro")
print("=" * 60)

# Datos del usuario a validar
nombre_usuario = "simon123"
contrasena = "MiPass2026!"
edad_registro = 20
email = "simon@email.com"

# Validación escalonada: cada nivel verifica una condición diferente
# Si falla una validación, no se evalúan las siguientes
if len(nombre_usuario) >= 4:
    print(f"[OK] Nombre de usuario '{nombre_usuario}' tiene longitud válida")

    if len(contrasena) >= 8:
        print(f"[OK] Contraseña tiene longitud válida ({len(contrasena)} caracteres)")

        if edad_registro >= 18:
            print(f"[OK] Edad válida ({edad_registro} años)")

            if "@" in email and "." in email:
                print(f"[OK] Email válido ({email})")
                print("\n¡Registro exitoso! Todos los datos son válidos.")
            else:
                print(f"[X] Email inválido: '{email}'")
        else:
            print(f"[X] Debe ser mayor de 18 años (edad actual: {edad_registro})")
    else:
        print(f"[X] Contraseña muy corta ({len(contrasena)} caracteres, mínimo 8)")
else:
    print(f"[X] Nombre de usuario muy corto ({len(nombre_usuario)} caracteres, mínimo 4)")

print()


# =============================================================================
# EJERCICIO 3: Calculadora de descuentos
# Descuento basado en tipo de cliente y monto de compra
# =============================================================================

print("=" * 60)
print("EJERCICIO 3: Calculadora de descuentos")
print("=" * 60)

# Datos de la compra
tipo_cliente = "premium"  # Opciones: "regular", "premium", "vip"
monto_compra = 250000     # Monto en pesos
dia_especial = True       # Si es día de promoción

# Determinamos el descuento base según el tipo de cliente
if tipo_cliente == "vip":
    descuento_base = 20  # 20% para VIP

    # Los clientes VIP tienen beneficio adicional por monto alto
    if monto_compra > 500000:
        descuento_adicional = 10
        print(f"  -> Descuento adicional VIP por compra mayor a $500,000")
    else:
        descuento_adicional = 5

elif tipo_cliente == "premium":
    descuento_base = 10  # 10% para Premium

    if monto_compra > 300000:
        descuento_adicional = 5
        print(f"  -> Descuento adicional Premium por compra mayor a $300,000")
    elif monto_compra > 100000:
        descuento_adicional = 3
    else:
        descuento_adicional = 0

else:
    # Cliente regular
    descuento_base = 0
    descuento_adicional = 0

    if monto_compra > 200000:
        descuento_base = 5
        print(f"  -> Descuento por compra mayor a $200,000")

# Descuento extra si es día especial de promoción
if dia_especial:
    descuento_extra = 5
    print(f"  -> ¡Día de promoción! +5% de descuento")
else:
    descuento_extra = 0

# Cálculo final
descuento_total = descuento_base + descuento_adicional + descuento_extra
valor_descuento = monto_compra * (descuento_total / 100)
total_a_pagar = monto_compra - valor_descuento

print(f"\nResumen de compra:")
print(f"  Cliente: {tipo_cliente}")
print(f"  Monto original: ${monto_compra:,.0f}")
print(f"  Descuento base: {descuento_base}%")
print(f"  Descuento adicional: {descuento_adicional}%")
print(f"  Descuento día especial: {descuento_extra}%")
print(f"  Descuento total: {descuento_total}%")
print(f"  Valor descuento: ${valor_descuento:,.0f}")
print(f"  Total a pagar: ${total_a_pagar:,.0f}")
print()


# =============================================================================
# EJERCICIO 4: Clasificador de IMC (Índice de Masa Corporal)
# Ejemplo de condicionales anidados para categorización médica
# =============================================================================

print("=" * 60)
print("EJERCICIO 4: Clasificador de IMC")
print("=" * 60)

# Datos del paciente
peso = 75    # kg
altura = 1.75  # metros
genero = "masculino"

# Calculamos el IMC: peso / altura²
imc = peso / (altura ** 2)

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC calculado: {imc:.2f}")

# Clasificación del IMC según la OMS
if imc < 18.5:
    categoria_imc = "Bajo peso"
    # Subcategoría dentro de bajo peso
    if imc < 16:
        detalle = "Delgadez severa"
    elif imc < 17:
        detalle = "Delgadez moderada"
    else:
        detalle = "Delgadez leve"
elif imc < 25:
    categoria_imc = "Peso normal"
    detalle = "Rango saludable"
elif imc < 30:
    categoria_imc = "Sobrepeso"
    detalle = "Pre-obesidad"
else:
    categoria_imc = "Obesidad"
    # Subcategoría dentro de obesidad
    if imc < 35:
        detalle = "Obesidad grado I"
    elif imc < 40:
        detalle = "Obesidad grado II"
    else:
        detalle = "Obesidad grado III (mórbida)"

print(f"Categoría: {categoria_imc}")
print(f"Detalle: {detalle}")
print()

print("=" * 60)
print("Fin del módulo de condicionales anidados")
print("=" * 60)
