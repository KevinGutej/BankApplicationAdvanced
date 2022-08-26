from Client import Client

class UI:

    def __init__(self):
        self.logged_user = None

    def show_start_page(self,bank):
        print("***************MAIN MENU********************")
        if self.logged_user:
            print(f" Currently logged: {self.logged_user} ")
            client = bank.get_client(self.logged_user)
            print(f" Your balance: {client.balance} ")
            print(f" Your account number: {client.account} ")
            print("[4] - Pay In")
            print("[5] - Pay out")
        else:
            print(f" Currently logged: Offline ")
            print("[1] - Login in")
            print("[2] - Sign Up")

        print("[3] - Exit")


        while True:
            choice = input("Please enter your choice: ")
            if choice.isdigit():
                if int(choice) > 0 and int(choice) < 6:
                    return int(choice)
            else:
                print("Please enter again")

    def sign_up(self,bank):
        name = input("Please enter your name: ")
        login = input("Please enter login: ")
        password = input("Please enter your password: ")
        bank.add_client(name,login,password)




    def login(self,bank):
        print("Please enter your credentials:")
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        client = bank.get_client(username)
        if not client:
            print("There is no existing client with these login")
            return
        else:
            if password == client.password:
                print("Login Sucessful")
                print("Greetings,", username, "you are now logged in now with your password")
                self.logged_user = username
            else:
                print("Password Incorect")

    def show_clients(self,clients):
        for client in clients:
            print(f"Name: {client.name}, Login: {client.login}")

    def pay_in(self,bank):
        client = bank.get_client(self.logged_user)
        amount = input("How much money would you like to pay in: ")
        client.pay_in(int(amount))
        bank.update_clients()

    def pay_out(self,bank):
        client = bank.get_client(self.logged_user)
        amount = input("How much money would you like to pay out: ")
        client.pay_out(int(amount))
        bank.update_clients()