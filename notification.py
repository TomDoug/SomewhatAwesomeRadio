import pygame, os

class Notification():
	def __init__(self, iconLocation):
		self.width = 0
		self.icon = pygame.image.load(os.path.join('imgs',iconLocation))
		
	def update(self):
		print "notification updated"
		
	def getIcon(self):
		return self.icon

class Message(Notification):
	def __init__(self, iconLocation):
		Notification.__init__(self, iconLocation)
		self.width = 40
	def update(self):
		print "Message updated"
		