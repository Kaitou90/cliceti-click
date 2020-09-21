from __future__ import print_function
from datetime import datetime
import time
import pygame

##### INITIATING PARAMS #####
game_start = datetime.now()

count, coin, coinsPerSec = 0, 0, 0
active = True
building = {
	"farm": {
		"amount": 3,
		"coinPerBuilding": 0.5
	},
	"inn": {
		"amount": 5,
		"coinPerBuilding": 2
	},
}

##### STARTING THE GAME LOOP #####

gameStart = pygame.init()
dameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('clicketi-click game')

clock = pygame.time.Clock()
crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		print(event)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()





# count how much coins buildings are producing in second
for x in building:
	print(x)
	print(building[x]["coinPerBuilding"])
	coinsPerSec += building[x]["coinPerBuilding"] * building[x]["amount"]
	print('coins per second ' , coinsPerSec)


# coin production calculator; total amount of coins
while (active):
	print(count )
	print("coin ", coin )

	time.sleep(1)
	count += 1
	coin += coinsPerSec


#


