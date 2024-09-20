'''
Convierte dólares estadounidenses (USD) a yuanes chinos (CNY)
'''
def usd_to_cny(usd_amount):
    conversion_rate = 6.75  # Tasa de conversión de USD a CNY
    cny_amount = usd_amount * conversion_rate
    return f"{cny_amount:.2f} Chinese Yuan"

# Ejemplos de uso
print(usd_to_cny(15))   # '101.25 Chinese Yuan'
print(usd_to_cny(465))  # '3138.75 Chinese Yuan'
