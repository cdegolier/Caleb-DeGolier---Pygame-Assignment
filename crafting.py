import pygame, sys, random
from pygame.locals import *
fpsClock = pygame.time.Clock()


BLACK = (0,0,0)
pygame.display.set_icon(pygame.image.load('images/player.png'))

#constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
STONE = 5
DIAMOND = 6
FIRE = 7
SAND = 8
BRICK = 9
CLOUD = 10

#imports images for the different blocks
textures = {
	DIRT : pygame.image.load('images/dirt.png'),
	GRASS: pygame.image.load('images/grass.png'),
	WATER: pygame.image.load('images/water.png'),
	COAL : pygame.image.load('images/coal.png'),
	LAVA : pygame.image.load('images/lava.png'),
	STONE : pygame.image.load('images/stone.png'),
	DIAMOND : pygame.image.load('images/diamond.png'),
	FIRE : pygame.image.load('images/fire.png'),
	SAND : pygame.image.load('images/sand.png'),
	BRICK : pygame.image.load('images/brick.png'),
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
	FIRE : 0,
	SAND : 0,
	BRICK : 0,
}

# maps each resource to number event keys used to place/craft the resource
controls = {
    DIRT  : 49,     # event 49 is 1 key
    GRASS : 50,     # event 50 is 2 key
    WATER : 51,     # event 51 is 3 key
    COAL  : 52,     # event 52 is 4 key
    STONE : 53,     # event 53 is 5 key
    LAVA  : 54,     # event 54 is 6 key
    FIRE  : 56,     # event 55 is 8 key
    SAND  : 57,     # event 56 is 9 key
    BRICK : 45      # event 49 is - key
}

craft = {
    FIRE  : { COAL: 1},
    SAND  : { DIRT:  1,  STONE: 1},
    BRICK : { STONE: 1,  SAND: 1}
}
	
#game dimensions
TILESIZE = 20
MAPWIDTH = 50
MAPHEIGHT = 25

#player constant 
PLAYER = pygame.image.load('images/player.png')
#position of the player (x,y)
playerPos = [0,0]

#lists resources for textures
resources = [DIRT, GRASS, WATER, COAL, LAVA, STONE, DIAMOND]

#CLOUD POSITION
# fixed x offscreen
cloud_x_pos = [-200, -500, -1000]
# random y pos
cloud_y_pos = [random.randint(0, MAPHEIGHT*TILESIZE - 1), random.randint(0, MAPHEIGHT*TILESIZE - 1), random.randint(0, MAPHEIGHT*TILESIZE - 1)]

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
	pygame.display.set_caption('M I N E C R A F T -- 2 D')
	DISPLAYSURF.fill(BLACK)
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
				
			# PLACE RESOURCES FROM INVENTORY. SWAP WITH RESOURCE WHERE PLAYER STANDING
			for key in controls:
				if (event.key == controls[key]):
					# if craft key pressed
					if key in craft:
						# initialize to true
						canBeMade = True
						# check to see if there are enough resources in inventory to craft item
						for each in craft[key]:
							# if not enough resources in inventory
							if craft[key][each] > inventory[each]:
								# cannot craft item
								canBeMade = False
							# if enough available resources, craft item
							if canBeMade == True:
								# remove each ingredient from craft recipe
								for i in craft[key]:
									inventory[i] -= craft[key][i]
									# add crafted item to inventory
									inventory[key] += 1
									# place item of key pressed
					else:
						# if there is at least one item in inventory
						if inventory[key] > 0:
							# get tile to swap with item
							standing_tile = tilemap[playerPos[1]][playerPos[0]]
							# increase inventory by standing tile
							inventory[standing_tile] += 1
							# remove item to place from inventory
							inventory[key] -= 1
							# place item from inventory
							tilemap[playerPos[1]][playerPos[0]] = key

	
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
		textObj = INVFONT.render(str(inventory[item]), True, (255,0,10), (0,0,0))
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 50
	
	# DISPLAY CLOUDS
	# display each instance of a cloud
	for each in range(len(cloud_x_pos)):
		# display cloud on screen
		DISPLAYSURF.blit(textures[CLOUD], (cloud_x_pos[each], cloud_y_pos[each]))
		# move cloud to right slightly
		cloud_x_pos[each] += 1
		# once cloud moves to end of map
		if cloud_x_pos[each] > MAPWIDTH*TILESIZE:
			# randomly pick a new position to place the cloud (clouds in random frequency and position)
			# random x distance offscreen
			cloud_x_pos[each] = -random.randint(0, 450)
			# random y pos
			cloud_y_pos[each] = random.randint(0, MAPHEIGHT*TILESIZE - 1)


	#UPDATE THE DISPLAY
	pygame.display.update()
	fpsClock.tick(24)
