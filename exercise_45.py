# Solicitar al usuario que ingrese su direccion de email.
# Imprimir un mensaje indicando si la direccion es valida o no,
# valiendose de una funcion para decidirlo.
# Una direccion se conderara valida si contiene el simbolo @

def emailVerification(email):
    if "@" in email:
        print("El mail ingresado es correcto")
    else:
        print("El mail ingresado es incorrecto, vuelva a intentarlo")

emailVerification(input("Ingresar dirección de email: "))
