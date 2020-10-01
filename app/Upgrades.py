
class Upgrades():

	def __init__(self, name, description, price, affect, effect, conditions='', bought=False):
		self.name = name
		self.description = description
		self.price = price
		self.conditions = conditions
		self.bought = bought
		self.affect = affect
		self.effect = effect

	def check_conditions(self):
		pass

	def buy_upgrade(self):
		if check_conditions() == True:
			money - price
			self.bought = True

	def get_all_upgrades():
		pass
