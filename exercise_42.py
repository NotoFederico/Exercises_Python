# Dada una matriz de caracteres, ordenar cada columna alfabéticamente

suma = 0
matrix = []
aux = []
# Ingreso de tamaño de la matriz
n = int(input("Ingresar el numero de filas de la matriz = "))
m = int(input("Ingresar el numero de columnas de la matriz = "))

# Ingreso de datos en la matriz
for row in range(n):
    matrix.append([])
    for column in range(m):
        matrix[row].append(
            input(f"Ingrese un caracter para fila {row} - columna {column} = "))

# Imprimo la matriz sin ordenar
print("Matriz resultante\n")
for iterador in matrix:
    print(*iterador)

# Ordeno la matriz alfabeticamente por columna
for column in range(n):
    for row in range(m):
        aux.append(matrix[row][column])
    aux = sorted(aux)
    for i in range(m):
        matrix[i][column] = aux[i]
    aux = []

# Imprimo la matriz ordenada
print("Matriz resultante\n")
for iterador in matrix:
    print(*iterador)
