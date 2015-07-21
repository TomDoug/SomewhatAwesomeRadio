import pygame, sys, os
from datetime import datetime
from pygame.locals import *

pygame.init()
font = pygame.font.Font(None, 36)
class StatusBar:
	def __init__(self, scr):
		self.screen = scr
		self.subScreen = pygame.Surface((scr.get_width(), int(scr.get_height()/10)))
		self.subWidth, self.subHeight = (scr.get_width(), scr.get_height()/10)
		self.hasTime = True
		self.background = pygame.image.load(os.path.join('imgs', 'stat.png'))
		self.background = pygame.transform.scale(self.background,(self.subWidth, self.subHeight))
	
	def update(self):
		pygame.draw.rect(self.subScreen,(255,255,255),(0,0,self.subWidth,self.subHeight),0)
		self.subScreen.blit(self.background,(0,0))
		if self.hasTime:
			nowTime = datetime.now()
			if nowTime.hour >= 12:
				nowHour = nowTime.hour - 12
			else:
				nowHour = nowTime.hour
			timeStr = str(nowHour) + ":" + str(nowTime.minute) + ":" + str(nowTime.second)
			time = font.render(str(timeStr), 1, (10,234,255))
			self.subScreen.blit(time, (self.subWidth-(self.subWidth/4), (self.subHeight/3)))
		self.screen.blit(self.subScreen, (0,0))
		
	
	
