from __future__ import print_function
from datetime import datetime
import pygame
from app.building import Building

##### INITIATING PARAMS #####

gameStart = pygame.init()


display_width = 800
display_height = 600


active = True
bulk = ["1", "10", "100", "1000", "smart", "max"]
buildings = {
	"farm": {
		"amount": 3,
		"coinPerBuilding": 0.5
	},
	"inn": {
		"amount": 5,
		"coinPerBuilding": 2
	},
	"blacksmith": {
		"amount": 5,
		"coinPerBuilding": 3
	},
}

spells = {
	"tax collection": {
		"manaRequired": 200,
		"description": ""
	},
	"production boost": {
		"manaRequired": 400,
		"description": "",
	},
	"gem power": {
		"manaRequired": 1000,
		"description": ""
	}
}

upgrades = {
	"farm production I": {
		"cost": 500,
		"description": "",
		"affect": "farms",
		"effect": "100%"
	},
	"farm production II": {
		"cost": 500,
		"description": "",
		"affect": "farms",
		"effect": "100%"
	},
	"farm production III": {
		"cost": 500,
		"description": "",
		"affect": "farms",
		"effect": "100%"
	},
	"farm production IV": {
		"cost": 500,
		"description": "",
		"affect": "farms",
		"effect": "100%"
	},
	"farm production V": {
		"cost": 500,
		"description": "",
		"affect": "farms",
		"effect": "100%"
	}
}
bulkIterator = 0


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
def coinsCounter(buildings):
	coinsPerSec = 0
	for x in buildings:
		coinsPerSec += buildings[x]["coinPerBuilding"] * buildings[x]["amount"]
	return coinsPerSec

def text_block(coin, posX, posY):
		font = pygame.font.SysFont(None, 25)
		text = font.render("Coin counter: "+str(coin), True, black)
		gameDisplay.blit(text, (posX,posY))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def button_object(btname, x, y, w, h, pgmain, pghover, clickX=0, clickY=0, action=None):
	mouse = pygame.mouse.get_pos()

	# fix this; mouse hover effect
	if x+w > mouse[0] > x and y+h > mouse[1] > y :
		pygame.draw.rect(gameDisplay, pghover,(x,y,w,h))

	else:
		pygame.draw.rect(gameDisplay, pgmain,(x,y,w,h))

	if action is not None and x+w > clickX > x and y+h > clickY > y :
		print(btname)
		action()

	btnSurf, btnText = text_objects(btname, pygame.font.Font("freesansbold.ttf",20))
	btnText.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(btnSurf, btnText)

def btn_building(btname, x, y, w, h, pgmain, pghover, clickX=0, clickY=0, action=None):


	button_object(btname, x, y, w, h, pgmain, pghover, clickX, clickY, action)


# Button click action to add iteration number to bulk buy button
def bulkIterationFunc():
	global bulkIterator

	if bulkIterator >= 5:
		bulkIterator = 0
	else:
		bulkIterator +=1

##### STARTING THE GAME LOOP #####
def game_loop():

	gameStart = datetime.now()
	timeCounter = datetime.now()

	clock = pygame.time.Clock()
	gameExit = False

	coinsPerSec = coinsCounter(buildings)
	coin = 0

	print(coinsPerSec)

	#infinit loop
	while not gameExit:
		clickX, clickY = 0, 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.MOUSEBUTTONUP:
				clickX, clickY = event.pos

		mouse = pygame.mouse.get_pos()

		# actions and events that are hapening every second
		if (datetime.now() - timeCounter).total_seconds() > 0.99 :
			timeCounter = datetime.now()
			# if timeCounter - datetime.now()
			coin += coinsPerSec
			#print(timeCounter )


		##### PYGAME DRAWING FUNCTIONALITY #####
		gameDisplay.fill(white)

		text_block(coin, 0, 0)

		# Upgrades display on left side of the screen
		upgradesBtnY = 100
		for upgrade in upgrades:
			button_object(upgrade, 50, upgradesBtnY, 50, 50, red, bright_red, clickX, clickY)
			upgradesBtnY += 55

		# buy more in bulk
		button_object(bulk[bulkIterator], 400, 500, 100, 50, red, bright_red, clickX, clickY, bulkIterationFunc)

		# Mana and spells on right side of the screen
		spellBtnY = 100
		for spell in spells:
			button_object(spell, 400, spellBtnY, 100, 50, red, bright_red, clickX, clickY)
			spellBtnY += 55

		# Constructions on right side of the screen
		buildingBtnY = 100
		for x in buildings:
			button_object(x, 550, buildingBtnY, 150, 50, red, bright_red, clickX, clickY)
			buildingBtnY += 55

		##### KEEP THESE AT BOTTOM OF GAME LOOP
		pygame.display.update()
		clock.tick(60)

##### END OF GAME LOOP #####


##### START THE GAME #####
game_loop()
pygame.quit()
quit()

