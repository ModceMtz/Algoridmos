'''
Calcula la presión total ejercida por dos gases en un recipiente cerrado
'''
def total_pressure(M1, M2, m1, m2, V, T):
    # Convertir temperatura de °C a Kelvin
    T_kelvin = T + 273.15
    # Constante de gas
    R = 0.082  # dm^3 * atm * K^-1 * mol^-1
    # Calcular la presión total usando la fórmula dada
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V
    return P_total

# Ejemplo de uso
M1 = 44.01  # masa molar del primer gas en g/mol (por ejemplo, CO2)
M2 = 28.97  # masa molar del segundo gas en g/mol (por ejemplo, N2)
m1 = 10     # masa del primer gas presente en el recipiente en gramos
m2 = 5      # masa del segundo gas presente en el recipiente en gramos
V = 10      # volumen del recipiente en dm^3
T = 25      # temperatura en °C

# Calcular la presión total
Ptotal = total_pressure(M1, M2, m1, m2, V, T)
print(f"La presión total es: {Ptotal} atm")
