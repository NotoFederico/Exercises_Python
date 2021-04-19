# Pedir al usuario su edad y mostrar si es mayor o no de edad
age = int(input("Ingrese su edad\n"))
string = "mayor de edad" if age >= 18 else "menor de edad"
print(f"La edad ingresada es {age} por lo tanto usted es {string}")
