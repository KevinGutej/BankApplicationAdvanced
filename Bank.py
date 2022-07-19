from Client import Client
from File import FileWritter
import random

class Bank:
    def __init__(self):
        self.clients = FileWritter.read_clients()
    def add_client(self,name, login, password):
        new_account = Bank.account_number_gen(self.clients)
        new_client = Client(name, login, password, new_account)
        self.clients.append(new_client)
        FileWritter.save_clients(self.clients)

    def get_client(self,client_login):
        temp_client = None
        for client in self.clients:
            if client_login == client.login:
                temp_client = client
        return temp_client

    @staticmethod
    def account_number_gen(clients):
        while True:
            is_unique = True
            number = random.randint(0, 999999999999999999999999)
            number = str(number)
            number = number.rjust(26, "0")

            for client in clients:
                if client.account == number:
                    is_unique = False

            if is_unique:
                return number


