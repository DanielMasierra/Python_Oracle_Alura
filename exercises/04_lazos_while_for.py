#1 - Escribe un programa que solicite dos números enteros e
# imprima todos los números enteros entre ellos.

def ejercicio_1():
    inicio = int(input('Ingresa el primer número entero:'))
    fin = int(input('Ingresa el segundo número entero: '))
    if inicio < fin: 
        for i in range (inicio +1, fin):
            print(i)
    elif inicio > fin:
        for i in range (fin +1, inicio): 
            print (i)
    else: 
        print('Los números son iguales')

#2 - Escribe un programa para calcular cuántos días tomará que la 
# colonia de una bacteria A supere o iguale a la colonia de una bacteria B,
#  basado en tasas de crecimiento del 3% y 1.5%, respectivamente. 
# Supón que la colonia A comienza con 4 elementos y B con 10.
