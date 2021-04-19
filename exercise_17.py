# Dado un número natural x, mostrar su último dígito.
def lastDigit(number: str):
    if number.isnumeric():
        return print("El ultimo digito es: ", number[-1])
    else:
        return print("Error de ingreso")


lastDigit(input("Ingrese un numero = "))
