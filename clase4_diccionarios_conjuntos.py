# #diccionarios

# estudiante = {"nombre": "Jefte", "edad": 55, "curso": "IA"}

# print(estudiante["nombre"])

# #modificar valores
# estudiante["edad"] = 35
# print(estudiante)

# #agregar informacion
# estudiante["ciudad"] = "Santo Domingo"
# print(estudiante)

# #eliminar info
# del estudiante["curso"]
# print(estudiante)

# #ejercicio
# """
# 1.  crear un diccionario llamado producto
# 2. las llaves (clave y valor) "nombre", precio y stock
# 3. agregar una nueva llave llamada categoria
# 4. modificar el precio de la llave precio agregando 10 al valor
# 5. eliminar la llave stock
# """

# producto = {"nombre": "Termo Owala", "precio":1500, "stock": 55 }
# print(producto)
# print("------")
# producto["categoria"] = "termo"
# print(producto)
# print("-------")
# producto["precio"] += 10
# print(producto)
# print("--------")
# del producto["stock"]
# print(producto)

# #metodos para trabajar con diccionarios
# print(estudiante.keys()) #devulve todas las llaves
# print(estudiante.values()) #devuelve todos los valores
# print(estudiante.items()) #devuelve cada par clave:valor en una tupla

# #acceder a un valor en el diccionario
# print(estudiante.get("stock")) #es mejor usar esta porque no para el programa. solo uestra none si no hay

# """
# EJERCICIO GUIADO

# utilicen este diccionario: 
# recorrer el diccionario con el metodo .items que me imprima para cada producto si es suficiente
# suficiente = 40 o mas
# pocas= menos de 40

# """
# inventario = {"manzana": 50, "peras": 30, "uvas": 80}

# for producto, cantidad in inventario.items():
#     if cantidad >= 40:
#         print(f"{producto} - suficiente {cantidad}")
#     else:
#         print(f"{producto} - pocas {cantidad}")

#conjuntos (set)- tranforma a un conjunto, no permite duplicados, el orden puede cambiar
frutas_emmy = {"manzana", "pera", "uva"}

litas_valores_repetidos = {"manzana", "pera", "uva", "manzana", "pera"}

nueva_lista = set(litas_valores_repetidos)
print(nueva_lista)

#operaciones entre conjuntos
#unificar conjuntos, 
frutas_emmy = {"manzana", "pera", "uva"}
frutas_mairon = {"banana", "uva", "pera"}

#une los dos diccionarios sin incluir los duplicados
print(frutas_emmy.union(frutas_mairon))

#delvueve los valores que se repiten
print(frutas_emmy.intersection(frutas_mairon))

#devuelve los valores que estan en el primer conjunto pero no en el segundo
print(frutas_emmy.difference(frutas_mairon))

"""
trabaja con esta lista

1. obtener cuantas respuestas hay que no se repiten
2. imprimir el numero junto con la lista de opciones distintas y ordenadas alfabeticamente

nota= transformar lista a set

"""

respuesta = ["python", "java", "python", "c++", "python", "java"]

lista_sin_repetidos =set(respuesta)

print("cantidad de respuestas distintas:", len(lista_sin_repetidos))
print("orden alfabetico:", sorted(lista_sin_repetidos))






