
class Building():

	def __init__(self, name, count, basePrice, coinsPerBuilding, alignment, boosts=0, image=''):
		self.name = name
		self.count = count
		self.basePrice = basePrice
		self.coinsPerBuilding = coinsPerBuilding
		self.alignment = alignment
		self.image = image
		self.boosts = boosts
	
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
		return self.coinPerBuilding * self.count
	
	def get_building_info:
		pass

	def get_all_buildings_info:
		pass