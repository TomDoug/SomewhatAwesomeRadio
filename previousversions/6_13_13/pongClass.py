import sys, os
import random
import pygame
import pickle
import operator
from pygame.locals import *
import gui

pygame.init()
size = width, height = 600, 400
font = pygame.font.Font(None, 36)
fancyfont = pygame.font.SysFont("Broadway", 25)

class MainMenu():
	def __init__(self,screen):
		print 'pong'

		self.screen = screen
		pygame.draw.rect(screen, (0,0,0), (0,0, int(width), int(height)), 0)
		
		pygame.display.flip()

		self.currentSelection = 0
		self.animationTime = 0
		self.aTimeInc = True
		self.clock = pygame.time.Clock()
		self.mainOn = True
		guiBack = gui.Mainmenu()


		self.icons = [pygame.image.load(os.path.join('imgs','playgame.jpg')), pygame.image.load(os.path.join('imgs','stats.jpg'))]
		self.players = []
		
		self.loadList()

	#	self.sortPlayers()
		self.mainScreen()
		self.mainLoop()
	#	self.addPlayer()
	#	self.statsScreen()

	def mainScreen(self):
		backg = pygame.image.load(os.path.join('imgs', 'swagmaster.jpg'))
		backg2 = pygame.transform.scale(backg, (width, height))
		self.screen.blit(backg2, (0,0))


		self.master = self.players[0]

		swagm = pygame.image.load(os.path.join('imgs', self.master.level, self.master.pic))
		swagm2 = pygame.transform.scale(swagm, (int((width/3.0)*(8.0/10.0)),int(height/5.0))) 
	#	self.screen.blit(swagm2,((width/3)+(width/30), (height/4)+(height/5)+(height/5)))

		
		swagname = fancyfont.render(self.master.name, 1, (0,0,0))
		self.screen.blit(swagname, (((width/3)+(width/9), ((height/4)+(height/5)+(height/20)))))


	def mainScreenani(self):
		if self.currentSelection == 1:
		
			self.screen.blit(self.getAnimatedFrame(),((width-(width/3)),0))
			playimg = pygame.image.load(os.path.join('imgs','playgame.jpg'))
			playimg2 = pygame.transform.scale(playimg,((width/3), height))
			self.screen.blit(playimg2, (0,0))


		if self.currentSelection == 0:
			self.screen.blit(self.getAnimatedFrame(),((0,0)))
			statimg = pygame.image.load(os.path.join('imgs','stats.jpg'))
			statimg2 = pygame.transform.scale(statimg,((width/3), height))
			self.screen.blit(statimg2, ((width-(width/3)),0))
		
		

		pygame.display.flip()


	def getAnimatedFrame(self):

		img = self.icons[self.currentSelection]
		sur = pygame.Surface((int(width/3), int(height)))
		sur.set_colorkey((255,1,255))
		pygame.draw.rect(sur,(255,1,255),(0,0,(width/3),height),0)
		sur.blit(pygame.transform.scale(img,((width/3)-self.animationTime, height-self.animationTime)),(self.animationTime/2,self.animationTime/2))
		return sur



	def statsScreen(self):
		self.sortPlayers()

		bg = pygame.image.load(os.path.join('imgs','statsbackground.jpg'))
		bg2 = pygame.transform.scale(bg, (width, height))
		self.screen.blit(bg2, (0,0))
		
		pygame.draw.line(self.screen, (0,0,0), (0,35),(600,35), 1)
		
		names = font.render("Player", 1, (0,0,0))
		self.screen.blit(names, ((width/7),0))

		wins = font.render("W", 1, (0,0,0))
		nextwidth = width/3
		self.screen.blit(wins, (nextwidth, 0))

		losses = font.render("L", 1, (0,0,0))
		self.screen.blit(losses, (nextwidth + (width/7), 0))

		uTable = font.render("UT", 1, (0,0,0))
		self.screen.blit(uTable, (nextwidth + (2*(width/7)), 0))

		nMile = font.render("NM", 1, (0,0,0))
		self.screen.blit(nMile, (nextwidth + (3*(width/7)), 0))
		
		x=1
		for i in self.finalSort:

			pic = pygame.image.load(os.path.join('imgs', i.level, i.pic))
			pic2 = pygame.transform.scale(pic, ((width/7),36))
			self.screen.blit(pic2,(0, (x*(height/10))))

			name = font.render(i.name, 1, (0,0,0))
			self.screen.blit(name, ((width/7, (x*(height/10)))))

			win = font.render(str(i.wins), 1, (0,0,0))
			self.screen.blit(win, ((nextwidth, (x*(height/10)))))

			lose = font.render(str(i.losses), 1, (0,0,0))
			self.screen.blit(lose, ((nextwidth + (1*width/7), (x*(height/10)))))
			
			UT = font.render(str(i.UT), 1, (0,0,0))
			self.screen.blit(UT, ((nextwidth + (2*(width/7)), (x*(height/10)))))

			NM = font.render(str(i.NM), 1, (0,0,0))
			self.screen.blit(NM, ((nextwidth + (3*(width/7)), (x*(height/10)))))

			x+=1


		pygame.display.flip()

	def sortPlayers(self):
		self.sortThis = {}
		for i in self.players:
			self.sortThis[i.name]=i.wins
		self.sortedPlayers = sorted(self.sortThis.iteritems(), key=operator.itemgetter(1))
	#	print self.sortedPlayers
		
		self.sortedNames = []

		for i in self.sortedPlayers[::-1]:
			name = i[0]
			self.sortedNames.append(name)

		
		self.finalSort = []
		for i in self.sortedNames:
			for j in self.players:
				if i == j.name:
					self.finalSort.append(j)
					break


	#	self.printStats()
	#	print self.sortThis



	def addPlayer(self):
		prompt = font.render("What is your name?", 1, (255, 255, 255))
		self.screen.blit(prompt, (0,0))

		pygame.display.flip()

		newName = raw_input("name: ")
		pygame.draw.rect(self.screen, (0,0,0), (0,0, width, height), 0)
		prompt2 = font.render("Your name is %s" % newName, 1, (255,255,255))
		self.screen.blit(prompt2, (0,0))

		pygame.display.flip()
		
		#adds to list#
		newPlayer = playerStats()
		newPlayer.name = newName
		self.players.append(newPlayer)

		self.updateList()
		self.loadList()
		self.printStats()

	def updateList(self):
		pickle.dump(self.players, open("pongStats.txt", "wb+"))

	def loadList(self):
		self.players = pickle.load(open("pongStats.txt", "rb"))

	def printStats(self):
		print "Name \tWins\tLosses"
		for i in self.players:
			print i.name + "\t" + str(i.wins) + "\t" + str(i.losses)
	def mainLoop(self):
		guiBack = gui.Mainmenu()
		while 1:
			self.clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
					if self.currentSelection == 1:
						self.currentSelection = 0
					else:
						self.currentSelection = 1

				if event.type == pygame.KEYDOWN and event.key == K_LEFT:
					if self.currentSelection == 1:
						self.currentSelection = 0
					else:
						self.currentSelection = 1

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					if self.currentSelection == 1:
						self.statsScreen()
						self.mainOn = False
					if self.currentSelection == 0:
						print 'play game'

				if event.type == pygame.KEYDOWN and event.key == K_BACKSPACE:
					if self.mainOn == True:
						guiBack.mainMenu()
					if self.mainOn == False:
						self.mainScreen()
						self.mainOn = True

			if self.aTimeInc:
				self.animationTime +=1
			else:
				self.animationTime -=1
			if self.animationTime >10 or self.animationTime <1:
				self.aTimeInc = not self.aTimeInc

			if self.mainOn == True:
				self.mainScreenani()

class playerStats():
	def __init__(self):
		
		randpic = "%d.jpg" % (random.randint(0,5))

		self.wins = 0
		self.losses = 0
		self.name = ""
		self.UT = 0
		self.NM = 0
		self.pic = randpic
		self.level = "baby"
