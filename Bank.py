import Client
from File import FileWritter

class Bank:
    def __init__(self):
        self.clients = []
    def add_client(self,client):
        self.clients.append(client)
        FileWritter.save_clients(self.clients)
