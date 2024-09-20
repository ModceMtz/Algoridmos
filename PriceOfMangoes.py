'''
Calcula el costo total de los mangos cuando hay una oferta de "3 por 2"
'''
def total_cost(quantity, price_per_mango):
    # Grupos de 3 mangos
    groups_of_three = quantity // 3
    # Mangos adicionales que no entran en la promoción
    remaining_mangoes = quantity % 3
    # Costo total: pagas 2 mangos por cada grupo de 3, más los mangos restantes
    total = (groups_of_three * 2 * price_per_mango) + (remaining_mangoes * price_per_mango)
    return total

# Ejemplo de uso
quantity = 7  # número de mangos
price_per_mango = 5  # precio por mango
cost = total_cost(quantity, price_per_mango)
print(f"El costo total es: {cost}")
