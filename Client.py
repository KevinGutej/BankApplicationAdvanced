class Client:
    def __init__(self, name, login,password,account):
        self.name = name
        self.login = login
        self.account = account
        self.password = password
        self.balance = 0

    def pay_in(self, cash_amount : int):
        self.balance = self.balance + cash_amount

    def pay_out(self, cash_amount : int):
        if(cash_amount > self.balance):
            print("You do not have enought money to pay out")
        else:
            self.balance = self.balance - cash_amount




