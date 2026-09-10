import pandas as pd

df = pd.read_csv("titanic.csv")

# print(df.shape)
# print(list(df.columns))

# #visualizar filas de mi df
# print(df.head(3))

# #imprimir solo la columna name utilizando .head 3
# print(df["Name"].head(3))

# #seleccionar y filtrar
subset = df[["Name", "Age", "Survived"]]
print(subset.head(3))

# #filtrar con una condicion
# mayores_30 = df[df["Age"] > 30]
# print(mayores_30.shape)

# mujeres = df[df["Sex"] == "female"]
# print(mujeres.shape)

# #combinar condiciones y contar valores
# mujeres_sobrevivientes = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
# print(mujeres_sobrevivientes.shape)
# #cuantas veces aparece un valor disitnto en cada columna- vaule counts 
# print(df["Survived"].value_counts())


# #ejemplo de concepto de "series" columna de datos, un indice especifico
# precios = pd.Series([25.99, 40.50, 15.75, 60.00])
# print(precios)
# print(type(precios))


# #emjemplo de dataframe
# productos = pd.DataFrame({
#     "nombre": ["audifonos", "mouse", "teclado"],
#     "precio": [45.99, 15.50, 40.00],
#     "stock": [120, 80, 45]

# })

# print(productos)

# """
# EJERCICIO GUIADO
# 1. crear un dataframe llamado estudiantes
# 2. incluir 3 columnas con la llave: nombre, edad, curso. (4 personas)
# 3. imprimir el dataframe

# """
# estudiantes = pd.DataFrame({
#     "nombre": ["Jenifer", "Andres", "Luis", "Susan"],
#     "edad": [25, 23, 19, 22],
#     "curso": ["cocina", "programacion", "historia", "arte"]

# })

# print(estudiantes)

import numpy as np

# #eliminar valores de filas vacias
# edades = df["Age"].dropna()

# #crear array de numpy con una serie de pandas
# edades_array = edades.to_numpy()

# print(type(edades_array))

# #formulaas utilizadas en nunmpy para calcular
# print("Promedio de edaddes:", round(np.mean(edades_array), 1))
# print("Edad maxima:", np.max(edades_array))
# print("Edad minima:", np.min(edades_array))
# print("Desviacion estandar:", round(np.std(edades_array), 1))

"""
ejercicio guiado
1. filtrar el dataframe para quedarse solor con los pasajeros de la columna Pclass
2. guardar en una variable nueva e imprimia cuantas filas tiene
3. despues utilizara el metodo .value_counts() para la columna Pclass del dataframe original

objetivo : visualzar cuantos pasajeros hay en cada clase
comparar con el 1
"""

pasajeros_primera_clase = df[df["Pclass"] == 1]
print(pasajeros_primera_clase.shape)
print(df["Pclass"].value_counts())
