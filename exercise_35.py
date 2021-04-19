"""
A una fiesta asistieron personas de diferentes edades y sexos. Construir un
algoritmo dadas las edades y generos de las personas.
Calcular :
- Cantidad de personas que asistieron a la fiesta
- Cantidad de hombres y mujeres
- Promedio de edades por generos
- La edad de la persona más joven que asitió
Ingresar datos hasta una edad sea cero.
"""

ageMList = []
ageFList = []
age = 1
youngest = 0

sexFlag = False
ageFlag = False

while age != 0:

    age = int(input("Ingrese su edad = "))
    if age < 0:
        ageFlag = False
        print("Ha ingresado una edad negativa, vuelva a intentarlo")
    elif age == 0:
        ageFlag = False
    else:
        ageFlag = True

    if ageFlag == True:
        ageFlag = False
        aux = input("Ingrese su sexo: 'f' o 'm'? (case sensitive) = ")
        if aux == "m":
            ageMList.append(age)
            sexFlag = True
        elif aux == "f":
            ageFList.append(age)
            sexFlag = True
        else:
            sexFlag = False
            print("Vuelva a ingresar su sexo correctamente")

    print("\nSiguiente registro:\n")

youngest = min(ageMList) if min(ageMList) < min(ageFList) else min(ageFList)

print("Se ha terminado de llenar la base de datos de invitados")
print("Estadisticas demográficas:\n")
print(
    f"La cantidad de personas que concurriran al evento es de {len(ageMList) + len(ageFList)}")
print(
    f"La cantidad de hombres es de {len(ageMList)} con una edad promedio de {sum(ageMList)/len(ageMList)} años")
print(
    f"La cantidad de mujeres es de {len(ageFList)} con una edad promedio de {sum(ageFList)/len(ageFList)} años")
