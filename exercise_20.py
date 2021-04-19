# Dado un número natural x, sumar todos sus dígitos. Mostar la suma obtenida.

def digitAddition(number: str):
    adition = 0
    if number.isnumeric():
        for iterador in number:
            adition += int(iterador)
        return print(f"Numero = {number}, la suma de sus digitos es {adition}")
    else:
        return print("Error de ingreso")


digitAddition(input("Ingrese un numero natural\n"))
