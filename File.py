import pickle

class FileWritter:
    def save_clients(clients):
        f = open("clients.pickle", "wb")
        pickle.dump(clients, f)

    def read_clients():
        f = open("clients.pickle", "rb")
        clients = pickle.load(f)
        return clients

