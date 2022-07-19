from os.path import exists
import pickle

class FileWritter:
    @staticmethod
    def save_clients(clients):
        f = open("clients.pickle", "wb")
        pickle.dump(clients, f)

    @staticmethod
    def read_clients():
        fileexists = exists("clients.pickle")
        if fileexists:
            f = open("clients.pickle", "rb")
            clients = pickle.load(f)
        else:
            clients = []
        return clients





