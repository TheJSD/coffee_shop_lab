import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Paul", 25)

    def test_customer_has_name(self):
        self.assertEqual("Paul", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(25, self.customer.wallet)
    
    def test_customer_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(15, self.customer.wallet)