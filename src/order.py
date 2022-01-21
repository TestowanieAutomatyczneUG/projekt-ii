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

    def is_id_leading_to_item(self, itemId: int):
        if type(itemId) is not int:
            raise ValueError("itemId is not int")
        for item in self.items:
            if item.id == itemId:
                return True
        return False

    def get_client(self):
        return Queries.find_client(self.clientId)

    def get_item(self):
        result = []
        for item in self.items:
            result.append((item.id, item.name, item.value))
        return result

    def get_all_orders():
        return Order.orders

    def find_order(id: int):
        if type(id) is not int:
            raise ValueError("id is not int")
        for order in Order.orders:
            if order.id == id:
                return order
        return None

    def delete_order(id: int):
        if type(id) is not int:
            raise ValueError("id is not int")
        for order in Order.orders:
            if order.id == id:
                Order.orders.remove(order)
                Queries.delete_order(id)
                del order
                return True
        raise ValueError("There is no order with this id")