import numpy as np

# numeros = [10, 20, 30, 40]
# print(numeros)
# arreglo = np.array(numeros)

# print(arreglo)
# print(type(arreglo))

# # operaciones vectorizadas
# lista_normal = [1,2,3,4,5]
# arreglo_numpy = np.array([1,2,3,4,5])
# print(lista_normal*2)
# print(arreglo_numpy * 2)

"""
ejercico guiado

1. crear un array llamado precios
2. introducir 5 precios de productos
3. aplicar 15% de descuento a todos a la vez (multiplicar por 0.85)
4. redondear el resultado a 2 decimales
"""

# precios = [29,51,33,150,548]
# precios_arreglo = np.array(precios)
# print(np.round(precios_arreglo * 0.85, 2))

# #indexing, slicing, funciones estadisticas

# temperaturas = np.array([25.9, 40.5, 15.7, 60.2, 32.2, 27.6, 24.3])

# #slicing
# print(temperaturas[0])
# print(temperaturas[-1])
# print(temperaturas[2:5])

# #promedio
# print("promedio:", np.mean(temperaturas))

# print("maxima:", np.max(temperaturas))
# print("minimo:", np.min(temperaturas))
# print("sumar:", np.sum(temperaturas))


# #distancia 
# print("desviacion estadar:", round(np.std(temperaturas), 2) )

"""
1. crear mi propio array, llamarlo temperaturas_semana
2. introducir 7 valores
3. imprimir el promedio, las max, la min, y la desviacion estandar
4. redondear todo los resultados a 1 decimal

"""
temperaturas_semana = np.array([32.6, 28.5, 26.9, 30.2, 29.3, 31.8, 27.7])

print("temperatura maxima:", round(np.max(temperaturas_semana), 1))
print("temperatura minima:", round(np.min(temperaturas_semana), 1))
print("Promedio de temperaturas:", round(np.mean(temperaturas_semana), 1))
print("La desviacion estandar es:", round(np.std(temperaturas_semana), 1))

#arrays de 2 dimensiones

matriz = np.array([
    [90,85,78],
    [70,88,92],

])

print(matriz)
#cantidad de filas y columnas
print(matriz.shape)
print(matriz[0])
#fila y objeto
print(matriz[1,2])

#calcular promedio por fila, axis= 1
print(np.mean(matriz, axis=1))
#por columna, axis= 0
print(np.mean(matriz, axis=0))

"""
sacar el promedio de cada mes entre todas las sucursales utilizando la matriz ventas

"""

ventas = np.array([
    [1220, 1500, 1350],
    [980,1300,1050],
    [1600,1440,1700],

])

print("Promedio por sucursal:", np.mean(ventas, axis=1))
print("promedio por mes:", np.mean(ventas, axis=0))

print(import(ventas))