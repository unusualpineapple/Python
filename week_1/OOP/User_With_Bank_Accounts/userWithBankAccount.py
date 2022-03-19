class BankAccount:
    def __init__(self, account_name, account, interest_rate):
        self.account_name = account_name
        self.account = account
        self.interest_rate = interest_rate
    def __repr__(self):
        return self.account

class User(BankAccount):
    def __init__(self, account_name, account, interest_rate, name):
        super().__init__(account_name, account, interest_rate)
        self.name = name
        # self.checking = BankAccount(100, .04)
    def __repr__(self):
        return self.name

    def make_deposit(self, account):
        self.account += account
        return self

    def make_withdrawl(self, amount):
        self.account -= amount
        return self

    def display_user_balance (self):
        print(f"{self.name} {self.account_name} : {self.account}")
        return self

anthony = User("checking", 100, .04, "anthony")
anthony.make_deposit(100).make_withdrawl(50).display_user_balance()
benjy = User("saving", 200, .08, "anthony")
benjy.make_deposit(5000).make_withdrawl(2000).display_user_balance()
chad = User("checking 2", 150, .09, "anthony")
chad.make_deposit(10000).make_withdrawl(6000).display_user_balance()
david = User("savings 2", 350, .09, "anthony")
david.make_deposit(20000).make_withdrawl(7000).display_user_balance()