class bankAccount:
    bank_balance=[]
    # bank_names=[]
    def __init__(self, account, interest_rate):
        self.account = account
        self.interest_rate= interest_rate
        # bankAccount.bank_names.append(name)
        # bankAccount.bank_balance.append(account)
    def __repr__(self):
        return self.account
    # def __repr__(self):
    #     return self.name

    def deposit_money(self, account):
        self.account += account
        return self
    def withdrawl_money(self, account):
        self.account -= account
        return self
    def display_balance(self):
        print(f"balance:{self.account}")
    def yield_interest(self):
        if self.account > 0:
            self.account += (self.interest_rate*self.account)
            # print(f"user:{self.name} and balance:{self.account}")
        return self
    @classmethod
    def print_Accounts_All(cls):
        sum = 0
        for account in cls.bank_balance:
            sum += account.balance
        return sum
        


        # for name in cls.bank_names:
        #     for account in bank_balance:
        #         print(f"{name} balance: {account}")

aAccount = bankAccount(0,1.6)
# aAccount.deposit_money(100).deposit_money(200).deposit_money(122246264374).withdrawl_money(864529375).yield_interest().display_balance()
bAccount = bankAccount(0,2.5)
# bAccount.deposit_money(100).deposit_money(1000).withdrawl_money(122246264374).withdrawl_money(864529375).yield_interest().display_balance()


# print(bankAccount.bank_names)
# print(bankAccount.bank_balance)


bankAccount.print_Accounts_All()


# def printInfo(someDict):
#     for key,val in someDict.items():
#         print(f"{len(val)} {key.upper()}")
#         for i in range (0,  len(val)):
#             print(val[i])
