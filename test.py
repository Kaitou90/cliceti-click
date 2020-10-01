from __future__ import print_function
from datetime import datetime
from app.building import Building


#name, count, basePrice, coinsPerBuilding, alignment, image
a = Building("farm", 3, 1, 0.5, 'neutral')
print('price for next 7 buildings: ')
print(a.building_cost(7, 0.02))

print('price for next 100 buildings: ')
print(a.building_cost(100, 0.02))

print('price for next 500 buildings: ')
print(a.building_cost(500, 0.02))

print('price for next 1000 buildings: ')
print(a.building_cost(1000, 0.02))

print('price for next 60 buildings: ')
print(a.building_cost(60, 0.02))

print('price for next 2 buildings: ')
print(a.building_cost(2, 0.02))
