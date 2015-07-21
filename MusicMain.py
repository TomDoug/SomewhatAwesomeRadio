import pygame, sys, os
from pygame.locals import *
import urllib2
from pprint import pprint

class MusicPage:

	def __init__(self, screen, clock, statusBar):
		self.online = False
		
		print "music page initialized"
		self.statusBar = statusBar
		self.running = False
		self.screen = screen
		
		self.songs = []
		self.artists = []
		
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
	def getSongs(self):
		songString = urllib2.urlopen('http://127.0.0.1/pi/songs').read()
		artistString = urllib2.urlopen('http://127.0.0.1/pi/artist').read()
		
		more = True
		while more:
			if len(songString) > 0:
				self.songs.append(songString[:songString.find("<br>")])
				songString = songString[songString.find("<br>")+4:]
				print len(songString)
			else:
				more = False
				
		more = True
		while more:
			if len(artistString) > 0:
				self.artists.append(artistString[:artistString.find("<br>")])
				artistString = artistString[artistString.find("<br>")+4:]
				print len(artistString)
			else:
				more = False
		pprint(self.artists)
	
	def musicMainLoop(self):
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
		self.getSongs()
		self.musicMainLoop()
