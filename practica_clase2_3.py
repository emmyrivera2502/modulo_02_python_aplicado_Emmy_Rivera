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
print("-------")

#metodo de listas
print("metodo de listas")

carrito = ["pantalon" , "camisa"]
carrito.append("zapatos")
print(carrito)
carrito.insert(1, "cinturon")
print(carrito)
carrito.remove("pantalon")
print(carrito)
print("camisa" in carrito)
carrito.sort()
print(carrito)

print("---------")

#Listas aniadas
print("listas aniadas")
print("parte A")

asientos = [
    ["L", "L", "X"],
    ["X", "L", "X"],
    ["L", "X", "X"],

    ]

print(asientos[0])
print(asientos[1][2])
for fila in asientos:
    print(fila)
print("------")
#parte b
print("parte b")

ventas_vendedores = [
    ["Vendedor 1", 80, 167, 539],
    ["vendedor 2", 78, 678, 342],

]

for vendedor in ventas_vendedores:
    nombre = vendedor[0]
    ventas = vendedor[1:]
    total = sum(ventas)

    print(f"{nombre}: total de ventas ${total}")
print("-------")
#tuplas
print("tuplas")
print("parte a")

color = (120, 200, 50)
print(color)
print(color[0], color[1], color[2])
print(type(color))
print("---------")
print("parte b")

def calcular_brillo(c):
    return sum(c) / 3

color_a= (120, 200, 50)
color_b= (10,10,10)

brillo_a = calcular_brillo(color_a)
brillo_b = calcular_brillo(color_b)
print(f"Brillo A: {round(brillo_a, 2)}")
print(f"Brillo B: {round(brillo_b, 2)}")

if brillo_a >brillo_b:
    print("El color A es mas brillante")
else:
    print("El color B es mas brillante")


print("-------")

print("torneo de trivia por equipos")

equipos = [
    ["Los Lakers", 35, 90, 22],
    ["Boston Celtics", 47, 17, 68],
    ["Knicks", 71, 86, 10]
]


def clasificar_equipo(total):
    if total >= 60:
        return("Campeon")
    elif total >= 40:
        return("Finalista")
    else:
        return("Principiante")

total = sum(equipos[0])
clasificacion_de_cada_equipo = clasificar_equipo(equipos)
print(clasificacion_de_cada_equipo)