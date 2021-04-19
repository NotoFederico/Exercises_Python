# Dada una lista de N números naturales x, mostrar el mayor de ellos.

counter = 0
list = []
n = int(input("Ingresar el numero de elementos de la lista a crear, N = "))
print(f"-Ahora ingrese los {n} elementos de la lista-")

while counter < n:
    list.append(int(input(f"Ingrese el elemento {counter} = ")))
    counter += 1
print("La lista ha sido completada")
print("El mayor de los elementos es el numero ", max(list))
