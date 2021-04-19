# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
cnt = 0
num = int(input("Ingrese un numero entero positivo\n"))
if num < 0 or num == 0:
    num = int(input("Vuelva a intentarlo.\nIngrese un numero entero positivo"))
elif num > 0:
    for cnt in range(num, -1, -1):
        print(cnt, end=", ")
