

class user:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    # Add money 
    def make_deposit(self, amount):
        self.balance += amount
        return self

    # Takes money away
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    # Print the user name and balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    # BONUS: moves money from one user to another
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self


yara = user("Yara Mhanna")
hamza = user("Hamza Mhanna")
zaid = user("Zaid Mhanna")

# 1. First user 3 deposits, 1 withdrawal 
yara.make_deposit(100).make_deposit(50).make_deposit(25).make_withdrawal(30).display_user_balance()

# 2. Second user 2 deposits, 2 withdrawals 
hamza.make_deposit(200).make_deposit(75).make_withdrawal(40).make_withdrawal(10).display_user_balance()

# 3. Third user 1 deposit, 3 withdrawals 
zaid.make_deposit(500).make_withdrawal(100).make_withdrawal(50).make_withdrawal(25).display_user_balance()

# 4. BONUS: first user transfers money to the third user 
yara.transfer_money(zaid, 45).display_user_balance()
zaid.display_user_balance()