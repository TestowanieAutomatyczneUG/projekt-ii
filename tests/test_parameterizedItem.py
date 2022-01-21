import unittest
from assertpy import *
from src.item import *
from parameterized import *
from unittest.mock import *

@parameterized_class(('wrongValueInt','wrongValueString', 'wrongValueFloat'), [
    (True, False, True),
    (None, None, None),
    ("Robert", -8.0, 9),
    ("", "", ""),
    ("Cosiek", 0, "łosiek"),
    ([9, 3, 6], [6, 3, 9], [3, 9, 6]),
    ("Bobert", 9.9, 1),
    ({'firstName': 8, 'lastName': 2, 'thirdName': 3}, {'firstName': 90, 'lastName': 5, 'thirdName': 4},
     {'firstName': 77, 'lastName': 777, 'thirdName': 5}),
])
class TestsParametrizedItem(unittest.TestCase):

    def setUp(self):
        def mock_get_items():
            return [(709, "cosiek", 177.0)]
        Item.itemy = []
        self.item = Item(mock_get_items()[0][0], mock_get_items()[0][1], mock_get_items()[0][2])