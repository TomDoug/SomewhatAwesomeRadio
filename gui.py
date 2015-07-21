import pygame, sys, os, UDPserver
import posixpath
import SportsMain, WeatherMain, MusicMain, PongMain, MessagesMain
import CalcVariables, MenuAnimation
from stausBar import *
from pygame.locals import *

#Settings variables:

desktop_ip_address = "127.0.0.1" #Use "127.0.0.1" when running the server ang gui on the same computer




size = width, height = 600, 400
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
font = pygame.font.Font(None, 36)	

class MainMenu:

	def __init__(self):
		self.statusBar = StatusBar(screen)
		self.previousSelection = 0
		self.calcVars = CalcVariables.CalcVars(width, height)
		self.animGen = MenuAnimation.AnimationGenerator(self.calcVars)
		
		self.LEFT = 0
		self.RIGHT = 1
		self.whichDirection = 0
		self.currentSelection = 1
		
		self.clock = pygame.time.Clock()
		self.loadIcons()
						
		self.background = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'mainbackground.jpg')), (width, self.animGen.calcVars.mainHeight))
		
		self.isChanging = False
		self.changeFrameCounter = 1.0
		self.changeCounterIncreasing = True
		
		self.otherScreens = [WeatherMain.WeatherPage(screen, self.clock, self.statusBar), MusicMain.MusicPage(screen, self.clock, self.statusBar), SportsMain.SportsPage(screen, self.clock, self.statusBar, self.animGen), PongMain.PongPage(screen, self.clock, self.statusBar), MessagesMain.MessagesPage(screen, self.clock, self.statusBar, self.animGen)]
		
		self.mainLoop()
		
	def loadIcons(self):
		self.icons = [self.loadImage('weather.png'), self.loadImage('music.png'), self.loadImage('sports.png'), self.loadImage('pong.png'), self.loadImage('messages.png')]
		
	def loadImage(self, path):#needs to be changed for linux
		dir = os.path.dirname(__file__)
		return pygame.image.load(os.path.join(dir,'imgs/' + path))
					
	def processSelection(self):
		self.otherScreens[self.currentSelection].begin()
		
	def mainLoop(self):
		while 1:
			self.clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
					
				if event.type == pygame.KEYDOWN:
					if event.key == K_RIGHT:
						if not self.isChanging:
							self.whichDirection = self.RIGHT
							self.previousSelection = self.currentSelection
							self.isChanging = True
							if self.currentSelection < len(self.icons)-1:
								self.currentSelection += 1
							else:
								self.currentSelection = 0
						
					
					if event.key == K_LEFT:
						if not self.isChanging:
							self.whichDirection = self.LEFT
							self.isChanging = True
							self.previousSelection = self.currentSelection
							if self.currentSelection > 0:
								self.currentSelection -= 1
							else:
								self.currentSelection = len(self.icons)-1
						
					if event.key == K_ESCAPE:
						sys.exit()
					if event.key == K_RETURN:
						self.processSelection()
			
			screen.blit(self.background,(0,self.animGen.calcVars.mainHeightOrigin))
			if not self.isChanging:
				self.animGen.paintImages(screen, self.icons, self.currentSelection)
			else:
				self.animGen.animateChange(screen, self.icons, self.previousSelection, self.whichDirection, self.changeFrameCounter)
				if self.changeFrameCounter < self.animGen.calcVars.numberOfChangeFrames:
					self.changeFrameCounter += 1
				else:
					self.changeFrameCounter = 1
					self.isChanging = False
			self.statusBar.update()
			pygame.display.update((0, self.calcVars.mainImageOrigin[1], self.calcVars.width, self.calcVars.imageHeight))
			
if __name__ == "__main__":
	pygame.init()
	s = UDPserver.server()
	s.daemon = True
	s.start()
	
	screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
	font = pygame.font.Font(None, 36)
	main = MainMenu()