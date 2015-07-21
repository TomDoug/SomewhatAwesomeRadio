#!/usr/bin/python
import os
import sys, pygame
from pygame.locals import *
import scores #this lets us use things we made in scores.pi
import id3reader #accesses mp3 metadata
import UDPserver #allows android remote to work
#import serialServer
import songClass
import Sports
import clientInterface

pygame.init()


mp = clientInterface.MusicPlayer()

s = UDPserver.server()
s.daemon = True
s.start()

#ser = serialServer.Serial()
#ser.daemon = True
#ser.start()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 36)

class Mainmenu():
	def __init__(self):
		self.songs = mp.songList
	


	def updateMain(self):
	
		weather = pygame.image.load(os.path.join('imgs','weather.jpg'))
		screen.blit(weather,(0,0))

		music = pygame.image.load(os.path.join('imgs','music.jpg'))
		screen.blit(music,(300,0))

		sports = pygame.image.load(os.path.join('imgs','sports.jpg'))
		screen.blit(sports,(0,200))

		hmm = pygame.image.load(os.path.join('imgs','hmm.jpg'))
		#not sure what  to put in this last box
		screen.blit(hmm,(300,200))
		
		if self.currentSelection == 0:#weather
			pygame.draw.rect(screen, (150,20,215), Rect((0,0), (299, 199)), 5)
			pygame.display.flip()
		elif self.currentSelection == 1:#music
			pygame.draw.rect(screen, (150,20,215), Rect((300,0), (299, 199)), 5)
			pygame.display.flip()
		elif self.currentSelection == 2:#sports
			pygame.draw.rect(screen, (150,20,215), Rect((0,200), (299, 199)), 5)
			pygame.display.flip()
		elif self.currentSelection == 3:#derp
			pygame.draw.rect(screen, (150,20,215), Rect((300,200), (299, 199)), 5)
			pygame.display.flip()

	currentSelection = 0
	def mainMenu(self):
		self.updateMain()
				
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
					if self.currentSelection == 0:
						self.currentSelection = 1
					elif self.currentSelection == 2:
						self.currentSelection = 3
					self.updateMain()	
				if event.type == pygame.KEYDOWN and event.key == K_DOWN:
					if self.currentSelection == 0:
						self.currentSelection = 2

					elif self.currentSelection == 1:
						self.currentSelection = 3
					self.updateMain()
				if event.type == pygame.KEYDOWN and event.key == K_LEFT:
					if self.currentSelection == 1:
						self.currentSelection = 0

					elif self.currentSelection == 3:
						self.currentSelection = 2
					self.updateMain()

				if event.type == pygame.KEYDOWN and event.key == K_UP:
					if self.currentSelection == 2:
						self.currentSelection = 0

					elif self.currentSelection == 3:
						self.currentSelection = 1
					self.updateMain()
				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					if self.currentSelection == 0:
						self.startWeather()
					elif self.currentSelection == 1:
						self.MusicArtist()
					elif self.currentSelection == 2:
						self.startSports()
					elif self.currentSelection == 3:
						print 'derp'
						#derp
				if event.type == pygame.QUIT:
					mp.sendMessage("quit")
					sys.exit()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					mp.sendMessage("quit")
					sys.exit()


	def MusicArtist(self):
		self.currentlist = ""
		Artists = []

		for i in self.songs:
			if i.artist == "":
				i.artist = "Unknown"
			if not i.artist in Artists:
				Artists.append(i.artist)
		self.currentlist = "Artists"
		self.updateMusic(Artists)


	def MusicSongs(self,art):
		tunes = []	
		for thatone in self.songs:
			try:			
				if thatone.artist == "%s" % art:
					tunes.append(thatone.song)
			except:
				continue

		self.currentlist = "tunes"
		self.updateMusic(tunes)	


	def updateMusic(self, listofthings):
		pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)


		data = [listofthings[x:x+16] for x in xrange(0, len(listofthings), 16)]
		howmuch = len(data)

		#this creates transparent block
		a=0
		s = pygame.Surface((600,25), pygame.SRCALPHA)
		s.fill((255,255,255,128))
		screen.blit(s, (0,a))

		y=0
		z=0
		for item in data[z]:
		#	print "%s" % performer
			
			image = font.render("%s" % item, 1, (255,255,255))
			screen.blit(image, (0,y))
			y+=25
		pygame.display.flip()

		while True:
			for event in pygame.event.get():

				if event.type == pygame.KEYDOWN and event.key == K_UP:

					if a == 0:
						z-=1
						a=400
						if z<0:
							z=howmuch-1

					pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)	
		
					a-=25
					s.fill((255,255,255,128))
					screen.blit(s, (0,a))

					y=0
					for item in data[z]:
			
						image = font.render("%s" % item, 1, (255,255,255))
						screen.blit(image, (0,y))
						y+=25
					
					pygame.display.flip()

				if event.type == pygame.KEYDOWN and event.key == K_DOWN:
					if a == 375:
						a=-25
						if z==howmuch-1:
							z=0
						else:
							z+=1
					
					pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)
		
					a+=25
					s.fill((255,255,255,128))
					screen.blit(s, (0,a))

					y=0
					for item in data[z]:
			
						image = font.render("%s" % item, 1, (255,255,255))
						screen.blit(image, (0,y))
						y+=25
					
					pygame.display.flip()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					if self.currentlist == "Artists":
						self.MusicSongs(data[z][a/25])

					elif self.currentlist == "tunes":
						self.MusicP(data[z][a/25])
				

				if event.type == pygame.QUIT:
					mp.sendMessage("quit")
					sys.exit()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					mp.sendMessage("quit")
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					if self.currentlist == "Artists":
						self.mainMenu()

					elif self.currentlist == "tunes":
						self.MusicArtist()



	def MusicP(self,playsong):
		lalala = pygame.image.load(os.path.join('imgs','note.jpeg'))
		screen.blit(lalala,(0,0))
		pygame.display.flip()	
		
		for i in self.songs:
			if i.song == playsong:
				currentsong = i
				break
		
		mp.load(i.filePath)


		while True:
			for event in pygame.event.get():

				if event.type == pygame.KEYDOWN and event.key == K_SPACE:
					mp.play()

				if event.type == pygame.KEYDOWN and event.key == K_p:
					mp.sendMessage("quit")

				if event.type == pygame.QUIT:
					
					mp.sendMessage("quit")
					sys.exit()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					mp.sendMessage("quit")
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.MusicSongs(currentsong.artist)
	
	def updateSports(self):
		NHL = pygame.image.load(os.path.join('imgs','NHL.jpg'))
		screen.blit(NHL,(0,0))

		NFL = pygame.image.load(os.path.join('imgs','NFL.jpg'))
		screen.blit(NFL,(300,0))

		NBA = pygame.image.load(os.path.join('imgs','NBA.jpg'))
		screen.blit(NBA,(0,200))

		MLB = pygame.image.load(os.path.join('imgs','MLB.jpg'))
		screen.blit(MLB,(300,200))
		
		if self.sportsSel == 0:
			pygame.draw.rect(screen, (150,20,215), Rect((0,0), (299, 199)), 5)
			pygame.display.flip()
		elif self.sportsSel == 1:
			pygame.draw.rect(screen, (150,20,215), Rect((300,0), (299, 199)), 5)
			pygame.display.flip()
		elif self.sportsSel == 2:
			pygame.draw.rect(screen, (150,20,215), Rect((0,200), (299, 199)), 5)
			pygame.display.flip()
		elif self.sportsSel == 3:
			pygame.draw.rect(screen, (150,20,215), Rect((300,200), (299, 199)), 5)
			pygame.display.flip()
			
	sportsSel = 0
	def startSports(self):
		
		self.updateSports()
		while 1:
			for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
						if self.sportsSel == 0:
							self.sportsSel = 1
						elif self.sportsSel == 2:
							self.sportsSel = 3
						self.updateSports()	
					if event.type == pygame.KEYDOWN and event.key == K_DOWN:
						if self.sportsSel == 0:
							self.sportsSel = 2

						elif self.sportsSel == 1:
							self.sportsSel = 3
						self.updateSports()
					if event.type == pygame.KEYDOWN and event.key == K_LEFT:
						if self.sportsSel == 1:
							self.sportsSel = 0

						elif self.sportsSel == 3:
							self.sportsSel = 2
						self.updateSports()

					if event.type == pygame.KEYDOWN and event.key == K_UP:
						if self.sportsSel == 2:
							self.sportsSel = 0

						elif self.sportsSel == 3:
							self.sportsSel = 1
						self.updateSports()
					if event.type == pygame.KEYDOWN and event.key == K_RETURN:
						if self.sportsSel == 0:
							self.sportScreen('nhl')
						elif self.sportsSel == 1:
							self.sportScreen('nfl')
						elif self.sportsSel == 2:
							self.sportScreen('nba')
						elif self.sportsSel == 3:
							self.sportScreen('mlb')
					if event.type == KEYDOWN and event.key == K_BACKSPACE:
						self.mainMenu()
					if event.type == pygame.QUIT:
						mp.sendMessage("quit")
						sys.exit()
					elif event.type == KEYDOWN and event.key == K_ESCAPE:
						mp.sendMessage("quit")	
						sys.exit()

	def sportScreen(self, spo):
		pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)
		scoreImg = []
		sco = []
		if spo == 'nhl':
			sco = sportScores.getNHLScores()
		elif spo == 'nfl':
			sco = sportScores.getNFLScores()
		elif spo == 'nba':
			sco = sportScores.getNBAScores()
		elif spo == 'mlb':
			sco = sportScores.getMLBScores()
			
		for i in sco:
			scoreImg.append(font.render(str(i),1,(255,255,255)))
			print i
		x = 10
		y = 10
		for i in scoreImg:
			screen.blit(i,(x,y))
			y += 20
		pygame.display.flip()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mp.sendMessage("quit")
					sys.exit()
				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					self.startSports()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					mp.sendMessage("quit")
					sys.exit()
	def startWeather(self):
		#weather stuff will go here
		print 'weather'

sportScores = Sports.Sports() #this creates a new sports object and calls the __in
startmenu = Mainmenu()	
startmenu.mainMenu()
