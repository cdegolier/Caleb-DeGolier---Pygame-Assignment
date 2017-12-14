#import the pygame and sys module
import pygame, sys

#imports useful constants
from pygame.locals import *

#initialize pygame module
pygame.init()

#create a new drawing surface, width=300 height=300
DISPLAYSURF = pygame.display.set_mode((300,300))
#givve the window a caption
pygame.display.set_caption('My First Game')

#loop to repeat forever
while True:
	#get all the user events
	for event in pygame.event.get():
		#if the user wants to quit
		if event.type == QUIT:
			#ends game and module
			pygame.quit()
			sys.exit()
	#draws a green (RGB) rectangle on DISPLAYSURF at 150 (x), 50 (y) and the side legnths (20 x 20)
	pygame.draw.rect(DISPLAYSURF, (0,255,0), (100,50,20,20))
	#draws varying rectangles
	pygame.draw.rect(DISPLAYSURF, (255,255,0), (150,50,20,20))
	pygame.draw.rect(DISPLAYSURF, (255,0,120), (20,60,20,20))
	pygame.draw.rect(DISPLAYSURF, (0,0,135), (220,250,20,20))
	#updates the display
	pygame.display.update()
