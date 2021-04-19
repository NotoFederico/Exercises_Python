# Dada una lista de palabras, contar cuantas vocales y consonantes tiene cada palabra.

vocalCounter = 0
consonantCounter = 0
string = input("Ingrese el texto a analizar:  ")
string = string.split()  # convierte un texto en una lista
for word in string:  # itera por palabra
    for letter in word:  # itera por letra
        if letter.lower() in "aeiou":  # busca coincidencias entre la letra y "aeiou"
            vocalCounter += 1
        else:
            consonantCounter += 1
print(
    f"La frase {string} tiene {vocalCounter} vocales y {consonantCounter} consonantes")
