class Budget:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, input):
        self.balance += input

    def withdraw(self, out):
        self.balance -= out
    
    def balancea (self):
        statement = self.balance
        print(f"Balance is £{statement}.")

food = Budget(40)
clothes = Budget(45)
entertainment = Budget(50)

food.deposit(50)
food.withdraw(5.00)
clothes.withdraw(25.00)

food.balancea()
clothes.balancea()
entertainment.balancea()