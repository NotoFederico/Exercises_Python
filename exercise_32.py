# Dados 3 números naturales, A, B y C, mostrar los múltiplos de A, menores que B que no sean divisores de C

a = int(input("Ingresar A: "))
b = int(input("Ingresar B: "))
c = int(input("Ingresar C: "))
flag = False

for iterador in range(1, a):
    if a % iterador == 0 and iterador < b and c % iterador != 0:
        flag = True
        print(iterador)
if(flag=False)
print("No hay un valor que cumpla todas las condiciones")
