from Client import Client

class UI:
    def show_start_page(self,bank):
        print("***************MAIN MENU********************")
        print('______________________________________________________________________________________________')
        print("Do you have a account?")
        account = input("Y / N: ")
        if account == 'Y':
            UI.login(bank)
        else:
            name = input("Please enter your name: ")
            login = input("Please enter login: ")
            password = input("Please enter your password: ")
            new_client = Client(name,login,password)
            bank.add_client(new_client)


    @staticmethod
    def login(bank):
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
            else:
                print("Password Incorect")

    def show_clients(self,clients):
        for client in clients:
            print(f"Name: {client.name}, Login: {client.login}")




