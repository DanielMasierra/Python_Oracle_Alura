"""
João está desarrollando un sistema de registro para un sitio de lectura. 
Necesita asegurarse de que los usuarios ingresen un nombre de usuario y 
una contraseña válidos. Las reglas son las siguientes:

El nombre de usuario debe tener al menos 5 caracteres.
La contraseña debe tener al menos 8 caracteres.
João quiere que el sistema siga solicitando la información 
hasta que ambas condiciones se cumplan. Cuando el usuario ingresa datos válidos, 
el programa debe mostrar el mensaje: "¡Registro realizado con éxito!".

Crea un programa que implemente esta lógica usando un bucle while.


"""



"""
while len(usuario) < 5 and len(contraseña) < 8:
    print('El nombre de usuario debe contener al menos 5 caracteres')
else:
"""    

while True: 
    usuario = input('Digite su usuario: ')
    contraseña = input('Digite su contraseña: ')

    if len(usuario) < 5:
        print('Tu usuario debe contener al menos 5 caracteres')
        continue

    if len(contraseña) < 8:
        print('Tu contraseña debe contener al menos 8 caracteres')
        continue
    
    print('Registro realizado con éxito')
    break


#En este ejercicio, el "while True" da la indicación de que se repita indefinidamente hasta
#que establezca el break. Ese la forma por default para este tipo de programas. 