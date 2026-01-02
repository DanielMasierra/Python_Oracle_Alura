#Bruno gestiona un pequeño comercio y quiere saber qué producto tuvo el mejor desempeño de 
# ventas el mes pasado. Registró la cantidad vendida de dos productos: manzanas y plátanos.
# Ahora, necesita escribir un programa que identifique y muestre cuál de ellos tuvo más ventas.
# Crea un programa que reciba el número de ventas de los dos productos y muestre un 
# mensaje indicando cuál de ellos vendió más. Si las cantidades son iguales, 
# muestra un mensaje diciendo que hubo un empate.

manzanas = int(input('Digite la cantidad de manzanas vendidas:'))
platanos = int(input('Digite la cantidad de platanos vendidas:'))

if platanos > manzanas: 
    print('Los platanos tuvieron más ventas')
elif platanos < manzanas: 
    print('las manzanas tuvieron más ventas')
else: 
    print('Hubo un empate en ventas')