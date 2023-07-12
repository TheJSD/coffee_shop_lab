import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Mocha", 10)

    def test_drink_name(self):
        self.assertEqual("Coke", self.drink.name)