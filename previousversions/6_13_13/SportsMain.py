import pygame, sys, os
from pygame.locals import *
import Sports
import gui2

class SportsPage:

	def __init__(self, screen, clock, statusBar):
		self.LEFT = 0
		self.RIGHT = 1
		print "sports page initialized"
		self.statusBar = statusBar
		self.running = False
		self.screen = screen
		self.animationTime = 0
		self.aTimeInc = True
		self.loadIcons()
		self.currentSelection = 0
		self.whichDirection = 0
		
		self.isChanging = False
		self.changeFrameCounter = 1.0
		self.numberOfChangeFrames = 15.0
		self.changeCounterIncreasing = True


		self.clock = clock
		self.mainScreenOrigin = ((0,screen.get_height()/10))
		self.mainWidth, self.mainHeight = self.mainScreenSize = ((screen.get_width(), screen.get_height() - (screen.get_height()/10)))

		self.imageHeight = int(self.mainScreenSize[1]*(.75))
		self.imageWidth = self.mainScreenSize[0]/2
		self.mainWidthOrigin, self.mainHeightOrigin = self.mainImageOrigin = ((screen.get_width()/2)-(self.imageWidth/2), ((self.mainScreenSize[1]/2)-(self.imageHeight/2))+self.mainScreenOrigin[1])
		
		self.padding = 0
		
		self.subImageWidth = int(self.imageWidth*.8)
		self.subImageHeight = int(self.imageHeight*.8)
		self.leftImageOrigin = (((-self.subImageWidth/2)-self.padding), ((self.mainScreenSize[1]/2)-(self.subImageHeight/2))+self.mainScreenOrigin[1])
		self.rightImageOrigin = ((screen.get_width()-(self.subImageWidth/2)+self.padding), ((self.mainScreenSize[1]/2)-(self.subImageHeight/2))+self.mainScreenOrigin[1])
		
		self.width = self.screen.get_width()
		self.height = self.screen.get_height()
		
		self.farRightOrigin = ((self.width+(self.subImageWidth/2)+self.padding), ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		self.farLeftOrigin = (((-self.subImageWidth/2)-self.padding)-self.subImageWidth, ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		
		
		self.background = pygame.image.load(os.path.join('imgs', 'mainbackground.jpg'))
		self.background = pygame.transform.scale(self.background, (self.mainScreenSize))
		
	def loadIcons(self):
		self.icons = [self.loadImage('nfl.jpg'), self.loadImage('nhl.jpg'), self.loadImage('nba.jpg'), self.loadImage('mlb.jpg')]
		#self.otherScreens = [WeatherMain.WeatherPage(screen, self.clock, self.statusBar), MusicMain.MusicPage(screen, self.clock, self.statusBar), SportsMain.SportsPage(screen, self.clock, self.statusBar), PongMain.PongPage(screen, self.clock, self.statusBar), MessagesMain.MessagesPage(screen, self.clock, self.statusBar)]
		
	def loadImage(self, path):
		#print os.path.join('imgs',path)
		return pygame.image.load(os.path.join('imgs',path))
		
	def draw(self):
		self.screen.blit(self.background, (self.mainScreenOrigin))
		
		if self.currentSelection > 0:
			left = self.currentSelection-1
		else:
			left = len(self.icons) - 1
		
		if self.currentSelection < len(self.icons)-1:
			right = self.currentSelection+1
		else:
			right = 0
			
		self.screen.blit(pygame.transform.scale(self.icons[left],(self.subImageWidth,self.subImageHeight)),self.leftImageOrigin)
		self.screen.blit(pygame.transform.scale(self.icons[right],(self.subImageWidth,self.subImageHeight)),self.rightImageOrigin)
		
		self.screen.blit(self.getAnimatedFrame(),self.mainImageOrigin)
		
		
		
		self.statusBar.update()
		pygame.display.flip()
		
	def getAnimatedFrame(self):
		img = self.icons[self.currentSelection]
		sur = pygame.Surface((self.imageWidth, self.imageHeight))
		sur.set_colorkey((255,1,255))
		pygame.draw.rect(sur,(255,1,255),(0,0,sur.get_width(),sur.get_height()),0)
		sur.blit(pygame.transform.scale(img,(self.imageWidth-self.animationTime, self.imageHeight-self.animationTime)),(self.animationTime/2,self.animationTime/2))
		return sur
		
	def animateChange(self):
		
		new = self.currentSelection
		self.screen.blit(self.background,(0,self.mainScreenOrigin[1]))
		pygame.draw.rect(self.screen,(255,1,255),(0,0,self.screen.get_width(),self.screen.get_height()/10),0)
		
		if self.whichDirection == self.RIGHT:
			old = new - 1
			leaving = old - 1
			entering = new + 1
			if entering > len(self.icons)-1:
				entering = entering - (len(self.icons))
			
			
			
			
			#image leaving screen
			leavingImageXDistance = self.leftImageOrigin[0] - self.farLeftOrigin[0]
			leavingImage = pygame.transform.scale(self.icons[leaving],(self.subImageWidth, self.subImageHeight))
			self.screen.blit(leavingImage,(self.leftImageOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*leavingImageXDistance), self.leftImageOrigin[1]))
			
			#old image
			oldImageXDistance = self.mainImageOrigin[0]-self.leftImageOrigin[0]
			oldImageYDistance = self.mainImageOrigin[1]-self.leftImageOrigin[1]
			oldImageTransformDistanceHeight = self.imageHeight - self.subImageHeight
			oldImageTransformDistanceWidth  = self.imageWidth - self.subImageWidth
			
			oldImage = pygame.transform.scale(self.icons[old],(int(self.imageWidth-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageTransformDistanceWidth)),int(self.imageHeight-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageTransformDistanceHeight))))
			self.screen.blit(oldImage,(self.mainImageOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageXDistance), self.mainImageOrigin[1]-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageYDistance)))
			
			#new image
			newImageXDistance = self.rightImageOrigin[0]-self.mainImageOrigin[0]
			newImageYDistance = self.mainImageOrigin[1]-self.rightImageOrigin[1]
			newImageTransformDistanceHeight = self.imageHeight - self.subImageHeight
			newImageTransformDistanceWidth  = self.imageWidth - self.subImageWidth
			
			newImage = pygame.transform.scale(self.icons[new],(int(self.subImageWidth + ((self.changeFrameCounter/self.numberOfChangeFrames)*newImageTransformDistanceWidth)),int(self.subImageHeight+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageTransformDistanceHeight))))
			self.screen.blit(newImage,(self.rightImageOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*newImageXDistance), self.rightImageOrigin[1]+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageYDistance)))
			
			#image entering screen
			enteringImageXDistance = self.farRightOrigin[0]-self.rightImageOrigin[0]
			enteringImage = pygame.transform.scale(self.icons[entering],(self.subImageWidth, self.subImageHeight))
			self.screen.blit(enteringImage,(self.farRightOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*enteringImageXDistance), self.leftImageOrigin[1]))
			
		else:
			old = new + 1
			leaving = old + 1
			entering = new - 1
			
			if old > len(self.icons)-1:
				old = old - (len(self.icons))
				
			if leaving > len(self.icons)-1:
				leaving = leaving - (len(self.icons))
				
				
			#image entering screen
			enteringImageXDistance = self.leftImageOrigin[0]-self.farLeftOrigin[0]
			enteringImage = pygame.transform.scale(self.icons[entering],(self.subImageWidth, self.subImageHeight))
			self.screen.blit(enteringImage,(self.farLeftOrigin[0]+((self.changeFrameCounter/self.numberOfChangeFrames)*enteringImageXDistance), self.leftImageOrigin[1]))
			

			#old image
			oldImageXDistance = self.mainImageOrigin[0]-self.rightImageOrigin[0]
			oldImageYDistance = self.mainImageOrigin[1]-self.rightImageOrigin[1]
			oldImageTransformDistanceHeight = self.imageHeight - self.subImageHeight
			oldImageTransformDistanceWidth  = self.imageWidth - self.subImageWidth
			
			oldImage = pygame.transform.scale(self.icons[old],(int(self.imageWidth-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageTransformDistanceWidth)),int(self.imageHeight-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageTransformDistanceHeight))))
			self.screen.blit(oldImage,(self.mainImageOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageXDistance), self.mainImageOrigin[1]-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageYDistance)))
			
			
			#new image
			newImageXDistance = self.mainImageOrigin[0]-self.leftImageOrigin[0]
			newImageYDistance = self.mainImageOrigin[1]-self.leftImageOrigin[1]
			newImageTransformDistanceHeight = self.imageHeight - self.subImageHeight
			newImageTransformDistanceWidth  = self.imageWidth - self.subImageWidth
			
			newImage = pygame.transform.scale(self.icons[new],(int(self.subImageWidth + ((self.changeFrameCounter/self.numberOfChangeFrames)*newImageTransformDistanceWidth)),int(self.subImageHeight+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageTransformDistanceHeight))))
			self.screen.blit(newImage,(self.leftImageOrigin[0]+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageXDistance), self.leftImageOrigin[1]+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageYDistance)))
			
			
			#image leaving screen
			leavingImageXDistance = self.farRightOrigin[0]-self.rightImageOrigin[0]
			leavingImage = pygame.transform.scale(self.icons[leaving],(self.subImageWidth, self.subImageHeight))
			self.screen.blit(leavingImage,(self.rightImageOrigin[0]+((self.changeFrameCounter/self.numberOfChangeFrames)*enteringImageXDistance), self.rightImageOrigin[1]))
			
			
		self.statusBar.update()
		pygame.display.flip()
		if self.changeFrameCounter < self.numberOfChangeFrames:
			self.changeFrameCounter += 1
		else:
			self.changeFrameCounter = 1
			self.isChanging = False
	
		
	def update(self):
		self.draw()

	def sportScreen(self, spo):
		pygame.draw.rect(self.screen, (0,0,0), (0,0, self.width, self.height), 0)
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
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mp.sendMessage("quit")
					sys.exit()
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					self.begin()
	
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
							if self.currentSelection < len(self.icons)-1:
								self.currentSelection += 1
							else:
								self.currentSelection = 0
						
					
					if event.key == K_LEFT:
						if not self.isChanging:
							self.whichDirection = self.LEFT
							self.isChanging = True
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
			
						self.MainBack = gui2.MainMenu()
						self.MainBack()
			###

			###other events
			
			###
			
			###loop logic
			
			if self.aTimeInc:
				self.animationTime +=1
			else:
				self.animationTime -=1
			if self.animationTime > 10 or self.animationTime < 1:
				self.aTimeInc = not self.aTimeInc
			
			if not self.isChanging:
				self.update()
			else:
				self.animateChange()
				
			if not self.running:
				break
			###
			
	def begin(self):
		self.running = True
		self.font = pygame.font.Font(None, 36)
		self.sportScores = Sports.Sports()
		self.sportsMainLoop()
