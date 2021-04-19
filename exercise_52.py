# Crear una clase Perro la cual describa su raza, porte,
# color y que pueda ladrar, comer y saltar

class Perro():
    def __init__(self, raza, porte, color):
        self.raza = raza
        self.porte = porte
        self.color = color
    def ladrar(self):
        print("Woof!")
    def comer(self):
        global comida
        if(comida>0):
            comida -=50
            print(f"*Eating noises* - Food left {comida} gr")
        else:
            print("No hay mas comida! Woof!")
    def saltar(self):
        print("Jump!")
    def info(self):
        print("Raza: ", self.raza)
        print("Porte: ", self.porte)
        print("Color: ", self.color)


comida = 400
perro = Perro("Border Collie", "Mediano", "Negro")
perro.info()
perro.saltar()