#Laura está desarrollando un sistema para saber si una persona tiene derecho a recibir un beneficio social. 
# Para eso, la persona debe cumplir las siguientes condiciones:
# Tener ingresos menores o iguales a $2,000.
# Tener al menos un hijo o hija.
# Crea un programa que reciba los ingresos mensuales y la cantidad de hijos de una persona, 
# y diga si tiene derecho al beneficio.


Ingresos = float(input('Digite la cantidad de dinero que representa sus ingresos mensuales: '))
hijos = int(input('¿Cuántos hijos tiene?: '))

if Ingresos <= 2000.00 and hijos >= 1:
    print ('Tiene derecho al beneficio social')
else: 
    print('No tiene derecho al beneficio social')