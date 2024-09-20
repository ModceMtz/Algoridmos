'''
Calcula un rango de edad apropiado para citas
'''
import math


def dating_age_range(age):
    if age > 14:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplos de uso
print(dating_age_range(27))  # 20-40
print(dating_age_range(5))  # 4-5
print(dating_age_range(17))  # 15-20
