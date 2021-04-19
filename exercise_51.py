# Crear una clase persona con los siguientes atributos:
# nombre, apellido, edad y que se pueda presentar

class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def presentarse(self):
        return f"Hola!, soy {self.nombre} {self.apellido} y tengo {self.edad} años"

federico = Persona("Federico", "Noto", 27)
print(federico.presentarse())