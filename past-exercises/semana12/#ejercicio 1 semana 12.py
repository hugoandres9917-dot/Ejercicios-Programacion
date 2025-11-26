#ejercicio 1 semana 12

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("El monto a depositar debe ser positovo.")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe se positivo")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes")
        self.balance -= amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser positivo")
        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"No se puede retirar {amount}."
                f"El balance no se puede quedar por debajo del minimo({self.min_balance})."
            )
        self.balance -= amount
        return self.balance   

account = BankAccount(100)
account.deposit(50)

account.withdraw(30)

savings = SavingsAccount(balance=200, min_balance=100)
savings.withdraw(50)

    
    

