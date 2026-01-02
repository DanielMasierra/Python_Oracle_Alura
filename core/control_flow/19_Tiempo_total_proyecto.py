"""
Camila está organizando un proyecto y necesita calcular el tiempo total 
necesario para concluir tres actividades: A, B y C. 
Sin embargo, si alguna actividad tiene un número de días negativo, 
el código debe avisar que los valores ingresados son inválidos y no calcular el total.
Escribe un programa que reciba el número de días de tres actividades y 
muestre el tiempo total del proyecto. Si algún valor es negativo, 
muestra un mensaje informando el error."""

actividad_a = int(input('Informe los días para la actividad A: '))
actividad_b = int(input('Informe los días para la actividad B: '))
actividad_c = int(input('Informe los días para la actividad C: '))

if actividad_a < 0: 
    print('Error: los días no pueden ser negativos')
elif actividad_b < 0:
    print('Error: los días no pueden ser negativos')
elif actividad_c < 0: 
    print('Error: los días no pueden ser negativos')
else:
    print(f'Quedan {(actividad_a + actividad_b + actividad_c)} días para finalizar el proyecto')