import uuid

class Client:
    def __init__(self, name, login,password):
        self.name = name
        self.login = login
        self.id = uuid.uuid1()
        self.password = password


