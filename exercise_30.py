# Dadas dos listas de números A y B, indicar si el mayor de la lista A se encuentra en la lista B.

listA = []
listB = []
maxA = 0

n = int(input("Ingresar el numero de elementos de la lista A a crear, N = "))

print(f"-Ahora ingrese los {n} elementos de la lista A-")
for iterador in range(n):
    listA.append(
        int(input(f"Ingrese el elemento {iterador+1} de la lista A = ")))

maxA = max(listA)

print("El valor máximo de la lista A es ", maxA)

n = int(input("Ingresar el numero de elementos de la lista B a crear, N = "))

print(f"-Ahora ingrese los {n} elementos de la lista B-")
for iterador in range(n):
    listB.append(
        int(input(f"Ingrese el elemento {iterador+1} de la lista B = ")))

if maxA in listB:
    print(f"El maximo \"{maxA}\" de la lista A se encuentra en la lista B")
else:
    print("El máximo de la lista A NO se halla en la lista B")
