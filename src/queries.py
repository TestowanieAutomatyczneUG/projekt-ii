class Queries:
    def get_clients(self):
        pass
    def get_items(self):
        pass
    def get_orders(self):
        pass
    def get_items_from_orders(self):
        pass
    def get_orders_from_item_by_id(self,item_id):
        pass
    def get_items_from_orders_by_id(self,order_id):
        pass
    def get_order_by_id(self,id):
        pass
    def get_client_orders_by_id(self,client_id):
        pass
    def get_client_by_id(self,id):
        pass
    def get_item_by_id(self,id):
        pass
    def add_item(self,id, name, value):
        pass
    def add_client(self,id, firstName, lastName, email):
        pass
    def add_item_to_order(self,order_id, item_id):
        pass
    def add_order(self,id, client_id):
        pass
    def delete_item_from_order(self,order_id, item_id):
        pass
    def edit_item(self,id, name, value):
        pass
    def edit_order(self,id, client_id):
        pass
    def edit_client(self,id, firstName, lastName, email):
        pass
    def edit_item_from_order(self,order_id, item_id):
        pass
    def delete_item(self,id):
        pass
    def delete_order(self,id):
        pass
    def delete_client(self,id):
        pass