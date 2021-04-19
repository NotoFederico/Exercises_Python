class FirstClass:  # Define a class object
    string = "Que viva España"
    def setdata(self, value):  # Define class's methods
        self.data = value  # self is the instance

    def display(self):
        print(self.data)  # self.data: per instance


class SecondClass(FirstClass):
    def display(self):
        print(f'Current value "{self.data}"')


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other



x = FirstClass()
y = FirstClass()
z = SecondClass()
a = ThirdClass('abc')

a.display()
print(a)
b = a + "apa"
print(b)
a.mul(3)
print(a)
c = 2 + 2
print(c)