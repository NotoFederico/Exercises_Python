# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

sentence = input("Ingrese una frase\n")
letter = input("Ahora ingrese una letra\n")
letterCount = 0
for cnt in sentence:
    if cnt == letter:
        letterCount += 1
print(
    f"La frase \"{sentence}\", contiene {letterCount} veces la letra \"{letter}\"")
