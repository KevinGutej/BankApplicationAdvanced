import uuid

class Client:
    def __init__(self, name, login):
        self.name = name
        self.login = login
        self.id = uuid.uuid1()


