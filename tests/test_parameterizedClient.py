import unittest
from assertpy import *
from src.client import *
from parameterized import *
from unittest.mock import *

@parameterized_class(( 'wrongValueInt','wrongValueString', 'wrongValueFloat'), [
    (True, False, True),
    (None,None,None),
    ("Robert",-8.0, 9),
    ("", "", ""),
    ("Cosiek", 0, "łosiek"),
    ([9,3,6], [6,3,9], [3,9,6]),
    ("Bobert", 9.9,1 ),
    ({'firstName': 8, 'lastName': 2,'thirdName':3}, {'firstName': 90, 'lastName': 5,'thirdName':4}, {'firstName': 77, 'lastName': 777,'thirdName':5}),
])
class TestsParametrizedClient(unittest.TestCase):

    def setUp(self):
        def mock_get_client_orders():
            return [(1,2,3,4)]
        def mock_get_clients():
            return [(7, "Bob", "Bobinovich", "BobMonkeyGmailCom")]
        Queries.find_client = Mock(return_value=(7, "Bob", "Bobinovich", "BobMonkeyGmailCom"))
        Client.clients = []
        Order.orders = []
        self.client = Client(mock_get_clients()[0][0], mock_get_clients()[0][1], mock_get_clients()[0][2], mock_get_clients()[0][3])
        order = Order(mock_get_client_orders()[0][0], mock_get_client_orders()[0][1])
        self.client.orders.append(order)



    def tearDown(self):
        del self.client
