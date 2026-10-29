
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


account1 = BankAccount(0.02, 0)
account2 = BankAccount(0.05, 0)

# 1. First account: 3 deposits, 1 withdrawal, yield interest, display 
account1.deposit(100).deposit(50).deposit(25).withdraw(30).yield_interest().display_account_info()

# 2. Second account: 2 deposits, 4 withdrawals, yield interest, display 
account2.deposit(200).deposit(100).withdraw(20).withdraw(30).withdraw(40).withdraw(10).yield_interest().display_account_info()