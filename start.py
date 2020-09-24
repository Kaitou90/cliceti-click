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
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('clicketi-click game')

##### GAME LOGIC / FUNCTIONS #####

# count how much coins buildings are producing total per second
def coinsCounter(building):
	coinsPerSec = 0
	for x in building:
		coinsPerSec += building[x]["coinPerBuilding"] * building[x]["amount"]
	return coinsPerSec

def text_block(coin, posX, posY):
		font = pygame.font.SysFont(None, 25)
		text = font.render("Coin counter: "+str(coin), True, black)
		gameDisplay.blit(text, (posX,posY))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

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

		mouse = pygame.mouse.get_pos()
		print(mouse)

		gameDisplay.fill(white)

		text_block(coin, 0, 0)

		if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
			pygame.draw.rect(gameDisplay, bright_red,(550,450,100,50))
		else :
			pygame.draw.rect(gameDisplay, red,(550,450,100,50))

		btnSurf, btnText = text_objects("GO!", pygame.font.Font("freesansbold.ttf",20))
		btnText.center = ( (550+(100/2)), (450+(50/2)) )
		gameDisplay.blit(btnSurf, btnText)

		coin += coinsPerSec

		pygame.display.update()
		clock.tick(60)

##### END OF GAME LOOP #####


##### START THE GAME #####
game_loop()
pygame.quit()
quit()

