import pygame, sys, os, UDPserver
import SportsMain, WeatherMain, MusicMain, PongMain, MessagesMain
from stausBar import *
from pygame.locals import *

size = width, height = 600, 400
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
font = pygame.font.Font(None, 36)	

class MainMenu:

	def __init__(self):

		self.statusBar = StatusBar(screen)
		self.LEFT = 0
		self.RIGHT = 1
		self.whichDirection = 0
		self.currentSelection = 1
		self.animationTime = 0
		self.aTimeInc = True
		self.clock = pygame.time.Clock()
		self.loadIcons()
		self.imageWidth = width/2
		self.mainHeightOrigin = height/10
		self.mainHeight = height - (height/10)
		self.imageHeight = int(self.mainHeight*(.75))
		self.mainImageOrigin = ((width/2)-(self.imageWidth/2), ((self.mainHeight/2)-(self.imageHeight/2))+self.mainHeightOrigin)
		
		
		
		self.padding = 0
		self.subImageWidth = int(self.imageWidth*.8)
		self.subImageHeight = int(self.imageHeight*.8)
		self.leftImageOrigin = (((-self.subImageWidth/2)-self.padding), ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		self.rightImageOrigin = ((width-(self.subImageWidth/2)+self.padding), ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		
		self.farRightOrigin = ((width+(self.subImageWidth/2)+self.padding), ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		self.farLeftOrigin = (((-self.subImageWidth/2)-self.padding)-self.subImageWidth, ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		self.background = pygame.image.load(os.path.join('imgs', 'mainbackground.jpg'))
		self.background = pygame.transform.scale(self.background, (width, self.mainHeight))
		
		self.isChanging = False
		self.changeFrameCounter = 1.0
		self.numberOfChangeFrames = 15.0
		self.changeCounterIncreasing = True
		
		self.sportsMain = SportsMain.SportsPage(screen, self.clock, self.statusBar)
		
		
		self.mainLoop()
		
	def loadIcons(self):
		self.icons = [self.loadImage('weather.jpg'), self.loadImage('music.jpg'), self.loadImage('sports.jpg'), self.loadImage('pong.jpg'), self.loadImage('messages.png')]
		self.otherScreens = [WeatherMain.WeatherPage(screen, self.clock, self.statusBar), MusicMain.MusicPage(screen, self.clock, self.statusBar), SportsMain.SportsPage(screen, self.clock, self.statusBar), PongMain.PongPage(screen, self.clock, self.statusBar), MessagesMain.MessagesPage(screen, self.clock, self.statusBar)]
		
	def loadImage(self, path):
		#print os.path.join('imgs',path)
		return pygame.image.load(os.path.join('imgs',path))
		
	def paint(self):
		#pygame.draw.rect(screen, (0,0,0),(0,0,width,10),0)
		
		screen.blit(self.background,(0,self.mainHeightOrigin))
		
		
		if self.currentSelection > 0:
			left = self.currentSelection-1
		else:
			left = len(self.icons) - 1
		
		if self.currentSelection < len(self.icons)-1:
			right = self.currentSelection+1
		else:
			right = 0

		screen.blit(pygame.transform.scale(self.icons[left],(self.subImageWidth,self.subImageHeight)),self.leftImageOrigin)
		screen.blit(pygame.transform.scale(self.icons[right],(self.subImageWidth,self.subImageHeight)),self.rightImageOrigin)
		
		screen.blit(self.getAnimatedFrame(),self.mainImageOrigin)
		self.statusBar.update()
		pygame.display.flip()
		
	def getAnimatedFrame(self):
		img = self.icons[self.currentSelection]
		sur = pygame.Surface((self.imageWidth, self.imageHeight))
		sur.set_colorkey((255,1,255))
		pygame.draw.rect(sur,(255,1,255),(0,0,width,height),0)
		sur.blit(pygame.transform.scale(img,(self.imageWidth-self.animationTime, self.imageHeight-self.animationTime)),(self.animationTime/2,self.animationTime/2))
		return sur
	
	def update(self):
		self.paint()
		
	def animateChange(self):
		
		new = self.currentSelection
		screen.blit(self.background,(0,self.mainHeightOrigin))

		pygame.draw.rect(screen,(255,1,255),(0,0,width,height/10),0)
		
		if self.whichDirection == self.RIGHT:
			old = new - 1
			leaving = old - 1
			entering = new + 1
			if entering > len(self.icons)-1:
				entering = entering - (len(self.icons))
			
			
			
			
			#image leaving screen
			leavingImageXDistance = self.leftImageOrigin[0] - self.farLeftOrigin[0]
			leavingImage = pygame.transform.scale(self.icons[leaving],(self.subImageWidth, self.subImageHeight))
			screen.blit(leavingImage,(self.leftImageOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*leavingImageXDistance), self.leftImageOrigin[1]))
			
			#old image
			oldImageXDistance = self.mainImageOrigin[0]-self.leftImageOrigin[0]
			oldImageYDistance = self.mainImageOrigin[1]-self.leftImageOrigin[1]
			oldImageTransformDistanceHeight = self.imageHeight - self.subImageHeight
			oldImageTransformDistanceWidth  = self.imageWidth - self.subImageWidth
			
			oldImage = pygame.transform.scale(self.icons[old],(int(self.imageWidth-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageTransformDistanceWidth)),int(self.imageHeight-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageTransformDistanceHeight))))
			screen.blit(oldImage,(self.mainImageOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageXDistance), self.mainImageOrigin[1]-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageYDistance)))
			
			#new image
			newImageXDistance = self.rightImageOrigin[0]-self.mainImageOrigin[0]
			newImageYDistance = self.mainImageOrigin[1]-self.rightImageOrigin[1]
			newImageTransformDistanceHeight = self.imageHeight - self.subImageHeight
			newImageTransformDistanceWidth  = self.imageWidth - self.subImageWidth
			
			newImage = pygame.transform.scale(self.icons[new],(int(self.subImageWidth + ((self.changeFrameCounter/self.numberOfChangeFrames)*newImageTransformDistanceWidth)),int(self.subImageHeight+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageTransformDistanceHeight))))
			screen.blit(newImage,(self.rightImageOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*newImageXDistance), self.rightImageOrigin[1]+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageYDistance)))
			
			#image entering screen
			enteringImageXDistance = self.farRightOrigin[0]-self.rightImageOrigin[0]
			enteringImage = pygame.transform.scale(self.icons[entering],(self.subImageWidth, self.subImageHeight))
			screen.blit(enteringImage,(self.farRightOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*enteringImageXDistance), self.leftImageOrigin[1]))
			
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
			screen.blit(enteringImage,(self.farLeftOrigin[0]+((self.changeFrameCounter/self.numberOfChangeFrames)*enteringImageXDistance), self.leftImageOrigin[1]))
			

			#old image
			oldImageXDistance = self.mainImageOrigin[0]-self.rightImageOrigin[0]
			oldImageYDistance = self.mainImageOrigin[1]-self.rightImageOrigin[1]
			oldImageTransformDistanceHeight = self.imageHeight - self.subImageHeight
			oldImageTransformDistanceWidth  = self.imageWidth - self.subImageWidth
			
			oldImage = pygame.transform.scale(self.icons[old],(int(self.imageWidth-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageTransformDistanceWidth)),int(self.imageHeight-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageTransformDistanceHeight))))
			screen.blit(oldImage,(self.mainImageOrigin[0]-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageXDistance), self.mainImageOrigin[1]-((self.changeFrameCounter/self.numberOfChangeFrames)*oldImageYDistance)))
			
			
			#new image
			newImageXDistance = self.mainImageOrigin[0]-self.leftImageOrigin[0]
			newImageYDistance = self.mainImageOrigin[1]-self.leftImageOrigin[1]
			newImageTransformDistanceHeight = self.imageHeight - self.subImageHeight
			newImageTransformDistanceWidth  = self.imageWidth - self.subImageWidth
			
			newImage = pygame.transform.scale(self.icons[new],(int(self.subImageWidth + ((self.changeFrameCounter/self.numberOfChangeFrames)*newImageTransformDistanceWidth)),int(self.subImageHeight+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageTransformDistanceHeight))))
			screen.blit(newImage,(self.leftImageOrigin[0]+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageXDistance), self.leftImageOrigin[1]+((self.changeFrameCounter/self.numberOfChangeFrames)*newImageYDistance)))
			
			
			#image leaving screen
			leavingImageXDistance = self.farRightOrigin[0]-self.rightImageOrigin[0]
			leavingImage = pygame.transform.scale(self.icons[leaving],(self.subImageWidth, self.subImageHeight))
			screen.blit(leavingImage,(self.rightImageOrigin[0]+((self.changeFrameCounter/self.numberOfChangeFrames)*enteringImageXDistance), self.rightImageOrigin[1]))
			
			
		self.statusBar.update()
		pygame.display.flip()
		if self.changeFrameCounter < self.numberOfChangeFrames:
			self.changeFrameCounter += 1
		else:
			self.changeFrameCounter = 1
			self.isChanging = False
		
	def processSelection(self):
		self.otherScreens[self.currentSelection].begin()
		#if self.currentSelection == 2:
		#	self.sportsMain.begin()
		
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
						
					if event.key == K_ESCAPE:
						sys.exit()
					if event.key == K_RETURN:
						self.processSelection()
			
			
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
				
			
if __name__ == "__main__":
	pygame.init()
	s = UDPserver.server()
	s.daemon = True
	s.start()
	
	size = width, height = 600, 400
	screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
	font = pygame.font.Font(None, 36)
	main = MainMenu()
