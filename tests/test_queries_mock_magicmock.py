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
        self.mockClass.get_clients = Mock(return_value=[(1,"Bob","Bobinovich","example.example@example.com"),
                                                        (2,"Bobin","Bobinin","example.example@example.com")])
        assert_that(self.mockClass.get_clients()).is_equal_to([(1,"Bob","Bobinovich","example.example@example.com"),
                                                        (2,"Bobin","Bobinin","example.example@example.com")])
    def test_mockClass_get_items(self):
        self.mockClass.get_items = MagicMock(return_value=[(1,"Bob",777),(2,"Bobin",73477)])
        assert_that(self.mockClass.get_items()).is_equal_to([(1,"Bob",777),(2,"Bobin",73477)])
    def test_mockClass_get_orders(self):
        self.mockClass.get_orders = MagicMock(return_value=[(1,2),(2,1)])
        assert_that(self.mockClass.get_orders()).is_equal_to([(1,2),(2,1)])