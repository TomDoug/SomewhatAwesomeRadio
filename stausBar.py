import pygame, sys, os
from datetime import datetime
from pygame.locals import *

pygame.init()
font = pygame.font.Font(None, 36)
class StatusBar:
	def __init__(self, scr):
		self.screen = scr
		self.notifications = []
		self.subScreen = pygame.Surface((scr.get_width(), int(scr.get_height()/10)))
		self.subWidth, self.subHeight = (scr.get_width(), scr.get_height()/10)
		self.hasTime = True
		self.background = pygame.image.load(os.path.join('imgs', 'stat.png'))
		self.background = pygame.transform.scale(self.background,(self.subWidth, self.subHeight))
	
	def addNotification(self, notif):
		notif.number = len(self.notifications)
		self.notifications.append(notif)
	def removeNotification(self, notif):
		print "______" 
		print notif
		try:
			self.notifications.remove(notif)
		except:
			print "Error, Notification not in status bar"
		
		#for i in range(0, len(self.notifications)):
		#	print i
		#	if self.notifications[i].number == notifNum:
		#		print i
		#		print len(self.notifications)
		#		self.notifications.remove(self.notifications[i])
		#		break
	def drawNotifications(self):
		curY=0
		for i in range(0, len(self.notifications)):
			self.subScreen.blit(pygame.transform.scale(self.notifications[i].getIcon(),(self.notifications[i].width,40) ),(curY, 0) )
			curY +=self.notifications[i].width
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
		
		self.drawNotifications()
		self.screen.blit(self.subScreen, (0,0))
		
	
	#TODO: Make a lower status bar that keeps track of the current song position
