class User:
    def __init__(self, fname):
        self.fname = fname
        # self.lname = lname
        # self.email = email
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self
    def make_withdrawl (self, amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.fname} balance: {self.amount}")
        return self
    def make_transfer(self, amount, user2):
        self.amount -= amount
        user2.amount += amount
        self.display_user_balance()
        user2.display_user_balance()

Lancelot = User("Lancelot")
timothy= User("timothy")
johnny= User("johnny")

Lancelot.make_deposit(3000000000).make_deposit(3500000000).make_deposit(33000000000).make_withdrawl(100000000).display_user_balance()

timothy.make_deposit(3000000000).make_deposit(3500000000).make_withdrawl(12131300000).make_withdrawl(100000000).display_user_balance()

johnny.make_deposit(3000000000).make_withdrawl(3500000000).make_withdrawl(33000000000).make_withdrawl(100000000).display_user_balance()

Lancelot.make_transfer(700, johnny)