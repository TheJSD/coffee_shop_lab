import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100)
        self.customer = Customer("Paul", 25)
        self.drink = Drink("Mocha", 10)


    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    # @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)
    
    def test_coffee_shop_increase_till(self):
        self.coffee_shop.change_till_by_amount(10)
        self.assertEqual(110, self.coffee_shop.till)
    
    def test_coffee_shop_decrease_till(self):
        self.coffee_shop.change_till_by_amount(-10)
        self.assertEqual(90, self.coffee_shop.till)
    
    def test_coffee_shop_sell_drink(self):
        self.coffee_shop.sell_drink(self.customer, self.drink)
        self.assertEqual(110, self.coffee_shop.till)
        self.assertEqual(15, self.customer.wallet)