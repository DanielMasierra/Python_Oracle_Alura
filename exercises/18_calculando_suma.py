"""Estás recibiendo una lista de valores que representan los productos de tu tienda virtual y 
te gustaría calcular la suma total de esos productos para entender el desempeño financiero semanal.

valores = [10, 20, 30, 40, 50]
Copia el código
Crea un programa para implementar la suma.

Salida esperada:

La suma total de los ingresos es: 150

¿Lograste implementar? ¡Compártelo con nosotros en el foro!"""


numeros = [10, 20, 30, 40, 50]

suma = 0
for numero in numeros: 
    suma += numero

print(f'La suma total de los ingresos es: {suma}')