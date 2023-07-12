class Customer:
    def __init__(self, name, wallet, age, energy):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = energy

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink):
        drink_price = drink.price
        self.reduce_wallet(drink_price)
        self.energy += drink.caffeine_level
        return drink_price
    
    def get_age(self):
        return self.age
    
    def get_energy(self):
        return self.energy
    