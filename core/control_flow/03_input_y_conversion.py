# Input básico
nombre = input("Escribe tu nombre: ")
print(f"\nHola, {nombre}")

# Conversión a entero
anio_admision = int(input("\nEscribe el año de admisión: "))

# Conversión a flotante
nota_admision = float(input("Escribe la nota de admisión: "))

# Mostrar tipos
print("\nTipos de datos:")
print(type(nombre))
print(type(anio_admision))
print(type(nota_admision))

# Salida formateada
print("\n\tResumen del estudiante")
print(f"\tAño de admisión: {anio_admision}")
print(f"\tNota de admisión: {nota_admision}")
