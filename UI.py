from Client import Client

class UI:

    def __init__(self):
        self.logged_user = None

    def show_start_page(self,bank):
        print("***************MAIN MENU********************")
        if self.logged_user:
            print(f" Currently logged: {self.logged_user} ")
        else:
            print(f" Currently logged: Offline ")

        print("[1] - Login in")
        print("[2] - Sign Up")
        print("[3] - Exit")

        while True:
            choice = input("Please a option: ")
            if choice.isdigit():
                if int(choice) > 0 and int(choice) < 4:
                    return int(choice)
            else:
                print("Please enter again")

        print('______________________________________________________________________________________________')
        print("Do you have a account?")
        account = input("Y / N: ")
        if account == 'Y':
            UI.login(bank)

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




