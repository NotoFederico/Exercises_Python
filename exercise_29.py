# Dada una lista ordenada de N números x, indicar si hay elementos repetidos.
list = []
flag = False
n = int(input("Ingresar el numero de elementos de la lista a crear, N = "))
print(f"-Ahora ingrese los {n} elementos de la lista-")
for iterador in range(n):
    list.append(int(input(f"Ingrese el elemento {iterador+1} = ")))
list.sort()
print(list)
for iterador in list:
    if list.count(iterador) > 1:
        flag = True
        print("Hay elementos repetidos")
        break
if flag == False:
    print("No hay elementos repetidos")
