#Cree una clase de BankAccount que:
    #Tenga un atributo de balance.
    #Tenga un método para ingresar dinero.
    #Tenga un método para retirar dinero.
#Cree otra clase que herede de esta llamada SavingsAccount que:
    #Tenga un atributo de min_balance que se pueda asignar al crearla.
    #Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.

#ejercicio 1 Clase BankAccount

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance #Atributo de balance
        
    def deposit(self, amount):
        if amount > 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.balance += amount #Método para ingresar dinero
        return self.balancec 
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes para retirar.")
        self.balance -= amount #Método para retirar dinero
        return self.balance

#ejercicio 2 Clase SavingsAccount que hereda de BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance) # constructor de la clase padre
        self.min_balance = min_balance #Atributo de min_balance
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if self.balance - amount < self.min_balance: # Arroja un error si el retiro haría que el balance quede debajo del min_balance
            raise ValueError("No se puede retirar esa cantidad. El balance no puede quedar debajo del mínimo requerido.")
        self.balance -= amount
        return self.balance

#Ejemplo de uso

account = SavingsAccount(balance=1000, min_balance=200)
print("Balance inicial:", account.balance)
try:
    account.deposit(500)
    print("Balance después del depósito:", account.balance)
except ValueError as e:
    print("Error:", e)

try:
    account.withdraw(300)
    print("Balance después del retiro:", account.balance)
except ValueError as e:
    print("Error:", e)

savings = SavingsAccount(balance=1000, min_balance=200)
try:
    savings.withdraw(900)  # Esto debería arrojar un error porque dejaría el balance debajo del min_balance
    print("Balance después del retiro:", savings.balance)
except ValueError as e:
    print("Error:", e)
