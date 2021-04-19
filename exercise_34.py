# Dados 3 dígitos, generar y mostrar el mayor número natural que puede escribirse con ellos.
list = []
list.append(input("Ingresar el digito A: "))
list.append(input("Ingresar el digito B: "))
list.append(input("Ingresar el digito C: "))
list = sorted(list)
list = list[::-1]
list = "".join(list)
print(list)
