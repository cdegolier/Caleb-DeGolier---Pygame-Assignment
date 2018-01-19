import pygame, sys
from pygame.locals import *

#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
STONE = 5

#imports images for the different blocks
textures = {
	DIRT : pygame.image.load('images/dirt.png'),
	GRASS: pygame.image.load('images/grass.png'),
	WATER: pygame.image.load('images/water.png'),
	COAL : pygame.image.load('images/coal.png'),
	LAVA : pygame.image.load('images/lava.png'),
	STONE : pygame.image.load('images/stone.png')
	}

#a list representing our tilemap
tilemap=[
		[GRASS, COAL, DIRT, LAVA, WATER],
		[WATER, WATER, GRASS, LAVA, WATER],
		[COAL, GRASS, COAL, STONE, STONE],
		[DIRT, GRASS, GRASS, GRASS, WATER],
		[GRASS, GRASS, WATER, WATER, LAVA]
		]

#game dimentions
TILESIZE = 20
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
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

	#UPDATE THE DISPLAY
	pygame.display.update()
