#Practica numpy
import numpy as np

#Arrays: creacion e idexado
print("Arrays: creacion e idexado")

"""
Crean un array calificaciones con 6 notas de examen.
Imprime la primera nota, la ultima, y las notas de la posicion 2 a la 5 (sin incluir la 5)
Imprime cuantas hay en total
"""
notas_examen = np.array([78,90,83,94,62,87])
print("La primera nota es:", notas_examen[0])
print("Las notas de la posicion 2 a la 5 son:", notas_examen[2:5])
print("El total de calificaciones es:", len(notas_examen))

print("------------")

#operaciones vectorizadas
print("Operaciones vectorizadas")

"""
crea un array comisiones con 4 montos de comision de ventas.
APlica un bono de 10% a todas a la vez, multiplica por 1.10, sin usar ningun bucle,
y redondea el resultado a 2 decimales.
"""

comisiones = np.array([247.99, 821.99, 113.67, 596.90])
print("Las comisiones mas el bono son:", np.round(comisiones*1.10, 2))
print("----------")

#Funciones estadisiticas
print("Funciones estadisiticas")

"""
Crea un array consumo_gb con el consumo de datos moviles (en GB) de 7 dias disitintos.
Imprime el promedio, el max, el min y la desviacion estandar, redondealos a 2 decimales.
"""
consumo_gb = np.array([1.5, 0.5, 2.2, 3.1, 1.2, 0.67, 5.8])

print("El promedio de GB es:", round(np.mean(consumo_gb),2))
print("El maximo de GB es:", (np.max(consumo_gb)))
print("EL minimo de GB es:", (np.min(consumo_gb)))
print("La desviacion estandar es:", round(np.std(consumo_gb), 2))
print("-----------")

#Arrays de 2 dimensiones
print("Arrays de 2 dimensiones")

"""
Con esta matriz, donde cada fila es un estudiante y cada columna es una semana de horas de estudio, calcula
el promedio de horas de cada estudiante en cada semana entre todos los estudiantes. 
"""
horas_estudio = np.array([
    [5, 8, 6, 7],
    [10, 9, 11, 8],
    [3, 4, 2, 5],
])

print(horas_estudio.shape)
print("Promedio por estudiante:", np.mean(horas_estudio, axis=1))
print("Promedio por semana:", np.mean(horas_estudio, axis=0))
print("---------")

#Desafio final: ventas semanales de 3 sucursales
print("Desafio final: ventas semanales de 3 sucursales")

"""
Con esta matriz:....
1. calcula el total de ventas de cada sucursal en la semana
2. una comision del 5% sobre el total de cada sucursal
3. el total de ventas combinadas de las 3 sucursales, por cada dia de la semana
"""
ventas = np.array([
    [1200, 1350, 980, 1420, 1100],
    [850, 920, 1050, 890, 960],
    [1600, 1750, 1580, 1690, 1720],
])

total_ventas_cada_sucursal = np.sum(ventas, axis=1)
print("Total de ventas por sucursal:", total_ventas_cada_sucursal)

comision_por_sucursal = total_ventas_cada_sucursal*0.05
print("Comision:", comision_por_sucursal)

total_ventas_pordia = np.sum(ventas, axis=0)
print("Totales por dia:", total_ventas_pordia)