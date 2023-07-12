class CoffeeShop:
	
	def __init__(self, name, till):
		self.name = name
		self.till = till

	def change_till_by_amount(self, amount):
		self.till += amount



	def age_check(self, customer):
		result = customer.get_age()
		if result < 16:
			return False #under 16
		if result >= 16:
			return True #16 or over
		
	def energy_check(self, customer):
		result = customer.get_energy()
		if result >= 100:
			return False # refuse anyone 100 energy or above
		if result <100:
			return True # can serve anyone below 100 energy
		
	def sell_drink(self, customer, drink):
		check_age_result = self.age_check(customer)
		if check_age_result == False:
			return "Customer is underage"
		drink_price = customer.buy_drink(drink)
		self.change_till_by_amount(drink_price)