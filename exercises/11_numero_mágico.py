"""Estás desarrollando un pequeño juego. El usuario ingresa un número entero
y el programa debe evaluar lo siguiente:
Si el número es divisible por 3 y 5, muestra: "¡Número mágico!"
Si solo es divisible por 3, muestra: "Divisible por 3"
Si solo es divisible por 5, muestra: "Divisible por 5"
Si no es divisible por ninguno, muestra: "No es un número mágico"
Este tipo de lógica es muy útil en juegos, validaciones o filtros."""


numero_magico = int(input("Escribe un número: "))

if numero_magico:
    if numero_magico%3==0 and numero_magico%5==0:
        print("Felicidades encontraste un número mágico")
    elif numero_magico%3 == 0: 
        print("Divisible por 3")
    elif numero_magico%5 == 0: 
        print("Divisible por 5")
    else: 
        print("No es número mágico")