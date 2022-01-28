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

    def test_magicMockClass_get_clients(self):
        self.mockClass.get_clients = Mock(return_value=[(1,"Bob","Bobinovich","example.example@example.com"),
                                                        (2,"Bobin","Bobinin","example.example@example.com")])
        assert_that(self.mockClass.get_clients()).is_equal_to([(1,"Bob","Bobinovich","example.example@example.com"),
                                                        (2,"Bobin","Bobinin","example.example@example.com")])
    def test_magicMockClass_get_items(self):
        self.mockClass.get_items = MagicMock(return_value=[(1,"Bob",777),(2,"Bobin",73477)])
        assert_that(self.mockClass.get_items()).is_equal_to([(1,"Bob",777),(2,"Bobin",73477)])
    def test_magicMockClass_get_orders(self):
        self.mockClass.get_orders = MagicMock(return_value=[(1,2),(2,1),(1,3)])
        assert_that(self.mockClass.get_orders()).is_equal_to([(1,2),(2,1),(1,3)])
    def test_magicMockClass_get_orders_from_item_by_id(self):
        self.mockClass.get_orders_from_item_by_id = MagicMock(return_value=[(1,"Bob",777)])
        assert_that(self.mockClass.get_orders_from_item_by_id(1)).is_equal_to([(1,"Bob",777)])
    def test_magicMockClass_get_items_from_orders_by_id(self):
        self.mockClass.get_items_from_orders_by_id = MagicMock(return_value=[(709, "cosiek", 177.0)])
        assert_that(self.mockClass.get_items_from_orders_by_id(709)).is_equal_to([(709, "cosiek", 177.0)])
    def test_magicMockClass_get_order_by_id(self):
        self.mockClass.get_order_by_id = MagicMock(return_value=[(1,2)])
        assert_that(self.mockClass.get_order_by_id(2)).is_equal_to([(1,2)])
    def test_magicMockClass_get_client_orders_by_id(self):
        self.mockClass.get_order_by_id = MagicMock(return_value=[(1,2),(1,3)])
        assert_that(self.mockClass.get_order_by_id(2)).is_equal_to([(1,2),(1,3)])
    def test_magicMockClass_get_client_by_id(self):
        self.mockClass.get_client_by_id = MagicMock(return_value=(7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
        assert_that(self.mockClass.get_client_by_id(7)).is_equal_to((7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
    def test_magicMockClass_get_item_by_id(self):
        self.mockClass.get_client_by_id = MagicMock(return_value=(709, "cosiek", 177.0))
        assert_that(self.mockClass.get_client_by_id(709)).is_equal_to((709, "cosiek", 177.0))
    def test_magicMockClass_add_item(self):
        self.mockClass.add_item = MagicMock(return_value=(709, "cosiek", 177.0))
        assert_that(self.mockClass.add_item()).is_equal_to((709, "cosiek", 177.0))
    def test_magicMockClass_add_client(self):
        self.mockClass.add_client = MagicMock(return_value=(7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
        assert_that(self.mockClass.add_client()).is_equal_to((7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
    def test_magicMockClass_add_item_to_order(self):
        self.mockClass.add_client = MagicMock(return_value=())
        assert_that(self.mockClass.add_client(2,3)).is_equal_to(())
    def test_magicMockClass_add_order(self):
        self.mockClass.add_order = MagicMock(return_value=(2,3))
        assert_that(self.mockClass.add_order()).is_equal_to((2,3))
    def test_magicMockClass_delete_item_from_order(self):
        self.mockClass.delete_item_from_order = MagicMock(return_value=())
        assert_that(self.mockClass.delete_item_from_order(2,3)).is_equal_to(())