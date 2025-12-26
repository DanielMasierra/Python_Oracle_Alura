# Cantidad de empleados
c_vigilante = 5
c_docente = 16
c_coordinador = 2

# Salarios
s_vigilante = 300
s_docente = 500
s_coordinador = 600

# Total de empleados
total_empleados = c_vigilante + c_docente + c_coordinador
print("Total de empleados:", total_empleados)

# Diferencia salarial
diferencia_salario = s_coordinador - s_vigilante
print("Diferencia salarial:", diferencia_salario)

# Promedio ponderado de salarios
promedio_salarios = (
    c_vigilante * s_vigilante +
    c_docente * s_docente +
    c_coordinador * s_coordinador
) / total_empleados

print("Promedio de salarios:", promedio_salarios)
