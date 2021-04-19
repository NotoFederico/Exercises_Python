# Dado un número natural, calcular su factorial.

f = int(input("Ingrese un numero para calcular su factorial! = "))
result = 1

if f != 0:
    for iterador in range(1, f+1):
        result *= iterador
    print(f"{f}! = {result}")
elif f == 0:
    print(f"{f}! = {result}")
else:
    print("Ingreso erroneo, vuelva a intentarlo")
