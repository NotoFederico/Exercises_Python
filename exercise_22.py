# Dado un número entero x, mostrar sus N primeras potencias.

def printNPow(number: str, n: str):
    for iterador in range(n+1):
        print(
            f"La potencia de {number} elevado a la {iterador} es {number**iterador}")


number = int(input("Ingrese un numero entero base\n"))
n = int(input("Ahora ingrese otro numero para iterar la base\n"))

printNPow(number, n)
