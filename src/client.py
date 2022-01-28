import json
from src.queries import Queries
from src.order import Order

class Client:
    def __init__(self, id: int, firstName:str, lastName:str, email:str):
        if type(id) is not int:
            raise ValueError("id is not int")
        if type(firstName) is not str or not firstName:
            raise ValueError("firstName is not string")
        if Client.find_client(id):
            raise ValueError("client with this id already exists")
        if type(email) is not str or not email:
            raise ValueError("email is not string")
        if type(lastName) is not str or not lastName:
            raise ValueError("lastName is not string")
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.orders = []
        self.email = email
        Client.clients.append(self)
    clients = []
    def add_order(self, id):
        if type(id) is not int:
            raise ValueError("id is not int")
        self.orders.append(Order(id, self.id))
        Queries.add_order(id, self.id)

    def delete_order(self, id):
        if type(id) is not int:
            raise ValueError("id is not int")
        self.orders.remove(Order.find_order(id))
        Order.delete_order(id)

    def edit_firstName(self, firstName):
        if type(firstName) is not str or not firstName:
            raise ValueError("firstName is not string")
        self.firstName = firstName
        Queries.edit_client(self.id, self.firstName, self.lastName, self.email)

    def edit_lastName(self, lastName):
        if type(lastName) is not str or not lastName:
            raise ValueError("lastName is not string")
        self.lastName = lastName
        Queries.edit_client(self.id, self.firstName, self.lastName, self.email)

    def edit_email(self, email):
        if type(email) is not str or not email:
            raise ValueError("email is not string")
        self.email = email
        Queries.edit_client(self.id, self.firstName, self.lastName, self.email)

    def orders_data(self):
        result = []
        for order in self.orders:
            items = []
            id = Queries.find_items_from_order(order.id)
            for item in id:
                item = Queries.find_item(item[1])
                items.append(item)
            result.append(items)
        return result

    def all_clients():
        return Client.clients

    def all_clients_data():
        result = []
        for client in Client.clients:
            result.append((client.id, client.firstName, client.lastName, client.email))
        return result

    def find_client(id):
        if type(id) is not int:
            raise ValueError("id is not int")
        for client in Client.clients:
            if client.id == id:
                return client
        return None

    def delete_client(id):
        if type(id) is not int:
            raise ValueError("id is not int")
        for client in Client.clients:
            if client.id == id:
                Client.clients.remove(client)
                del client
                Queries.delete_client(id)
                return True
        raise ValueError("There is no client with this id")

    def save_to_file():
        with open("data/clients.json", "w") as file:
            result = []
            for client in Client.clients:
                result.append(client)
            file.write(json.dumps(result))