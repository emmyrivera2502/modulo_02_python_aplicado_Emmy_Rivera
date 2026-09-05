import numpy as np
import pandas as pd

df = pd.read_csv("titanic.csv")
print(df.shape)

#buscar valores nulos
print(df.isnull().sum())

#cuando una columna tiene demasiados nulos es mejor eliminarla
#eliminar una columna completa
df = df.drop(columns=["Cabin"])

#calcular la mediana de la columna Age porque es la segunda con mas nulos
edad_mediana = df["Age"].median()
df["Age"] = df["Age"].fillna(edad_mediana)

#eliminar filas vacias dentro de la columna embarked
df = df.dropna(subset= ["Embarked"])

print(df.shape)
print(df.isnull().sum().sum())

"""
ejercicio guiado
1. imprimir la cantidad de columnas que tenemos
2. confirmar que la columna age ya no tiene nulos

"""
print(list(df.columns))
print(df["Age"].isnull().sum)

#crear columnas nuevas a travez de feature engineering
df["FamiliaTotal"] = df["SibSp"] + df["Parch"] + 1
print(df[["SibSp", "Parch", "FamiliaTotal"]].head())

#crear columna para evaluar valores booleanos (true/false)
df["EsMenorDeEdad"] = df["Age"] < 18
print(df["EsMenorDeEdad"].value_counts())

# identificar tipos de datos y ordenarlos
print(df.dtypes)

#cambiar tipo de datos de una columna
df["Survived"] = df["Survived"].astype(bool)
print(df["Survived"].dtype)
print(df["Survived"].head(3))

#ordenar el dataset
df_por_edad = df.sort_values("Age", ascending= True)
print(df_por_edad[["Name", "Age"]].head(3))

#agrupar el dataset
#groupby calcucar segun una categorio
promedio_edad_por_clase = df.groupby("Pclass")["Age"].mean()
print(promedio_edad_por_clase)

promedio_edad_por_clase = df.groupby("Pclass")["Survived"].mean()
print(promedio_edad_por_clase.round(3))

#guardar el nuevo dataset que hicimoa
df.to_csv("titanic limpio.csv", index=False)

