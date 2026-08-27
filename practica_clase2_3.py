# Practica bucles, funciones y estructuras de datos


#Bucle for
print("Bucle for")

print("parte A")
horas_estudio_pordia = [2, 3, 1, 4, 2, 5, 3]
total = 0
for h in horas_estudio_pordia:
    total += h

promedio = total / len(horas_estudio_pordia)
print("Total de horas :" , total)
print("Promedio dirario:", round(promedio, 1))
print("---------")
#parte b
print("Parte B")
contador = 0
for h in horas_estudio_pordia:
    if h >= 3:
        contador +=1

print("Dias con 3 horas o mas:", contador)
print("--------")

#Bulce while
print("bucle while")
ahorro = 0
semanas = 0

while ahorro < 300:
    ahorro += 60
    semanas += 1

print("semanas necesarias:", semanas)
print("ahorro final:", ahorro)
print("---------")

#Funciones
print("funciones")
print("parte A")

def calcular_costo_envio(peso, distancia):
    costo_de_envio = (peso * 0.5 + distancia*0.1)
    return costo_de_envio

resultado = calcular_costo_envio(12 , 80)
print(f"El costo de su paquete es: {round(resultado, 2)}" )
print("------")

print("Parte B")
def clasificar_envio(costo):
    if costo < 10:
        return("Economico")
    elif costo < 25:
        return("Estandar")
    else:
        return("Premium")

print(clasificar_envio(resultado))
print("------")

#listas: creacion, acceso y slicing
print("listas: creacion, acceso y slicing")

peliculas = ["Megamente", "Truman Show", "Barbie", "Avatar", "Avengers Endgame", "Spiderman"]
print(peliculas)
print(peliculas [0])
print(peliculas [-1])
print(peliculas [:3])
print(len(peliculas))
print("------")

print("parte B")
print(peliculas[::2])
print(peliculas[1:4])
print(peliculas[2:])