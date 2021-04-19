# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo.
num = int(input("Ingrese un numero entero positivo\n"))
char = "*"
for repeticion in range(num):
    print(char)
    char += "*"
