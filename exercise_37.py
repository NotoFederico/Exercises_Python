# Calcular cuantos segundos tiene una hora dada. (por ej. 12:23:15 tiene 44595 segundos)

hours = int(input("Ingrese cantidad de horas = "))
minutes = int(input("Ingrese cantidad de minutos = "))
seconds = int(input("Ingrese cantidad de segundos = "))

print(
    f"la cantidad de segundos del tiempo ingresado es de {hours*60*60+minutes*60+seconds} segundos")
