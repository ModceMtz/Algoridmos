'''
Predice el rendimiento de los jugadores de baloncesto en la NBA
'''
def nba_extrap(ppg, mpg):
    if mpg == 0:  # Si no ha jugado minutos, entonces no puede extrapolarse
        return 0
    # Extrapolar puntos por 48 minutos
    ppg_per_48 = (ppg / mpg) * 48
    # Redondear a la décima más cercana
    return round(ppg_per_48, 1)

# Ejemplos de uso
print(nba_extrap(12, 20))  # 28.8
print(nba_extrap(10, 10))  # 48
print(nba_extrap(5, 17))   # 14.1
print(nba_extrap(0, 0))    # 0
