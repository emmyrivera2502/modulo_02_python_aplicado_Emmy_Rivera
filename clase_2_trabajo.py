""" 
calcular cuantas vueltas 'completas' se pueden correr con esta distancia y cuantos metros sobrarian despues de esas vueltas completas

necesito almacenar las vueltas completas y los metros sobrantes.

mostrar resultado
"""

distancia = 1500 
vueltas_completas = 400

vueltas_completas_que_se_pueden_correr = distancia // vueltas_completas
metros_que_sobran = distancia % vueltas_completas

print(vueltas_completas_que_se_pueden_correr)
print(metros_que_sobran)

