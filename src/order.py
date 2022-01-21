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

    def add_item(self, itemId: int):
        if type(itemId) is not int:
            raise ValueError("itemId is not int")
        if not Queries.find_item(itemId):
            raise ValueError("There is no item with this id")
        for item in Item.items:
            if item.id == itemId:
                self.items.append(item)
                Queries.add_item_to_order(self.id, itemId)

    def delete_item(self, itemId: int):
        if type(itemId) is not int:
            raise ValueError("itemId is not int")
        for item in self.items:
            if item.id == itemId:
                self.items.remove(item)
                Queries.delete_item_from_order(self.id, itemId)
                return True
        raise ValueError("There is no item with this id")
