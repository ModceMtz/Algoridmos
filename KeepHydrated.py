'''
Calcula la cantidad de agua que Nathan beberá durante su tiempo en bicicleta
'''

import math

def litres(time):
    # Calculamos la cantidad de litros y usamos math.floor para redondear hacia abajo
    return math.floor(time * 0.5)

# Ejemplos de prueba
print(litres(3))   # 3 horas -> 1.5 litros -> redondeado a 1 litro
print(litres(6.7)) # 6.7 horas -> 3.35 litros -> redondeado a 3 litros
print(litres(11.8)) # 11.8 horas -> 5.9 litros -> redondeado a 5 litros
