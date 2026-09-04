frutas = ["manzana", "banana", "fresa", "naranja", "pera", "uva"]

#agregar a la lista
frutas.append("mango")
print(frutas)

#eliminar de la lista
frutas.remove("banana")
print(frutas)

frutas.insert(1, "toronja")
print(frutas)

print(frutas)
print(frutas[-2])
print(frutas[0:3])
print(len(frutas))

numeros = [10, 20, 30, 40, 50]

print(numeros[:2])
print(numeros[2:])
print(numeros[::2])

#Ejercicio guiado

temperaturas = [22, 25, 20, 32, 19, 27, 24]
print("Primeras 3:", temperaturas[:3])
print("ultimo:", temperaturas[-1])
temp_max = max(temperaturas)
temp_min = min(temperaturas)
print("la maxima seria:", temp_max, "la minima seria:", temp_min)

#organizar la lista de menor a mayor
numeros_desordenados = [5, 2, 7, 1, 8]
numeros_desordenados.sort()
orden = sorted(numeros_desordenados, reverse=True)

print(numeros_desordenados)


#ejercicio guiado 2
tareas = ["estudiar", "hacer ejercicio"]
tareas.append("leer")

#agregar el elemento cocinar en la primera posicion de la lista
tareas.insert(1, "cocinar")

#eliminar el elemento "hacer ejercicio"
tareas.remove("hacer ejercicio")

print(tareas)

#preguntar si el elemento eestudiar existe
print("estudiar" in tareas)

#listas aisladas
tablero = [
    ["x", "o", "x"],
    ["o","x", "o"],
    ["x", "o", "x"]
]

print(tablero [0])
print(tablero[0][1])
print(tablero[2][2])

#ejercicio guiado

notas_estudiantes =[
    ["Esther", 85, 90, 78],
    ["Erick", 60, 70, 65],
]

for estudiante in notas_estudiantes:
    nombre = estudiante[0]
    notas = estudiante[1:]
    promedio = sum(notas) / len(notas)
print(f"{nombre}: promedio {round(promedio, 1)}")

#tuplas- no modificar el valor 
coordenada = (19.78, -70.69)
print(coordenada)
print(coordenada[0], coordenada[1])
print(type(coordenada))

#ejercicio guiado
"""
calculen la distancia entre ambos puntos utilizando la formula para calcular distancia

pista: para calcular distancia utilice esta formula: 
raiz cuadrada((x2-x1)2 + (y2-y1)2)

nota: para calcular la raiz cuadrada es **0.5
"""

punto_a = (0, 0)
punto_b = (3, 4)

distancia = ((punto_b[0] - punto_a[1])**2 + (punto_b[1] - punto_a[1])**2)**0.5
print("la distancia entre el punto a y el punto b es:", distancia)
