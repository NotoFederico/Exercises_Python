# Generar los primeros h números primos (Un número es primo si solo es
# divisible por si mismo y por la unidad)

def printPrimes(number: int):
    if number.isnumeric():
        prime = 2
        flag = False
        counter = 0
        suma = 0
        number = int(number)
        for iterador1 in range(1, number+1):
            #print("Valor de iterador1", iterador1)
            flag = False
            while flag != True:
                for iterador2 in range(1, prime+1):
                    #print("Valor de iterador2", iterador2, prime)
                    if prime % iterador2 == 0:
                        counter += 1
                        suma += iterador2
                if counter == 2 and suma == prime+1:
                    flag = True
                    counter = 0
                    suma = 0
                    print(prime, end=", ")
                    prime += 1
                else:
                    flag = False
                    counter = 0
                    suma = 0
                    prime += 1

    else:
        print("Error de ingreso, vuelva a intentarlo")


printPrimes(input("Ingrese la cantidad de numeros primos a generar = "))
