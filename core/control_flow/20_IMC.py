#Anna Júlia está creando un sistema para calcular el Índice de Masa Corporal (IMC) 
# y proporcionar recomendaciones básicas. El programa debe recibir el peso 
# y la altura de una persona y mostrar el valor del IMC, además de 
# indicar si está por debajo del peso, con peso normal o por encima del peso. 
# Crea un programa que reciba el peso (en kg) y la altura (en metros) y 
# calcule el IMC usando la fórmula: IMC = peso / (altura ** 2)
# Luego, muestra el valor del IMC y un mensaje indicando si está por 
# debajo del peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) o por encima del peso (IMC >= 25).

Peso = float(input('Digite su peso (kg): ')) 
Altura = float(input('Digite su altura (m): '))

IMC = Peso / (Altura **2)
if IMC < 18.5:
    print(f'Tiene un IMC de: {IMC}. Está por debajo del peso normal')
elif 18.5 <= IMC <25:
    print(f'Tiene un IMC de: {IMC} Tienes un peso normal')
else:
    print (f'Tiene un IMC de: {IMC}. Está por encima del peso normal')
