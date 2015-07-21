import pygame, sys, os
from pygame.locals import *
import notification, MenuAnimation

class MessagesPage:

	def __init__(self, screen, clock, statusBar, animGen):
		self.animGen = animGen
		print "messages page initialized"
		self.statusBar = statusBar
		self.running = False
		self.screen = screen
		self.messages = []

		
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
	
	
	def messagesMainLoop(self):
		while 1:
			for event in pygame.event.get():
			
			###keydown events
				if event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						sys.exit()
					if event.key == K_BACKSPACE:
						self.running = False
					if event.key == K_UP:
						notif = notification.Message("message.jpg")
						self.statusBar.addNotification(notif)
						self.messages.append(notif)
					if event.key == K_DOWN:
						try:
							notif = self.messages[len(self.messages)-1]
							self.statusBar.removeNotification(notif)
							self.messages.remove(notif)
						except:
							print "Error, Notification not in status bar"
					
		

						
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
		self.messagesMainLoop()