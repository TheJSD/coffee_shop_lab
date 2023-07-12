import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink_mocha = Drink("Mocha", 10, 25)

    def test_drink_name(self):
        self.assertEqual("Mocha", self.drink_mocha.name)

    def test_drink_price(self):
        self.assertEqual(10, self.drink_mocha.price)