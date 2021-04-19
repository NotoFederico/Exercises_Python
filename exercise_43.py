# Dada una matriz de NxM elementos, compuesta de 0 y 1 , recorrer
# cada una de las filas y mostrar el valor decimal equivalente.

matrix = []
string = ""
suma = 0
c = 0

# Ingreso de tamaño de la matriz
n = int(input("Ingresar el numero de filas de la matriz = "))
m = int(input("Ingresar el numero de columnas de la matriz = "))

# Ingreso de datos en la matriz
for row in range(n):
    matrix.append([])
    for column in range(m):
        while True:
            value = input(
                f"Ingrese un caracter para fila {row} - columna {column} (TIENE QUE SER 0 o 1) = ")
            if value != "0" and value != "1":
                print("Se ha ingresado un caracter invalido, vuelva a intentarlo")
            else:
                break
        matrix[row].append(value)

# Imprimo la matriz ordenada
print("Matriz resultante\n")
for iterador in matrix:
    print(*iterador)

# Recorro cada fila y muestro el valor decimal
for row in matrix:
    for iterador in row:
        string += iterador
    c = len(string)-1
    for iterador in string:
        suma += int(iterador)*(2**c)
        c -= 1
    print(f"La suma de la fila {row} es {suma}")
    string = ""
    suma = 0
