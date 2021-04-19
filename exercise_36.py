# Determinar si un número X es perfecto, un número es perfecto si la suma de
# sus divisores es el mismo número. Ej. El 6 es perfecto ya que 1+2+3=6

def perfectNumber(number: int):
    aux = 0
    if number.isnumeric():
        number = int(number)
        for iterador in range(1, number):
            if number % iterador == 0:
                aux += iterador
        if aux == number:
            return print(f"El numero {number} es perfecto!")
        else:
            return print(f"El numero {number} NO es perfecto :(")
    else:
        return print("Error de ingreso, vuelva a intentarlo")


perfectNumber(input("Ingrese un numero para comprobar si es perfecto = "))
