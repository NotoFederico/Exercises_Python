# Dada una lista de N números x, indicar si la misma viene ordenada ascendentemente.

list = []
flag = False
maxA = 0

n = int(input("Ingresar el numero de elementos de la lista a crear, N = "))

print(f"-Ahora ingrese los {n} elementos de la lista-")
for iterador in range(n):
    list.append(int(input(f"Ingrese el elemento {iterador+1} de la lista = ")))

sortedList = sorted(list)
if sortedList == list:
    print("La lista esta ordenada de forma ascendente")
else:
    print("La lista NO esta ordenada de forma ascendente")
