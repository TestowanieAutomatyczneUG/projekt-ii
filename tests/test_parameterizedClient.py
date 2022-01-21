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

    def test_client_init_wrong_lastName(self):
        assert_that(Client).raises(ValueError).when_called_with(self.client.id, self.client.firstName, self.wrongValueString, self.client.email)



    def test_client_init_wrong_firstName(self):
        assert_that(Client).raises(ValueError).when_called_with(self.client.id, self.wrongValueString, self.client.lastName, self.client.email)

    def test_client_init_wrong_email(self):
        assert_that(Client).raises(ValueError).when_called_with(self.client.id, self.client.firstName, self.client.lastName, self.wrongValueString)

    def test_client_delete_client_wrong_id(self):
        assert_that(Client.delete_client).raises(ValueError).when_called_with(self.wrongValueInt)

    def test_edit_client_lastname_wrong_lastname(self):
        assert_that(self.client.edit_lastName).raises(ValueError).when_called_with(self.wrongValueString)

    def test_client_remove_order_wrong_id(self):
        assert_that(self.client.delete_order).raises(ValueError).when_called_with(self.wrongValueInt)

    def test_client_add_order_wrong_id(self):
        assert_that(self.client.add_order).raises(ValueError).when_called_with(self.wrongValueInt)

    def test_edit_client_name_wrong_name(self):
        assert_that(self.client.edit_firstName).raises(ValueError).when_called_with(self.wrongValueString)

    def test_edit_client_email_wrong_email(self):
        assert_that(self.client.edit_email).raises(ValueError).when_called_with(self.wrongValueString)

    def test_find_client_wrong_id(self):
        assert_that(Client.find_client).raises(ValueError).when_called_with(self.wrongValueInt)


    def tearDown(self):
        del self.client
