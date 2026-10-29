
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    # Adds money to this user's balance
    def make_deposit(self, amount):
        self.balance += amount

    # Takes money away from this user's balance
    def make_withdrawal(self, amount):
        self.balance -= amount

    # Prints the user's name and balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    # BONUS: moves money from this user to another user
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount


yara = User("yara Mhanna")
hamza = User("hamza Mhanna")
zaid = User("zaid Mhanna")

# 2.  First user 3 deposits, 1 withdrawal
yara.make_deposit(100)
yara.make_deposit(50)
yara.make_deposit(25)
yara.make_withdrawal(30)
yara.display_user_balance()

# 2. Second user 2 deposits, 2 withdrawals
hamza.make_deposit(200)
hamza.make_deposit(75)
hamza.make_withdrawal(40)
hamza.make_withdrawal(10)
hamza.display_user_balance()

# 3. Third user 1 deposit, 3 withdrawals
zaid.make_deposit(500)
zaid.make_withdrawal(100)
zaid.make_withdrawal(50)
zaid.make_withdrawal(25)
zaid.display_user_balance()

# 4. BONUS: first user transfers money to the third user
yara.transfer_money(zaid, 45)
yara.display_user_balance()
zaid.display_user_balance()