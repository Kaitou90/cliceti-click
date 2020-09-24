from __future__ import print_function
from datetime import datetime
import time
import pygame

##### INITIATING PARAMS #####

gameStart = pygame.init()


display_width = 800
display_height = 600

game_start = datetime.now()

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


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('clicketi-click game')

##### GAME LOGIC / FUNCTIONS #####

# count how much coins buildings are producing in second
def coinsCounter(building):
	coinsPerSec = 0
	for x in building:
		coinsPerSec += building[x]["coinPerBuilding"] * building[x]["amount"]
	return coinsPerSec

def text_block(coin):
		font = pygame.font.SysFont(None, 25)
		text = font.render("Coin counter: "+str(coin), True, black)
		gameDisplay.blit(text,(0,0))



##### STARTING THE GAME LOOP #####
def game_loop():

	clock = pygame.time.Clock()
	gameExit = False

	coinsPerSec = coinsCounter(building)
	coin = 0

	print(coinsPerSec)

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True


		gameDisplay.fill(white)

		text_block(coin)

		coin += coinsPerSec

		pygame.display.update()
		clock.tick(1)

##### END OF GAME LOOP #####


##### START THE GAME #####
game_loop()
pygame.quit()
quit()

