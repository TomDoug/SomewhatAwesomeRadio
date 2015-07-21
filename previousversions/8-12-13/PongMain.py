import pygame, sys, os
from pygame.locals import *
import sys, os
import random
import pickle
import operator
import gui2


class PongPage:

	def __init__(self, screen, clock, statusBar):
		print "pong page initialized"
		self.statusBar = statusBar
		self.running = False
		self.screen = screen

		
		self.clock = clock
		self.mainScreenOrigin = ((0,screen.get_height()/10))
		self.mainScreenSize = ((screen.get_width(), screen.get_height() - (screen.get_height()/10)))
		
		self.background = pygame.image.load(os.path.join('imgs', 'mainbackground.jpg'))
		self.background = pygame.transform.scale(self.background, (self.mainScreenSize))

		
	

	def update(self):
		self.draw()
		
	def draw(self):
		self.screen.blit(self.background, (self.mainScreenOrigin))
	

		if self.mainOn:
			self.mainScreen()
			self.statusBar.update()
		if not self.mainOn:
			self.statsScreen()
		
		pygame.display.flip()


	def mainScreen(self):
		backg = pygame.image.load(os.path.join('imgs', 'statsbackground.jpg'))
		backg2 = pygame.transform.scale(backg, (self.mainScreenSize))
		self.screen.blit(backg2, (self.mainScreenOrigin))

		

		self.master = self.finalSort[0]

		swagm = pygame.image.load(os.path.join('imgs', self.master.level, self.master.pic))
		swagm2 = pygame.transform.scale(swagm, (int((self.width/3.0)*(8.0/10.0)),int(self.height/5.0))) 
	#	self.screen.blit(swagm2,((width/3)+(width/30), (height/4)+(height/5)+(height/5)))

	
		text = self.fancyfont.render("Current Swagmaster", 1, (0,0,0))
		self.screen.blit(text, (((self.width/3), ((self.height/4)+(self.height/5)))))

		swagname = self.fancyfont.render(self.master.name, 1, (0,0,0))
		self.screen.blit(swagname, (((self.width/3)+(self.width/9), ((self.height/4)+(self.height/5)+(self.height/20)))))


	def addPlayer(self):
		prompt = self.font.render("What is your name?", 1, (255, 255, 255))
		self.screen.blit(prompt, (0,0))

		pygame.display.flip()

		newName = raw_input("name: ")
		pygame.draw.rect(self.screen, (0,0,0), (0,0, self.width, self.height), 0)
		prompt2 = self.font.render("Your name is %s" % newName, 1, (255,255,255))
		self.screen.blit(prompt2, (0,0))

		pygame.display.flip()
		
		#adds to list#
		newPlayer = playerStats()
		newPlayer.name = newName
		self.players.append(newPlayer)

		self.updateList()
		self.loadList()
		self.printStats()

	def statsScreen(self):
		self.sortPlayers()

		bg = pygame.image.load(os.path.join('imgs','statsbackground.jpg'))
		bg2 = pygame.transform.scale(bg, (self.width, self.height))
		self.screen.blit(bg2, (0,0))
		
		pygame.draw.line(self.screen, (0,0,0), (0,35),(600,35), 1)
		
		names = self.font.render("Player", 1, (0,0,0))
		self.screen.blit(names, ((self.width/7),0))

		wins = self.font.render("W", 1, (0,0,0))
		nextwidth = self.width/3
		self.screen.blit(wins, (nextwidth, 0))

		losses = self.font.render("L", 1, (0,0,0))
		self.screen.blit(losses, (nextwidth + (self.width/7), 0))

		uTable = self.font.render("UT", 1, (0,0,0))
		self.screen.blit(uTable, (nextwidth + (2*(self.width/7)), 0))

		nMile = self.font.render("NM", 1, (0,0,0))
		self.screen.blit(nMile, (nextwidth + (3*(self.width/7)), 0))
		
		x=1
		for i in self.finalSort:

			pic = pygame.image.load(os.path.join('imgs', i.level, i.pic))
			pic2 = pygame.transform.scale(pic, ((self.width/7),36))
			self.screen.blit(pic2,(0, (x*(self.height/10))))

			name = self.font.render(i.name, 1, (0,0,0))
			self.screen.blit(name, ((self.width/7, (x*(self.height/10)))))

			win = self.font.render(str(i.wins), 1, (0,0,0))
			self.screen.blit(win, ((nextwidth, (x*(self.height/10)))))

			lose = self.font.render(str(i.losses), 1, (0,0,0))
			self.screen.blit(lose, ((nextwidth + (1*self.width/7), (x*(self.height/10)))))
			
			UT = self.font.render(str(i.UT), 1, (0,0,0))
			self.screen.blit(UT, ((nextwidth + (2*(self.width/7)), (x*(self.height/10)))))

			NM = self.font.render(str(i.NM), 1, (0,0,0))
			self.screen.blit(NM, ((nextwidth + (3*(self.width/7)), (x*(self.height/10)))))

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


	def updateList(self):
		pickle.dump(self.players, open("pongStats.txt", "wb+"))

	def loadList(self):
		self.players = pickle.load(open("pongStats.txt", "rb"))
		
	def printStats(self):
		print "Name \tWins \tLosses"
		for i in self.players:
			print i.name + "\t" + str(i.wins) + "\t" + str(i.losses)	
	
	def pongMainLoop(self):
		while 1:
			for event in pygame.event.get():
			
			###keydown events
				if event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						sys.exit()
					if event.key == K_BACKSPACE:
						if self.mainOn:
							self.running = False
						if not self.mainOn:
							self.mainOn = True
					if event.key == K_RETURN:
						self.statsScreen()
						self.mainOn = False
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

		self.width = 600
		self.height = 400

		self.font=pygame.font.Font(None, 36)
		self.fancyfont = pygame.font.SysFont("Broadway", 25)

		self.mainOn = True
		self.icons = [pygame.image.load(os.path.join('imgs','playgame.jpg')), pygame.image.load(os.path.join('imgs','stats.jpg'))]
		self.players = []


		self.loadList()
	#	self.addPlayer()
		self.updateList()
		self.sortPlayers()
		
	#	self.loadList()

		self.pongMainLoop()


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
