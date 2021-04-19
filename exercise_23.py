# Dado un número natural x, mostrar todos sus divisores.
def divisor(number: int):
    if number.isnumeric():
        number = int(number)
        print(f"El numero {number} es divisible por:")
        for iterador in range(1, number):
            if number % iterador == 0:
                print(iterador, end=", ")
    else:
        print("Error de ingreso, vuelva a intentarlo")


divisor(input("Ingrese un numero para luego mostrar todos sus divisores posibles = "))
