class CoffeeShop:
	
	def __init__(self, name, till):
		self.name = name
		self.till = till

	def change_till_by_amount(self, amount):
		self.till += amount

	def sell_drink(self, customer, drink):

		drink_price = customer.buy_drink(drink)
		self.change_till_by_amount(drink_price)

	def age_check(self, customer):
		result = customer.get_age()
		if result < 16:
			return False #under 16
		if result >= 16:
			return True #16 or over