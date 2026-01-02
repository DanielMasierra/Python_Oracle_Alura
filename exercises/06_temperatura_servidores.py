#Lucas trabaja en TI y necesita garantizar que la temperatura de 
# una sala de servidores no supere los 25°C. 
# Quiere un programa que reciba la temperatura actual como entrada y, si es necesario, 
# muestre un mensaje de alerta.

Temperatura = float(input('Digite la temperatura actual: '))
if Temperatura > 25.0:
    print ('¡Alerta! La temperatura está por encima del límite permitido')
else:
    print ('Temperatura dentro del límite permitido')