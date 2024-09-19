'''
Codigo para cambiar el tamaño de las imagenes o fotas a preferencia
'''
def ajustar_relacion_aspecto(ancho_original, alto_original):
    # La relación de aspecto deseada es 16:9
    # Calculamos el nuevo ancho manteniendo la altura original
    nuevo_ancho = round(alto_original * (16 / 9))

    return nuevo_ancho


# Ejemplo de uso
ancho_original = 374
alto_original = 280

nuevo_ancho = ajustar_relacion_aspecto(ancho_original, alto_original)
print(f"La nueva resolución con relación de aspecto 16:9 es {nuevo_ancho} x {alto_original}")
