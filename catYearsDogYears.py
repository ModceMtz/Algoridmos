def calculate_ages(humanYears):
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return {
        'años humanos': humanYears,
        'años gato': catYears,
        'años perro': dogYears
    }


# Ejemplo de uso
print(calculate_ages(1))  # Output: [1, 15, 15]
print(calculate_ages(2))  # Output: [2, 24, 24]
print(calculate_ages(10))  # Output: [10, 56, 64]
