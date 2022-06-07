from Client import Client

class UI:
    def show_start_page(bank):
        print("***************MAIN MENU********************")
        print('______________________________________________________________________________________________')
        print("Do you have a account?")
        account = input("Y / N: ")
        if account == 'Y':
            return
        else:
            name = input("Please enter your name: ")
            login = input("Please enter login: ")
            new_client = Client(name,login)
            bank.add_client(new_client)




    def login(self):
        pass


