class ContaBancaria:
    def __init__(self,holder,balance):
        self.holder = holder
        self.balance = balance
    def deposit(self,incremento):
        self.balance += incremento
    def withdraw(self,decremento):
        self.balance -= decremento
    def extract(self):
        return f"EXTRACT = {self.balance}"