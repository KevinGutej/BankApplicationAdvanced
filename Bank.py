import Client
from File import FileWritter

class Bank:
    def __init__(self):
        self.clients = FileWritter.read_clients()
    def add_client(self,client):
        self.clients.append(client)
        FileWritter.save_clients(self.clients)

    def get_client(self,client_login):
        temp_client = None
        for client in self.clients:
            if client_login == client.login:
                temp_client = client
        return temp_client
