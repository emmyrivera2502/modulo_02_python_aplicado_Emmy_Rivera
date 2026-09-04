# # Variables y tipos de datos

# #VARIABLES
# #string (texto)
# nombre = "Natasha"

# # integer (entero)
# edad = 30

# # float (decimal)
# altura = 1.63

# # boolean (booleano)
# es_estudiante = True

# print(nombre)
# print(edad)
# print(altura)
# print(es_estudiante)

# print(type(nombre), type(edad), type(altura), type(es_estudiante))


# nombre = "Vanessa"
# edad = 25
# cuanto_dinero_tiene = 658.93
# tiene_mucho_dinero = False

# print(nombre)
# print(edad)
# print(cuanto_dinero_tiene)
# print(tiene_mucho_dinero)

# print(type(nombre), type(edad), type(cuanto_dinero_tiene), type(tiene_mucho_dinero))

nombre = input("como te llamas?")
edad = int(input("cuantos años tienes?"))

print(f"Hola, {nombre}. el año que viene tendras {edad + 1} años")  

"""
pidale a su compañero que ingrese su temperatura en grados celsius.
convertir a numero y mostrar el resultado en grados fahrenheit.

la formula: 'fahrenheit = (celsius * 9/5) + 32'

"""
temperatura_en_celcius = float(input("cual es tu temperatura en grados celsius?"))
temperatura_en_farenheit = float((temperatura_en_celcius * 9/5) + 32)
temperatura_en_farenheit_entero = int(temperatura_en_farenheit)
print(f"tu temperatura en grados fahrenheit es: {temperatura_en_farenheit_entero}°F")

#condicionales

temperatura_corporal = 36.7
if temperatura_corporal >= 38:
     print("temperatura alta")
if temperatura_corporal <= 32:
    print("temperatura baja")
else:
    print("temperatura normal")

#ejercicio integrador de conceptos

edades = [55, 27, 28, 17, 30]
for edad in edades:
   if edad >= 55:
      print(f"{edad} años: persona alduta")
   elif edad >= 30:
      print(f"{edad} años: persona promedio")
   else:
      print(f"{edad} años: persona joven")