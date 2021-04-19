# Crear una clase Cajero en el cual permita a un usuario
# sacar dinero

KEYS = 0
CASH = 1

class Cajero:

    def __init__(self):
        self.__users = {
            "federico":[1234,1000],
            "martin":[555,9999999]
        }
        self.__attemps = 3

    def login(self, user, password):
        if self.__attemps !=0:
            if user in self.__users.keys():
                if password == self.__users[user][KEYS]:
                    print(f"Welcome {user}!")
                    print(f"Current actives =  ${self.__users[user][CASH]}")
                    if self.__users[user][KEYS] > 0:
                        amount = int(input("Enter the amount of money to extract = $"))
                        if(amount<=self.__users[user][CASH]):
                            print("Processing your request")
                            self.__users[user][CASH] -= amount
                            print("Withdraw your money please")
                            print(f"Current actives =  ${self.__users[user][CASH]}")
                        else:
                            print("Insufficient funds")
                else:
                    self.__attemps -=1
                    print("Wrong password!")
            else:
                print("Invalid credentials")
        else:
            print("Too many attemps. Card blocked. Call your bank")



cajero = Cajero()
#Python es hackeable
print(cajero._Cajero__users)
cajero.login("federico",12134)
cajero.login("federico",1234)
