# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-09-19
# DESCRIPTION: creating a class and its members

class BankAccount:
    name = ""
    balance = 0 # member variables

    def __init__(self,n: str,b: int): # constructor
        self.name = n
        self.balance = b

    def __str__(self): # print function in which we overwrite __str__
        return str(self.name) + " has a balance of $" + str(self.balance)

    def deposit(self, b: float): # deposit function
        self.balance += b

def main():
    ba1 = BankAccount("John", 100) # testing the program 
    ba1.deposit(400)
    print(ba1)
    ba2 = BankAccount("Codi", 300)
    ba2.deposit(600)
    print(ba2)

if __name__ == "__main__":
    main()