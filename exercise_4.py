# Preguntar e imprimir n veces, el nombre del usuario
# en la consola en diferentes lineas
import math

name = input("Ingrese su nombre\n")

printIter = float(input("Ahora, ingrese un numero entero \n"))

while printIter < 0:
    printIter = float(input("Vuelva a intentarlo. Ingrese un numero entero \n"))

while math.modf(printIter > 0):
    printIter = float(input("Vuelva a intentarlo. Ingrese un numero entero \n"))

print(f"El nombre ingresado es {name} y la cantidad de veces a imprimir su nombre es {printIter} veces")

if printIter == 0:
    print("Su nombre no se imprimira porque ha elegido iterar 0 veces")
else:
    print((name + "\n")*printIter)
