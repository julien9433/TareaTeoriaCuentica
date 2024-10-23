from Split import texto

text = "en un lugar de la mancha"
print(text.capitalize())

texto_en_mayuscula = text.upper()
print(texto_en_mayuscula)

texto_en_minuscula = texto_en_mayuscula.lower()
print(texto_en_mayuscula)

longitud_texto = len(texto_en_minuscula)
print(longitud_texto)

# En un lugar de la mancha
print(texto_en_minuscula.isalnum())

cadena_ejemplo = "12345 67890"
vocales = "aeiouAEIOU"
print(cadena_ejemplo.isalnum())
print(cadena_ejemplo.isalpha())
print(vocales.isalpha())
print(cadena_ejemplo.isdigit())
print(vocales.lower())
print(texto_en_mayuscula.islower())
print(texto_en_minuscula.islower())
print(texto_en_minuscula.isupper())
print(texto_en_minuscula.isupper())

cadena_ejemplo = "     En un lugar de la mancha    "
print(cadena_ejemplo.lstrip())
print(cadena_ejemplo.rstrip())
print(cadena_ejemplo.strip())
