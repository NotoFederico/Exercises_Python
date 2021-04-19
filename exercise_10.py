# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

num = int(input("Ingrese un numero\n"))
string = "es par" if num % 2 == 0 else "es impar."
print(f"El numero ingresado \"{num}\", {string}")
