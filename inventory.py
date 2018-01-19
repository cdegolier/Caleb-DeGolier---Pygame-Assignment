import pygame, sys, random
from pygame.locals import *

#colors
TEXTCOLOR = (255,0,10)
BLACK = (0,0,0)

#cloud position
cloudx = -200
cloudy = 0

#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
STONE = 5
DIAMOND = 6
CLOUD = 11

#imports images for the different blocks
textures = {
	DIRT : pygame.image.load('images/dirt.png'),
	GRASS: pygame.image.load('images/grass.png'),
	WATER: pygame.image.load('images/water.png'),
	COAL : pygame.image.load('images/coal.png'),
	LAVA : pygame.image.load('images/lava.png'),
	STONE : pygame.image.load('images/stone.png'),
	DIAMOND : pygame.image.load('images/diamond.png'),
	CLOUD : pygame.image.load('images/cloud.png')
	}
#creates an inventory for the player
inventory =	{
	DIRT : 0,
	GRASS : 0,
	WATER : 0,
	COAL : 0,
	STONE : 0,
	LAVA : 0,
	DIAMOND : 0,
}
	
#game dimentions
TILESIZE = 20
MAPWIDTH = 50
MAPHEIGHT = 25

#player constant 
PLAYER = pygame.image.load('images/player.png')
#position of the player (x,y)
playerPos = [0,0]

#lists resources for textures
resources = [DIRT, GRASS, WATER, COAL, LAVA, STONE, DIAMOND]

#a command to randomly generate a tilemap
tilemap = [[random.choice(resources) for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 50))

#add a font for inventory
INVFONT = pygame.font.Font('Bungee.ttf', 18)

#loops through the rows to change the chance of each block appearing
for rw in range(MAPHEIGHT):
	#loop through the columns
	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0,20)
		if randomNumber == 1 or randomNumber == 2:
			tile = WATER
		elif randomNumber == 0 or randomNumber == 11:
			tile = COAL
		elif randomNumber >= 3 and randomNumber <= 9:
			tile = GRASS
		elif randomNumber >=12 and randomNumber <= 14:
			tile = LAVA
		elif randomNumber == 15:
			tile = DIAMOND
		else:
			tile = DIRT
		#set the position of the tilemap to the randomly chosen tile
		tilemap[rw][cl] = tile

while True:

	#get all user events
	for event in pygame.event.get():
		#if the user wants to quit
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH -1:
				playerPos[0] += 1
			if (event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if (event.key == K_DOWN) and playerPos[1] < (MAPHEIGHT - 1):
				playerPos[1] += 1
			if (event.key == K_UP) and playerPos[1] > 0:
				playerPos [1] -=1
			if (event.key == K_SPACE):
				#what resource the player is currently standing on
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				#player now has one more
				inventory[currentTile] += 1
				#player now on dirt
				tilemap[playerPos[1]][playerPos[0]] = DIRT
				
			#placing dirt
			if event.key == K_1:
				#get the tile to swap with dirt
				currentTile = tilemap[playerPos[1]][ playerPos[0]]
				if inventory[DIRT] > 0:
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][ playerPos[0]] = DIRT
					inventory[currentTile] += 1
			
	
	#loop through each row
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

	#displays the player at current position
	DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))
	
	#displays inventory, starting at 10 pixels
	placePosition = 10
	for item in resources:
		#ADDS IMAGE 
		DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT*TILESIZE+20))
		placePosition += 30
		textObj = INVFONT.render(str(inventory[item]), True, TEXTCOLOR, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 50
		
	#displays the clouds
	DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloudx,cloudy))
	#moves left
	cloudx += 1
	if cloudx > MAPWIDTH*TILESIZE:
		cloudy = random.randint(0,MAPHEIGHT*TILESIZE)
		cloudx = -200
	
	#UPDATE THE DISPLAY
	pygame.display.update()
