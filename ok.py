"""
# pidale a su compañero que ingrese su temperatura en grados celsius.
# convertir a numero y mostrar el resultado en grados fahrenheit.

# la formula: 'fahrenheit = (celsius * 9/5) + 32'

"""
temperatura_en_celcius = float(input("cual es tu temperatura en grados celsius?"))
temperatura_en_farenheit = float((temperatura_en_celcius * 9/5) + 32)
temperatura_en_farenheit_entero = int(temperatura_en_farenheit)
print(f"tu temperatura en grados fahrenheit es: {temperatura_en_farenheit_entero}°F")

