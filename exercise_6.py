# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

workHours = int(input("Ingrese la cantidad de horas trabajadas\n"))
costPerHour = int(input("Ahora ingrese el costo por hora de su trabajo\n"))
print(
    f"La paga que le corresponde por trabajar {workHours} horas al dia a un costo de ${costPerHour} por hora es de {workHours*costPerHour}")
