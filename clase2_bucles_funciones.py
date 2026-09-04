#Bucle for
edades = [24, 31, 19, 45, 27]

suma = 0

for edad in edades:
    suma += edad 

print("suma total:", suma)
print("promedio:", suma / len(edades))

"""
ejercicio: con la misma lista que utilizamos "edades" contar cuantas edades son mayores o iguales a 30, utilizar el bucle for y una variable 
contadora. 
variable contadora: es una variable que empieza en 0 y le suma 1 cada vez que se cumple la condicion. ejemplo contador += 1

pista: necesitar combinar lo que vimos ahora con el bucle for con lo que ustedes apredieron en la clase pasada "condicionales"

"""

edades = [24, 31, 19, 45, 27]

contador = 0
for edad in edades:
    if edad >= 30:
        contador += 1

print("Total de edades mayores o igual a 30:" , contador)

#bucle while
contador = 1
while contador <= 5:
    print("vuelta - numero" , contador)
    contador += 1

"""
utilicen "while", hagan una cuenta regresiva desde 5 hasta 1 y al final impriman "Iniciamos"

"""
numero = 5
while numero >= 1:
    print(numero)
    numero -= 1
print("Iniciamos")

#funciones
def calcular_indice_de_masa_corporal(peso, altura):
    imc = peso / (altura ** 2)
    return imc 

resultado = calcular_indice_de_masa_corporal(74 , 1.78) 
print(f"IMC: {round(resultado, 2)}")


"""
escribir una funcion y llamarla "clasificar_imc(imc)" que reciba un imc y devuelva un texto: "bajo de peso" si es menor a 18.5.
peso normal si esta esta en 18.5 y 25. sobrepeso si esta entre 25 y 30. obesidad si es de 30 o mas. despues, llamar el resultado de la
funcion anterior. 
imprimir con la palabra resultado.
"""

def clasificar_imc(imc):
    if imc < 18.5:
        return("bajo peso")
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    else:
        return "obesidad"

print(clasificar_imc(resultado))

#variables, tipos de datos, operadores, condicionales, bucles, funciones, listas
    




