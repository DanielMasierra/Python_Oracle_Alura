"""Ana está implementando un sistema de filtrado de libros en Buscante. 
La funcionalidad debe recorrer una lista de libros y mostrar el nombre de 
cada libro disponible en stock. Sin embargo, 
si el libro está agotado, debe ser ignorado durante la iteración.

libros = [
    {"nombre": "1984", "stock": 5},
    {"nombre": "Dom Casmurro", "stock": 0},
    {"nombre": "El Principito", "stock": 3},
    {"nombre": "El Hobbit", "stock": 0},
    {"nombre": "Orgullo y Prejuicio", "stock": 2}]

Crea un programa que ayude a Ana a mostrar solamente los libros que tienen stock disponible, 
en el formato: "Libro disponible: <nombre del libro>".

   
"""
libros = [
    {"nombre": "1984", "stock": 5},
    {"nombre": "Dom Casmurro", "stock": 0},
    {"nombre": "El Principito", "stock": 3},
    {"nombre": "El Hobbit", "stock": 0},
    {"nombre": "Orgullo y Prejuicio", "stock": 2}
]

for libro in libros:
    if libro["stock"] == 0:
        continue
    print(f'Libro disponible {libro["nombre"]}')

#Enseñanza: para acceder a una clave dentro de un diccionario, debe usarse [] y dentro la clave, en este caso
#"stock"
#Igual al momento del print, debe colocarse la clave a imprimir dentro de [], y siempre con f string