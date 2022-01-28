from unittest.mock import MagicMock
import unittest
from src.queries import *

class TestsMock(unittest.TestCase):
    def setUp(self):
        self.mockClass = Queries()

    def test_mockClass_get_clients(self):
        self.mockClass.get_clients = MagicMock(return_value=[])
    def test_mockClass_get_items(self):
        self.mockClass.get_items = MagicMock(return_value=[])
    def test_mockClass_get_orders(self):
        self.mockClass.get_orders = MagicMock(return_value=[])