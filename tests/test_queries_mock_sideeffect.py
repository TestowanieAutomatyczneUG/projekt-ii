from unittest.mock import *
import unittest
from assertpy import *
from src.queries import *
from src.client import Client
from src.item import Item
from src.order import Order

class TestsMock(unittest.TestCase):
    def setUp(self):
        self.mockClass = Queries()

    def test_mockClass_get_clients(self):
        self.mockClass.get_clients = Mock(return_value=[("1","Bob","Bobinovich","example.example@example.com"),
                                                        ("2","Bobin","Bobinin","example.example@example.com")],side_effect=Exception("wrong id type"))
        assert_that(self.mockClass.get_clients).raises(Exception)
    def test_mockClass_get_items(self):
        self.mockClass.get_items = Mock(return_value=[("1","Bob","777"),("2","Bobin","73477")],side_effect=Exception("wrong id type"))
        assert_that(self.mockClass.get_items).raises(Exception)
    def test_mockClass_get_orders(self):
        self.mockClass.get_orders = Mock(return_value=["(1,2),(2,1),(1,3)"],side_effect=Exception("wrong id type"))
        assert_that(self.mockClass.get_orders).raises(Exception)
    def test_mockClass_get_orders_from_item_by_id(self):
        self.mockClass.get_orders_from_item_by_id = Mock(return_value=[(1,"Bob",777)],side_effect=Exception("wrong id type"))
        assert_that(self.mockClass.get_orders_from_item_by_id).raises(Exception)
    def test_mockClass_get_items_from_orders_by_id(self):
        self.mockClass.get_items_from_orders_by_id = Mock(return_value=[(709, "cosiek", 177.0)],side_effect=Exception("wrong id type"))
        assert_that(self.mockClass.get_items_from_orders_by_id).raises(Exception)
    def test_mockClass_get_order_by_id(self):
        self.mockClass.get_order_by_id = Mock(return_value=[(1,2)])
        assert_that(self.mockClass.get_order_by_id(2)).is_equal_to([(1,2)])
    def test_mockClass_get_client_orders_by_id(self):
        self.mockClass.get_order_by_id = Mock(return_value=[(1,2),(1,3)])
        assert_that(self.mockClass.get_order_by_id(2)).is_equal_to([(1,2),(1,3)])
    def test_mockClass_get_client_by_id(self):
        self.mockClass.get_client_by_id = Mock(return_value=(7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
        assert_that(self.mockClass.get_client_by_id(7)).is_equal_to((7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
    def test_mockClass_get_item_by_id(self):
        self.mockClass.get_client_by_id = Mock(return_value=(709, "cosiek", 177.0))
        assert_that(self.mockClass.get_client_by_id(709)).is_equal_to((709, "cosiek", 177.0))
    def test_mockClass_add_item(self):
        self.mockClass.add_item = Mock(return_value=(709, "cosiek", 177.0))
        assert_that(self.mockClass.add_item()).is_equal_to((709, "cosiek", 177.0))
    def test_mockClass_add_client(self):
        self.mockClass.add_client = Mock(return_value=(7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
        assert_that(self.mockClass.add_client()).is_equal_to((7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
    def test_mockClass_add_item_to_order(self):
        self.mockClass.add_client = Mock(return_value=())
        assert_that(self.mockClass.add_client(2,3)).is_equal_to(())
    def test_mockClass_add_order(self):
        self.mockClass.add_order = Mock(return_value=(2,3))
        assert_that(self.mockClass.add_order()).is_equal_to((2,3))
    def test_mockClass_delete_item_from_order(self):
        self.mockClass.delete_item_from_order = Mock(return_value=())
        assert_that(self.mockClass.delete_item_from_order(2,3)).is_equal_to(())
    def test_mockClass_edit_item(self):
        self.mockClass.edit_item = Mock(return_value=("motylek",3))
        assert_that(self.mockClass.edit_item("motylek",3)).is_equal_to(("motylek",3))
    def test_mockClass_edit_order(self):
        self.mockClass.edit_order = Mock(return_value=(1,3))
        assert_that(self.mockClass.edit_order(1,3)).is_equal_to((1,3))
    def test_mockClass_edit_client(self):
        self.mockClass.edit_client = Mock(return_value=("bob","bobin","b@b.com"))
        assert_that(self.mockClass.edit_client("bob","bobin","b@b.com")).is_equal_to(("bob","bobin","b@b.com"))
    def test_mockClass_edit_item_from_order(self):
        self.mockClass.edit_item_from_order = Mock(return_value=(2,3))
        assert_that(self.mockClass.edit_item_from_order(2,3)).is_equal_to((2,3))
    def test_mockClass_delete_item(self):
        self.mockClass.delete_item = Mock(return_value=())
        assert_that(self.mockClass.delete_item(2)).is_equal_to(())
    def test_mockClass_delete_order(self):
        self.mockClass.delete_order = Mock(return_value=())
        assert_that(self.mockClass.delete_order(1)).is_equal_to(())
    def test_mockClass_delete_client(self):
        self.mockClass.delete_client = Mock(return_value=())
        assert_that(self.mockClass.delete_client(3)).is_equal_to(())
