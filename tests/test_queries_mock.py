from unittest.mock import MagicMock
import unittest
from assertpy import *
from src.queries import *
from src.client import *
from src.item import *
from src.order import *

class TestsMock(unittest.TestCase):
    def setUp(self):
        self.mockClass = Queries()

    def test_mockClass_get_clients(self):
        self.mockClass.get_clients = Mock(return_value=[Client(1,"Bob","Bobinovich","example.example@example.com")])
        assert_that(self.mockClass.get_clients).is_equal_to([Client(1,"Bob","Bobinovich","example.example@example.com")])
    def test_mockClass_get_items(self):
        self.mockClass.get_items = MagicMock(return_value=[])
    def test_mockClass_get_orders(self):
        self.mockClass.get_orders = MagicMock(return_value=[])