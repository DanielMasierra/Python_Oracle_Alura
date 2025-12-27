#El comando `elif` es una palabra clave en Python que significa "si no, si" y 
# lo podemos considerar una *contracción* entre `else` e `if`. 
# Se utiliza en conjunto con la palabra clave `if` para formar una estructura condicional en cadena.

nota = float(input('Digita la nota: '))

if nota >= 7: 
  print('Aprobó.')
elif 7> nota >=5:
  print('Recuperación.')
else:  
  print('reprobó.')