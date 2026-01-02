"""Una escuela otorga becas según tres criterios:

Ingreso familiar mensual.
Promedio del estudiante.
Asistencia (en porcentaje).

Reglas:

Si el ingreso es menor a $1,500 y el promedio es mayor a 8.0 y 
la asistencia es al menos 90% → "Beca completa"
Si el ingreso es menor a $2,500 y promedio mayor a 7.0 y 
asistencia al menos 85% → "Media beca"
En otros casos → "No elegible para beca"""


Ingreso_familiar_mensual = float(input('Digite el ingreso familiar mensual: '))
Promedio_estudiante = float(input('Digite el promedio del estudiante: '))
Asistencia = int(input('Digite el porcentaje de asistencias: '))

if Ingreso_familiar_mensual < 1500 and Promedio_estudiante > 8.0 and Asistencia >= 90: 
    print('Beca completa')
elif Ingreso_familiar_mensual < 2500 and Promedio_estudiante > 7.0 and Asistencia >= 85: 
    print('Media beca')
else: 
    print('No elegible para la beca')