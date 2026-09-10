#Proyecto final mes 2

import pandas as pd
df = pd.read_csv("hollywood.csv")


print("Trabajo final Emmy Rivera")
print("-----------")

#1. CARGAR Y DIAGNOSTICAR
print("Primera etapa, cargar y diagnosticar")

#Modificar el DT para quedarnos con las columnas que queremos
df = df[["Movie", "LeadStudio", "Genre", "RottenTomatoes", "AudienceScore", "WorldGross", "Budget", "Year"]]

#ver cuantas filas y columnas tiene el dt
print("La cantidad de filas y columnas son:", df.shape)


#ahora revisamos cuantos valores nulos tiene
print("Los valores nulos son:", df.isnull().sum())

print("-----------")

#2. LIMPIAR
print("Segunda etapa, limpiar")

#rellenar valores nulos: Genre y LeadStudio
df["Genre"] = df["Genre"].fillna("others")
df["LeadStudio"] = df["LeadStudio"].fillna("extra studios")

#rellenar Rottentomatoes y audiencescore (columnas numericas)
mediana_de_RottenTomatoes = df["RottenTomatoes"].median()
df["RottenTomatoes"] = df["RottenTomatoes"].fillna(mediana_de_RottenTomatoes)

mediana_audiencescore = df["AudienceScore"].median()
df["AudienceScore"] = df["AudienceScore"].fillna(mediana_audiencescore)

#eliminar valores nulos de worldgross y budget
df = df.dropna(subset=["WorldGross"])
df = df.dropna(subset=["Budget"])
print("Los valores nulos de WorldGross y Budget se han eliminado")
print("------")
#verificar
print(df.isnull().sum())
print("La nueva cantidad de filas y columnas es:", df.shape)
print("-----------")

#3. CREAR COLUMNAS NUEVAS
print("Etapa 3, crear columnas nuevas")

#Crear las columnas "Ganancia" y "Exitosa"
df["Ganancia"] = df["WorldGross"] - df["Budget"]
print("Se añadio una nueva columna: Ganancia")
print("-------")
#El parametro de si la pelicula es exitosa es si tiene una puntuacion de 60 o mas en RottenTomatoes
df["Exitosa"] = df["RottenTomatoes"] >= 60
print("Se añadio una nueva columna: Exitosa")
#Contabilizar
print(df["Exitosa"].value_counts())
print("------")

#4. TIPOS DE DATOS Y ORDENAR
print("Etapa 4, tipos de datos y ordenar")

#revisar si la columna Exitosa se guardo como tipo booleano
print(df.dtypes)
print("La columna 'Exitosa' es:", df.dtypes["Exitosa"])
print("-----")

#Ordenar en dt por Ganancia de mayor a menor, imprimir el nombre y la ganancia de las 3 peliculas mas rentables.
df_por_ganancias = df.sort_values("Ganancia", ascending= False)
print("--Este es el top 3 de peliculas con mayores ganancias:--")
print(df_por_ganancias[["Movie", "Ganancia"]].head(3))
print("------")

#5. AGRUPAR Y ANALIZAR
print("--Quinta fase, agrupar y analizar--")

#Agrupar el dataset por Genre, calcular promedio de RottenTomatoes de cada genero, redondeado a 1 decimal
dt_agrupado_porGenre = round(df.groupby(by= "Genre") ["RottenTomatoes"].mean(), 1)
print("--Este es el dataset agrupado por Genre--")
print(dt_agrupado_porGenre)
print("-----")

#Agrupar por LeadStudio, calculando el promedio de Ganancia redondeando a 1 decimal
dt_por_LeadStudio = round(df.groupby(by="LeadStudio") ["Ganancia"].mean(), 1)
print("--Este es el dataset agrupado por LeadStudio--")
print(dt_por_LeadStudio)
print("----")

#6. GUARDAR EL RESULTADO
print("--Sexta y ultima etapa: Guardar el resultado--")

print("El nuevo csv fue guardado")
df.to_csv("Hollywood_limpio.csv", index=False)

#Confirmar que todo este correcto
print("--Confirmacion--")
df_nuevo = pd.read_csv("Hollywood_limpio.csv")
print("La cantidad de filas y columnas son:", df_nuevo.shape)

print("--La cantidad de nulos son:--")
print(df_nuevo.isnull().sum())
