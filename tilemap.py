import pygame, sys
from pygame.locals import *

#constants representing colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0 ,0)
GREY = (169,169,169)

#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
ROCK = 5

#a dictionary linking colors to names
colors = {
	DIRT : BROWN,
	GRASS: GREEN,
	WATER: BLUE,
	COAL : BLACK,
	LAVA : RED,
	ROCK : GREY
	}

#a list representing our tilemap
tilemap=[
		[GRASS, COAL, DIRT, LAVA, WATER],
		[WATER, WATER, GRASS, LAVA, WATER],
		[COAL, GRASS, COAL, ROCK, ROCK],
		[DIRT, GRASS, GRASS, GRASS, WATER],
		[GRASS, GRASS, WATER, WATER, LAVA]
		]

#game dimentions
TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

while True:

	#get all user events
	for event in pygame.event.get():
		#if the user wants to quit
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	#loop through each row
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

	#UPDATE THE DISPLAY
	pygame.display.update()
