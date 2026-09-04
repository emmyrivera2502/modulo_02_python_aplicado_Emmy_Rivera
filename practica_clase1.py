#Practica 1

# VARIABLES Y TIPO DE DATOS

print("Variables y tipos de datos")
producto = "pantalones"
precio = 1699.99
en_oferta = False
cantidad_en_stock = 35

print(producto)
print(precio)
print(en_oferta)
print(cantidad_en_stock)

print(type(producto), type(precio), type(en_oferta), type(cantidad_en_stock))

print("------------------")
#OPERADORES
# PARTE A: una compra cuesta 18.75 el cliente paga con un billete de 20. Calcula e imprime el vuelto exacto.
print("operadores parte A")
el_cliente_paga = 20
el_precio = 18.75
el_vuelto = el_cliente_paga - el_precio
print(f"el vuelto es: {el_vuelto}")
print("------------------")


# PARTE B: un cajero tiene que dar 37 dolares en cambio, usando la menor cantidad de billetes de 10. Calcula cuantos
#billetes de 10 completos puede dar, y cuanto sobre en billetes mas pequenos.
print ("operadores parte B")
cambio_total = 37
billetes_de_10 = cambio_total // 10
sobrante = cambio_total % 10
print(f"billetes de 10 completos: {billetes_de_10}")
print(f"sobrante: {sobrante}")
print("------------------")

#Entrada y salido
print("entrada y salida")

tu_altura = float(input("cual es tu altura en metros?"))
altura_de_tu_hermano = float(input("cual es la altura de tu hermano en metros?"))

su_altura_combiada = tu_altura + altura_de_tu_hermano
print(f"la altura combinada es: {su_altura_combiada}")
print("------------------")

#CONDICIONALES
print("condicionales")

nota = 98

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else: 
    print("F")

print(f"si tu nota es {nota}, tu calficacion es {nota >= 90 and 'A' or nota >= 80 and 'B' or nota >= 70 and 'C' or nota >= 60 and 'D' or 'F'}")
print("------------------")

#EJERCICO INTEGRADOR
print("ejercicio integrador")

monto_de_compra = float(input("cual es el monto de su compra?"))

if monto_de_compra >= 200:
    print("tienes un 15% de desucuento con tu compra")
    descuento = monto_de_compra * 0.15
    monto_final = monto_de_compra - descuento
    print (f"el monto final de su compra es: {monto_final}")
    print(f"el monto original de su compra era: {monto_de_compra}")
elif monto_de_compra >= 100 and monto_de_compra <= 199:
    print("tienes un 10% de desucuento con tu compra")
    descuento = monto_de_compra * 0.10
    monto_final = monto_de_compra - descuento
    print (f"el monto final de su compra es: {monto_final}")
    print(f"el monto original de su compra era: {monto_de_compra}")
elif monto_de_compra <= 100:
    print("lo sentimos, no tienes descuento con tu compra")
    print (f"el monto final de su compra es: {monto_de_compra}")
print("------------------")

#CALCULADORA DE PROPINA INTELIGENTE
print("calculadora de propina inteligente")

cuenta_del_restaurante = float(input("cual es el monto de su cuenta en el restaurante?"))
cantidad_de_personas_en_mesa = int(input("cuantas personas hay en la mesa?"))

if cuenta_del_restaurante < 20:
    porcentaje = 0.10
elif cuenta_del_restaurante <= 50:
    porcentaje = 0.15
else:
    porcentaje = 0.20

if cantidad_de_personas_en_mesa > 4:
    porcentaje = porcentaje + 0.05

propina = cuenta_del_restaurante * porcentaje
total_a_pagar = cuenta_del_restaurante + propina
monto_por_persona = total_a_pagar / cantidad_de_personas_en_mesa

print(f"Propina: {propina}")
print(f"Total a pagar: {total_a_pagar}")
print(f"Cada persona paga: {monto_por_persona}")