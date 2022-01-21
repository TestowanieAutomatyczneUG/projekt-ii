from src.queries import Queries
from src.item import Item

class Order:
    orders = []

    def __init__(self, id: int, clientId: int):
        if type(id) is not int:
            raise ValueError("id is not int")
        if type(clientId) is not int:
            raise ValueError("clientId is not int")
        if not Queries.find_client(clientId):
            raise ValueError("There is no client with this id")
        self.id = id
        self.clientId = clientId
        self.items = []
        Order.orders.append(self)
