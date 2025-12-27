#---**Situación:** Recibiremos el promedio de la nota de los estudiantes y 
# necesitamos de un algoritmo que ejecute el análisis y determine si el estudiante 
# fue **Aprobado** o **Reprobado**, mostrando un mensaje del resultado. 
# Para ser aprobado, el promedio necesita ser igual o superior a 7.0.


nota = float(input('Digita la nota: '))

if nota >= 7: 
  print('Aprobó.')
else: 
  print('reprobó.')

#Ahora, nuestra institución educativa estableció que las personas que tengan el promedio entre 5.0 y 7.0 
# pueden participar del curso de Recuperación durante las vacaciones para lograr aprobar.
# Entonces podemos apoyarnos en un conjunto de ifs para poder estructurar esta nueva condición.

  """
  nota = float(input('Digita la nota: '))

if nota >= 7: 
  print('Aprobó.')
if 7> nota >=5:
  print('Recuperación.')
if nota < 5:  
  print('reprobó.')
"""