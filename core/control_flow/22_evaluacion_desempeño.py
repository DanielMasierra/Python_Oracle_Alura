#Una empresa evalúa a sus empleados con base en dos criterios:

#Puntuación de desempeño (de 0 a 10)
# Años trabajados

#Reglas:

#Si la puntuación es mayor o igual a 7:
    #Si trabajó más de 5 años: "Elegible para ascenso"
    #Si trabajó 5 años o menos: "Buen desempeño, sigue así"
#Si la puntuación es menor a 7: "Necesita mejorar"

#Crea un programa que reciba la puntuación y los años trabajados, y muestre el mensaje adecuado.

Puntuación = float(input('Ingrese su puntuación de desempeño: '))
Anos_trabajados = float(input('Ingrese la cantidad de años trabajados: '))

if Puntuación >= 7 and Anos_trabajados > 5: 
    print("Elegible para ascenso")
elif Puntuación >= 7 and Anos_trabajados < 5: 
    print("Buen desempeño, sigue así")
else: 
    print("Necesita mejorar")