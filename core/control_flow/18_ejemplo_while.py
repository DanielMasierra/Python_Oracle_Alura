"""count = 0

while(count < 10):
    count = count + 1
    if count == 5: 
        print (count)
        break
    print(count)"""

count = 0
while(count < 10):
    count = count + 1
    if count == 5: 
        continue
    print(count)

#importante: para salir del bucle, poner un límite, en teste caso es el +1. Hasta llegar a 10. 