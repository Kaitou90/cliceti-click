
class Building():

	def __init__(self, name, count, basePrice, coinsPerBuilding, alignment, boosts=0, image=''):
		self.name = name
		self.count = count
		self.basePrice = basePrice
		self.coinsPerBuilding = coinsPerBuilding
		self.alignment = alignment
		self.image = image
		self.boosts = boosts
		self.priceIncrease = 0.02
	
	def buy_buildings(self, money, multiplied=1, priceIncrease=0.02):
		price = building_cost(multiplied, priceIncrease)

		if money >= price:
			self.count += multiplied
			return money - price

	# uses sum of sequence to calculate the next building price
	# where n is number of the last building
	# multiplied refers to amount of buildings to be bought
	def building_cost(self, multiplied, priceIncrease):
		n = self.basePrice + (self.count+multiplied-1)*priceIncrease
		price = ( ( self.basePrice + n ) / 2 ) * multiplied

		return round(price, 2)

	# count how much coins this type of buildings are producing total per second
	def coins_counter(self):
		return self.coinsPerBuilding * self.count
	
	def get_building_info(self):
		maxOption = 12
		smartOption = 9
		buyOne = self.building_cost(1, self.priceIncrease)
		buyTen = self.building_cost(10, self.priceIncrease)
		buyHundred = self.building_cost(100, self.priceIncrease)
		buyMax = self.building_cost(maxOption, self.priceIncrease)
		buySmart = self.building_cost(smartOption, self.priceIncrease)

		hoverText = """{0}
cost for 1: {3}
cost for 10: {4}
cost for 100: {5}
cost for {1} (MAX): {6}
cost for {2} (SMART): {7}

Produces {8} coins per second.
All buildings produce {9} coins per second. ({10})
"""
		return hoverText.format(self.name.upper(), maxOption, smartOption, buyOne, buyTen, buyHundred, buyMax, buySmart, self.coinsPerBuilding, self.coins_counter(), '100%')

	def get_all_buildings_info():
		pass