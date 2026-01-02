#1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y 
# muestre el número más grande.

def ejercicio_1():

    numero_1 = float(input('Escribe el primer número:'))
    numero_2 = float(input('Escribe el segundo número:'))

    if numero_1 > numero_2:
        print(f'El número mayor es: {numero_1}')
    elif numero_2 > numero_1:
        print(f'El número mayor es: {numero_2}')
    else: 
        print('Ambos números son iguales')


#2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e 
# informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).

def ejercicio_2():
    crecimiento_porcentual = float(input('Escriba el crecimiento porcentual de su empresa:'))
    if crecimiento_porcentual > 0:
        print('La empresa creció en producción')
    elif crecimiento_porcentual == 0: 
        print('La empresa se estancó')
    else:
        print('La empresa decreció')

#3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria 
# es una vocal o una consonante.

def ejercicio_3():
    letra = input('Escribe una vocal o consonante: ').lower()
    vocales = 'aeiou'
    if letra in vocales:
        print('Elegiste una vocal')
    else:
        print('Elegiste una consonante')


#4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil 
# durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.

def ejercicio_4():
    precio_ano1 = float(input('Ingrese el precio promedio del automovil en el primer año: '))
    precio_ano2 = float(input('Ingrese el precio promedio del automovil en el segundo año: '))
    precio_ano3 = float(input('Ingrese el precio promedio del automovil en el tercer año: '))

    mayor = precio_ano1
    if precio_ano2 > mayor:
        mayor = precio_ano2
    if precio_ano3 > mayor:
        mayor = precio_ano3

    menor = precio_ano1
    if precio_ano2 < menor:
        menor = precio_ano2
    if precio_ano3 < menor:
        menor = precio_ano3

    print(f'El precio más alto fue de ${mayor}')
    print(f'El precio más bajo fue de ${menor}')

#5 - Escribe un programa que pregunte sobre el precio de tres productos e 
# indique cuál es el producto más barato para comprar.

def ejercicio_5 (): 
    Producto_1 = float(input('Ingrese el precio del primer producto: '))
    Producto_2 = float(input('Ingrese el precio del segundo producto: ')) 
    Producto_3 = float(input('Ingrese el precio del tercer producto: ')) 

    Producto_barato = Producto_1  
    if Producto_2 < Producto_1:
        Producto_barato = Producto_2
    if Producto_3 < Producto_2: 
        Producto_barato = Producto_3

    print(f'El producto más barato cuesta: {Producto_barato}')


    
