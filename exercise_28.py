# Dada una lista de N números enteros x, calcular su promedio. Mostrar el resultado.
list = []
sum = 0
n = int(input("Ingresar el numero de elementos de la lista a crear, N = "))
print(f"-Ahora ingrese los {n} elementos de la lista-")
for iterador in range(n):
    list.append(int(input(f"Ingrese el elemento {iterador} = ")))
    sum += list[iterador]
print("La lista ha sido completada")
print("El promedo de los valores ingresados es ", sum/len(list))
