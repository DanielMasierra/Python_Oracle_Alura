# 02_strings_manipulacion.py
# Tratamiento básico de strings

texto = '  Micaela de los Sanyos '

# Transformación encadenada
nuevo_texto = texto.strip().replace('y', 't').upper()

print(nuevo_texto)
print(id(texto), id(nuevo_texto))