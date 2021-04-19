# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
cnt = 0
num = int(input("Ingrese un numero entero positivo\n"))
if num < 0 or num == 0:
    num = int(input("Vuelva a intentarlo.\nIngrese un numero entero positivo"))
elif num > 0:
    for cnt in range(1, num+1):
        if cnt % 2 != 0:
            print(cnt, end=", ")
