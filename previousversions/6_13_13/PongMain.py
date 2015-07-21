import pygame, sys, os
from pygame.locals import *

class PongPage:

	def __init__(self, screen, clock, statusBar):
		print "pong page initialized"
		self.statusBar = statusBar
		self.running = False
		self.screen = screen

		
		self.clock = clock
		self.mainScreenOrigin = ((0,screen.get_height()/10))
		self.mainScreenSize = ((screen.get_width(), screen.get_height() - (screen.get_height()/10)))
		
		self.background = pygame.image.load(os.path.join('imgs', 'mainbackground.jpg'))
		self.background = pygame.transform.scale(self.background, (self.mainScreenSize))
		
		
	def draw(self):
		self.screen.blit(self.background, (self.mainScreenOrigin))
		
		
		self.statusBar.update()
		pygame.display.flip()
		
	def update(self):
		self.draw()
	
	
	def pongMainLoop(self):
		while 1:
			for event in pygame.event.get():
			
			###keydown events
				if event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						sys.exit()
					if event.key == K_BACKSPACE:
						self.running = False
			###

			###other events
			
			###
			
			###loop logic
			self.update()
			if not self.running:
				break
			###
			
	def begin(self):
		self.running = True
		self.pongMainLoop()