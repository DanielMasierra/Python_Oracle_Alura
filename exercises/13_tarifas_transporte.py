"""Un sistema de transporte cobra según la edad del pasajero y la distancia recorrida:

Menores de 6 años: Viajan gratis.
De 6 a 18 años:
Hasta 20 km: $1.50
Más de 20 km: $2.50
Mayores de 18:
Hasta 20 km: $2.50
Más de 20 km: $4.00

Crea un programa que reciba la edad y distancia, y muestre el valor a pagar."""

Edad = int(input('Ingrese su edad: '))


if Edad < 6: 
    print("Viaja gratis")
elif Edad <= 18: 
    Distancia = int(input('Ingrese la distancia recorrida: '))
    if Distancia <= 20: 
        print('Valor del pasaje: $1.50')
    else: 
        print('Valor del pasaje: $2.50')
else: 
    Distancia = int(input('Ingrese la distancia recorrida: '))
    if Distancia <= 20: 
        print("Valor del pasaje: $2.50")
    else: 
        print("Valor del pasaje $4.50")

#En este ejercicio, se optó por poner la var distancia despues de
#solicitar la edad. La intención es no pedir datos si no se requieren, ej. si ingresan que son menores de 6 años y despues
#piden la distancia que se recorrerá.

