# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

word = input("Ingrese una palabra\n")
wordLenght = len(word)
for cnt in range(wordLenght, 0, -1):
    print(word[cnt-1])
