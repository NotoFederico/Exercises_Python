# Dado un número natural x, contar la cantidad de dígitos que posee.

def digitQuantity(number: str):
    counter = 0
    if number.isnumeric():
        for iterador in number:
            counter += 1
        return print(f"La cantidad de digitos del numero {number} es {counter}")
    else:
        return print("Error de ingreso")


digitQuantity(input("Ingrese un numero natural\n"))
