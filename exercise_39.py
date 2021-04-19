# Se debe generar los primeros k números de la serie de Fibonacci. En la serie
# los dos primeros números son el 0 y el 1. El resto se calcula como la suma de los dos
# números que lo preceden. Además debe contar cuantos números primos existen en la serie

def printPrimesFibo(number: int):
    if number.isnumeric():
        f0 = 1
        f1 = 2
        fn = 2
        flag = False
        counter = 0
        suma = 0
        number = int(number)
        for iterador1 in range(1, number+1):
            flag = False
            while flag != True:
                for iterador2 in range(1, fn+1):
                    if fn % iterador2 == 0:
                        counter += 1
                        suma += iterador2
                if counter == 2 and suma == fn+1:
                    flag = True
                    counter = 0
                    suma = 0
                    print(fn, end=", ")
                    fn = f0 + f1
                    f0 = f1
                    f1 = fn
                else:
                    flag = False
                    counter = 0
                    suma = 0
                    fn = f0 + f1
                    f0 = f1
                    f1 = fn

    else:
        print("Error de ingreso, vuelva a intentarlo")


printPrimesFibo(input(
    "Ingrese la cantidad de numeros de fibonacci a generar que seran comparados con numeros primos = "))
