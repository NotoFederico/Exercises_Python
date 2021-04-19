# Dado un número natural x, sumar todos sus divisores.
def divisor(number: int):
    sum = 0
    if number.isnumeric():
        number = int(number)
        print(f"La suma de los divisores de {number} es:")
        for iterador in range(1, number):
            if number % iterador == 0:
                sum += iterador
        print(sum)
    else:
        print("Error de ingreso, vuelva a intentarlo")


divisor(input("Ingrese un numero para luego mostrar la suma de todos sus divisores = "))
