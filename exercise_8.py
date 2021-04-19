# Ingresar dos números y mostrar el menor de ellos

num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))
if num1 < num2:
    print(f"El primer número {num1}, es menor que el segundo, {num2}")
elif num1 == num2:
    print("Son iguales")
else:
    print(f"El segundo número {num2}, es menor que el primero, {num1}")
