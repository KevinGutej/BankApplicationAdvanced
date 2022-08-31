import pickle


file_name = "clients.pickle"

with (open(file_name, "rb")) as f:
    objects = pickle.load(f)

for client in objects:
    print(client.__dict__)

