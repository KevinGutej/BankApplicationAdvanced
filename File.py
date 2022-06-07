class FileWritter:
    def save_clients(clients):
        with open('clients.txt', 'w') as file:
            for client in clients:
                file.write(f'{client.name}, {client.login}, {client.id}')
