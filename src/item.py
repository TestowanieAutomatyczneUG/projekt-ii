from src.queries import Queries

class Item:
    items = []

    def __init__(self, id: int, name: str, value: float):
        if type(id) is not int:
            raise ValueError("id is not int")
        if type(name) is not str or not name:
            raise ValueError("name is not string")
        if type(value) is not float and type(value) is not int:
            raise ValueError("value is not int")
        if value < 0:
            raise ValueError("value is not above 0")
        self.id = id
        self.name = name
        self.value = float(value)
        Item.items.append(self)

    def add_item(self):
        Queries.add_item(self.id, self.name, self.value)

    def delete_item(self):
        Queries.delete_item(self.id)

    def edit_name(self, name):
        if type(name) is not str or not name:
            raise ValueError("name is not string")
        self.name = name
        Queries.edit_item(self.id, self.name, self.value)

    def edit_value(self, value):
        if type(value) is not float and type(value) is not int:
            raise ValueError("value is not int")
        if value < 0:
            raise ValueError("value is not above 0")
        self.value = float(value)
        Queries.edytuj_item(self.id, self.name, self.value)

    def all_items():
        return Item.items