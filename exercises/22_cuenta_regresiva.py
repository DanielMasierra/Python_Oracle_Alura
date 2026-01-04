

for segundos in range(10, 0, -1):
    if segundos %2 == 0: 
        print (f'Faltan solo {segundos} segundos - ¡No pierdas esta oportunidad!')
    else: 
        print (f'La cuenta conitúa: {segundos} segundos restantes')
print("¡Aprovecha la promoción ahora!")


"""En este ejercicio la linea de "range" controla cómo cuenta el programa. Le estoy diciendo un inicio (10), fin (0)
y cuanto avanza en casa iteración (-1)

Luego, en el caso del if segundos %2 ===:0, este paso es importante para identificar que se trata de un número par"""