# Dados dos números naturales A y B, mostrar sus divisores comunes
def commonDiv(a, b):
    if a > 0 and b > 0:
        print("\nLos divisores que tienen en comun son:")
        for iterador1 in range(1, a+1):
            if a % iterador1 == 0:
                for iterador2 in range(1, b):
                    if b % iterador2 == 0 and iterador2 == iterador1:
                        print(iterador2, end=", ")
    else:
        return print("Alguno de los numeros ingresados es menor o igual a 0, vueva a intentarlo")


a = int(input("Ingrese el numero natural A\n"))
b = int(input("Ingrese el numero natural B\n"))

commonDiv(a, b)
