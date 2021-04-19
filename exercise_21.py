# Dado un número natural x, determinar si es capicúa.
def capicua(number: str):
    if number.isnumeric():
        if number[::-1] == number:
            print(f"El numero {number} es capicua")
        else:
            print(f"El numero {number} NO es capicua")
    else:
        return print("Error de ingreso")


capicua(input("Ingrese un numero natural\n"))
