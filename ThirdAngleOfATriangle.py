'''
Calcula el tercer ángulo de un triángulo
'''
def find_third_angle(angle1, angle2):
    return 180 - (angle1 + angle2)

# Ejemplos de uso
print(find_third_angle(60, 60))  # 60
print(find_third_angle(45, 45))  # 90
