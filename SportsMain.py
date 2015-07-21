import pygame, sys, os
from pygame.locals import *
import Sports

class SportsPage:

	def __init__(self, screen, clock, statusBar, animGen):
		self.LEFT = 0
		self.RIGHT = 1
		print "sports page initialized"
		self.statusBar = statusBar
		self.screen = screen
	
		self.icons = self.loadIcons()
		self.currentSelection = 0
		self.whichDirection = 0
		self.running = False
		
		self.isChanging = False
		self.changeFrameCounter = 1.0
		self.changeCounterIncreasing = True
		
		self.animGen = animGen
		
		self.clock = clock
		
		
		self.background = pygame.image.load(os.path.join('imgs', 'mainbackground.jpg'))
		self.background = pygame.transform.scale(self.background, (self.animGen.calcVars.width, self.animGen.calcVars.mainHeight))
		
	def loadIcons(self):
		return [self.loadImage('NFL.jpg'), self.loadImage('NHL.jpg'), self.loadImage('NBA.jpg'), self.loadImage('MLB.jpg')]
		
	def loadImage(self, path):
		print os.path.join('/imgs',path)
		return pygame.image.load(os.path.join('imgs',path.strip()))
			
	def sportScreen(self, spo):
		#pygame.draw.rect(self.screen, (0,0,0), (0,0, self.width, self.height), 0)
		
		#dims background with alpha (not available on draw.rect)
		s = pygame.Surface((self.animGen.calcVars.width,self.animGen.calcVars.height))
		s.set_alpha(128)
		s.fill((0,0,0))
		self.screen.blit(s, (0,0))



		scoreImg = []
		sco = []
		if spo == 'nhl':
			sco = self.sportScores.getNHLScores()
		elif spo == 'nfl':
			sco = self.sportScores.getNFLScores()
		elif spo == 'nba':
			sco = self.sportScores.getNBAScores()
		elif spo == 'mlb':
			sco = self.sportScores.getMLBScores()
			
		for i in sco:
			scoreImg.append(self.font.render(str(i),1,(255,255,255)))
			#print i
		x = 10
		y = 10
		for i in scoreImg:
			self.screen.blit(i,(x,y))
			y += 20
		pygame.display.flip()
		run = True
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mp.sendMessage("quit")
					sys.exit()
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					run =False
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					mp.sendMessage("quit")
					sys.exit()
	
	def sportsMainLoop(self):
		while 1:
			self.clock.tick(30)
			for event in pygame.event.get():
			
			###keydown events
				if event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						sys.exit()
					if event.key == K_BACKSPACE:
						self.running = False
						
					if event.key == K_RIGHT:
						if not self.isChanging:
							self.whichDirection = self.RIGHT
							self.isChanging = True
							self.previousSelection = self.currentSelection
							
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

					if event.key == K_RETURN:
						if self.currentSelection == 0:
							self.sportScreen('nfl')
						elif self.currentSelection == 1:
							self.sportScreen('nhl')
						elif self.currentSelection == 2:
							self.sportScreen('nba')
						elif self.currentSelection == 3:
							self.sportScreen('mlb')

						
					if event.type == KEYDOWN and event.key == K_BACKSPACE:				
						break
			###

			###other events
			
			###
			
			###loop logic
			self.screen.blit(self.background,(0,self.animGen.calcVars.mainHeightOrigin))

			if not self.isChanging:
				self.animGen.paintImages(self.screen, self.icons, self.currentSelection)
			else:
				self.animGen.animateChange(self.screen, self.icons, self.previousSelection, self.whichDirection, self.changeFrameCounter)
				if self.changeFrameCounter < self.animGen.calcVars.numberOfChangeFrames: #are we done sliding?
					self.changeFrameCounter += 1
				else:
					self.changeFrameCounter = 1 
					self.isChanging = False
			self.statusBar.update()
			pygame.display.flip()
			if not self.running:
				break
			
	def begin(self):
		self.font = pygame.font.Font(None, 36)
		self.sportScores = Sports.Sports()
		self.running = True
		self.sportsMainLoop()
