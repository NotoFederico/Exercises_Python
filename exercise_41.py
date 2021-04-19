# Dada una matriz de NxM elementos, calcular el promedio de cada fila y de
# cada columna. Mostrar en pantalla la matriz cargada y los promedios correspondientes.

counter = 0
suma = 0
matrix = []

# Ingreso de tamaño de la matriz
n = int(input("Ingresar el numero de filas de la matriz = "))
m = int(input("Ingresar el numero de columnas de la matriz = "))

# Ingreso de datos en la matriz
for row in range(n):
    matrix.append([])
    for column in range(m):
        matrix[row].append(
            int(input(f"Ingrese un dato para fila {row} - columna {column} = ")))

# Imprimo la matriz
print("Matriz resultante\n")
for iterador in matrix:
    print(*iterador)

# Promedio del valor de cada fila
for iterador in matrix:
    print(f"Fila {counter} - {iterador} - Promedio - {sum(iterador)/n}")
    counter += 1

# Promedio del valor de cada columna
for column in range(m):
    for row in range(n):
        suma += matrix[row][column]
        print(matrix[row][column], end=", ")
    print(f"El promedio de la columna {column} es {suma/m}")
    suma = 0
