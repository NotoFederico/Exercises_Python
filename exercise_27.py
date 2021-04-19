# Dada una lista de N números naturales x, mostrar el menor de ellos.
list = []
n = int(input("Ingresar el numero de elementos de la lista a crear, N = "))
print(f"-Ahora ingrese los {n} elementos de la lista-")
for iterador in range(n):
    list.append(int(input(f"Ingrese el elemento {iterador} = ")))
print("La lista ha sido completada")
print("El minimo de los elementos es el numero ", min(list))
