#1 - Crea un programa que solicite al usuario que escriba su nombre y luego imprima 
# "Hola, [nombre]."

def ejercicio_1():
    nombre = input('Escribe tu nombre: ')
    print(f"\nHola, {nombre}")

#2 - Crea un programa que solicite al usuario que escriba su nombre y edad, y 
# luego imprima "Hola, [nombre], tienes [edad] años."

def ejercicio_2():
    nombre = input("Escribe tu nombre:")
    edad = input("Escribe tu edad: ")
    print(f"Hola, {nombre}, tienes {edad}")


#3 - Crea un programa que solicite al usuario que escriba su nombre, edad y altura en metros, 
# y luego imprima "Hola, [nombre], tienes [edad] años y mides [altura] metros."

def ejercicio_3():
    nombre = input("escribe tu nombre:")
    edad = input("escribe tu edad: ")
    altura = input("escribe tu altura en Metros: ")
    print(f'Hola, {nombre}, tienes {edad} años y mides {altura} metros.')

#4 - Crea un programa que solicite dos valores numéricos al usuario y
#  luego imprima la suma de ambos valores.

def ejercicio_4():
    valor_1 = int(input("escribe el primer número:"))
    valor_2 = int(input("escribe el segundo número:"))
    print(valor_1+valor_2)

#5 - Crea un programa que solicite tres valores numéricos al usuario y 
# luego imprima la suma de los tres valores.

def ejercicio_5():
    valor_1 = int(input("escribe el primer número:"))
    valor_2 = int(input("escribe el segundo número:"))
    valor_3 = int(input("escribe el tercer número:"))
    print(valor_1+valor_2+valor_3)

#6 - Crea un programa que solicite dos valores numéricos al usuario y 
# luego imprima la resta del primero menos el segundo valor.

def ejercicio_6():
    valor_1 = int(input("escribe el primer número:"))
    valor_2 = int(input("escribe el segundo número:"))
    print(valor_1-valor_2)

#7 - Crea un programa que solicite dos valores numéricos al usuario y 
# luego imprima la multiplicación de los dos valores.

def ejercicio_7():
    valor_1 = int(input("escribe el primer número:"))
    valor_2 = int(input("escribe el segundo número:"))   
    print(valor_1*valor_2)

#8 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador,
#  y realice la división entre los dos valores. 
# Asegúrate de que el valor del denominador no sea igual a 0.

def ejercicio_8():
    valor_1 = int(input("escribe numerador:"))
    valor_2 = int(input("escribe denominador:"))   
    print(valor_1/valor_2)

#9 - Crea un programa que solicite dos valores numéricos, un operador y una potencia, 
# y realice la exponenciación entre estos dos valores.

def ejercicio_9():
    valor_1 = int(input("escribe la base:"))
    valor_2 = int(input("escribe el exponente:"))   
    print(valor_1**valor_2)

#10 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, 
# y realice la división entera entre los dos valores. 
# Asegúrate de que el valor del denominador no sea igual a 0.

def ejercicio_10():
    valor_1 = int(input("escribe el numerador:"))
    valor_2 = int(input("escribe el denominador:"))
    print(valor_1%valor_2)











