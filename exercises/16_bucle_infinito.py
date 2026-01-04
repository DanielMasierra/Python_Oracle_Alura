#André está probando una nueva función en el backend de Buscante que procesa datos en un bucle. 
# Durante las pruebas, se dio cuenta de que el sistema dejó de responder y sospecha 
# que el problema está en un bucle infinito.

"""contador = 0

while contador < 10:
    print("Procesando datos...")"""

#¿Cuál es el problema del código de André y cómo resolverlo?

contador = 0 
while (contador < 10): 
    print ("Procesando datos...")
    contador += 1
