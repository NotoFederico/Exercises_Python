# Dado un número natural x, contar la cantidad de dígitos pares e impares que posee.
def oddevenCounter(number: str):
    odd = 0
    even = 0
    if number.isnumeric():
        for iterador in number:
            if int(iterador) % 2 == 0:
                even += 1
            else:
                odd += 1
        return print(f"Numero = {number}, digitos: pares = {even}; impares = {odd}")
    else:
        return print("Error de ingreso")


oddevenCounter(input("Ingrese un numero natural\n"))
