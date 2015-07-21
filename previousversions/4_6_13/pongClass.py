import sys, os
import pygame
import pickle

pygame.init()
size = width, height = 600, 400
font = pygame.font.Font(None, 36)

class MainMenu():
	def __init__(self,screen):
		print 'pong'

		self.screen = screen
		pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)
		
		pygame.display.flip()

		self.players = []
		
		self.loadList()

		self.mainScreen()
	#	self.addPlayer()
	#	self.statsScreen()

	def mainScreen(self):
		playgame = pygame.image.load(os.path.join('imgs','playgame.jpg'))
		playgame2 = pygame.transform.scale(playgame, ((width/3), height))
		self.screen.blit(playgame2,(0,0))

		stats = pygame.image.load(os.path.join('imgs','stats.jpg'))
		stats2 = pygame.transform.scale(stats, ((width/3), height))
		self.screen.blit(stats2,((width-(width/3)),0))

		pygame.display.flip()



	def statsScreen(self):
		pygame.draw.rect(self.screen, (255,255,255), (0,0, width, height), 0)
		pygame.draw.line(self.screen, (0,0,0), (0,35),(600,35), 1)
		
		names = font.render("Player", 1, (0,0,0))
		self.screen.blit(names, (0,0))

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
		for i in self.players:
			name = font.render(i.name, 1, (0,0,0))
			self.screen.blit(name, (0, (x*(height/10))))

			win = font.render(str(i.wins), 1, (0,0,0))
			self.screen.blit(win, (nextwidth, (x*(height/10))))

			lose = font.render(str(i.losses), 1, (0,0,0))
			self.screen.blit(lose, ((nextwidth + (width/7), (x*(height/10)))))
			
			UT = font.render(str(i.UT), 1, (0,0,0))
			self.screen.blit(UT, ((nextwidth + (2*(width/7)), (x*(height/10)))))

			NM = font.render(str(i.NM), 1, (0,0,0))
			self.screen.blit(NM, ((nextwidth + (3*(width/7)), (x*(height/10)))))



			x+=1


		pygame.display.flip()




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



class playerStats():
	def __init__(self):
		self.wins = 0
		self.losses = 0
		self.name = ""
		self.UT = 0
		self.NM = 0

