#!/usr/bin/python

import os
import sys, pygame
from pygame.locals import *
import scores #this lets us use things we made in scores.pi
import id3reader #accesses mp3 metadata
#import UDPserver
import songClass



pygame.init()
pygame.mixer.init()

#s = UDPserver.server()
#s.start()

size = width, height = 600, 400

screen = pygame.display.set_mode(size)

font = pygame.font.Font(None, 36)
class Mainmenu():
	def Chooseweather(self):
		weather = pygame.image.load(os.path.join('imgs','weather.jpg'))
		screen.blit(weather,(0,0))

		music = pygame.image.load(os.path.join('imgs','music.jpg'))
		screen.blit(music,(300,0))

		sports = pygame.image.load(os.path.join('imgs','sports.jpg'))
		screen.blit(sports,(0,200))

		hmm = pygame.image.load(os.path.join('imgs','hmm.jpg'))
		#not sure what  to put in this last box
		screen.blit(hmm,(300,200))
	
		pygame.draw.rect(screen, (150,20,215), Rect((0,0), (299, 199)), 5)
		pygame.display.flip()
		

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
					return self.Choosemusic()

				if event.type == pygame.KEYDOWN and event.key == K_DOWN:
					return self.Choosesports()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					print "weather"
						
				if event.type == pygame.QUIT:
					sys.exit()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()


	def Choosemusic(self):
		weather = pygame.image.load(os.path.join('imgs','weather.jpg'))
		screen.blit(weather,(0,0))

		music = pygame.image.load(os.path.join('imgs','music.jpg'))
		screen.blit(music,(300,0))

		sports = pygame.image.load(os.path.join('imgs','sports.jpg'))
		screen.blit(sports,(0,200))

		hmm = pygame.image.load(os.path.join('imgs','hmm.jpg'))
		#not sure what  to put in this last box
		screen.blit(hmm,(300,200))
	
		pygame.draw.rect(screen, (150,20,215), Rect((300,0), (299, 199)), 5)
		pygame.display.flip()
		

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_LEFT:
					return self.Chooseweather()

				if event.type == pygame.KEYDOWN and event.key == K_DOWN:
					return self.Choosederp()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					return self.MusicArtist()	

				if event.type == pygame.QUIT:
					sys.exit()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()


	def Choosesports(self):
		weather = pygame.image.load(os.path.join('imgs','weather.jpg'))
		screen.blit(weather,(0,0))

		music = pygame.image.load(os.path.join('imgs','music.jpg'))
		screen.blit(music,(300,0))

		sports = pygame.image.load(os.path.join('imgs','sports.jpg'))
		screen.blit(sports,(0,200))

		hmm = pygame.image.load(os.path.join('imgs','hmm.jpg'))
		#not sure what  to put in this last box
		screen.blit(hmm,(300,200))
	
		pygame.draw.rect(screen, (150,20,215), Rect((0,200), (299, 199)), 5)
		pygame.display.flip()
		

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
					return self.Choosederp()

				if event.type == pygame.KEYDOWN and event.key == K_UP:
					return self.Chooseweather()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					return self.ChooseNHL()	

				if event.type == pygame.QUIT:
					sys.exit()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()


	def Choosederp(self):
		weather = pygame.image.load(os.path.join('imgs','weather.jpg'))
		screen.blit(weather,(0,0))

		music = pygame.image.load(os.path.join('imgs','music.jpg'))
		screen.blit(music,(300,0))

		sports = pygame.image.load(os.path.join('imgs','sports.jpg'))
		screen.blit(sports,(0,200))

		hmm = pygame.image.load(os.path.join('imgs','hmm.jpg'))
		#not sure what  to put in this last box
		screen.blit(hmm,(300,200))
	
		pygame.draw.rect(screen, (150,20,215), Rect((300,200), (299, 199)), 5)
		pygame.display.flip()
		

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_LEFT:
					return self.Choosesports()

				if event.type == pygame.KEYDOWN and event.key == K_UP:
					return self.Choosemusic()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					print "derp"	

				if event.type == pygame.QUIT:
					sys.exit()
				


	def MusicArtist(self):
		pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)

		songs = []

		for (dirpath, dirname, filenames) in os.walk('C:\\Users\\Matt\\Music\\Music'): 
			for i in filenames:
				#makes sure the file is a .mp3
				if i.find('.mp3') != -1:
					path = dirpath + "\\" + i
					#makes a new instance of the song class for each song
					songs.append(songClass.song(path))

		Artists = []

		for i in songs:
			if i.artist == "":
				i.artist = "Unknown"
			if not i.artist in Artists:
				Artists.append(i.artist)


	#	Artists = os.listdir("C:\Users\Matt\Music\Music")
		data = [Artists[x:x+16] for x in xrange(0, len(Artists), 16)]
		howmuch = len(data)

		#this creates transparent block
		a=0
		s = pygame.Surface((600,25), pygame.SRCALPHA)
		s.fill((255,255,255,128))
		screen.blit(s, (0,a))

		y=0
		z=0
		for performer in data[z]:
		#	print "%s" % performer
			
			image = font.render("%s" % performer, 1, (255,255,255))
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
					for performer in data[z]:
			
						image = font.render("%s" % performer, 1, (255,255,255))
						screen.blit(image, (0,y))
						y+=25
					
					pygame.display.flip()
					print z

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
					for performer in data[z]:
			
						image = font.render("%s" % performer, 1, (255,255,255))
						screen.blit(image, (0,y))
						y+=25
					
					pygame.display.flip()
					print z

			#	if event.type == pygame.KEYDOWN and event.key == K_RETURN:
				

				if event.type == pygame.QUIT:
					sys.exit()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					pygame.mixer.music.stop()
					return self.Choosemusic()


	def MusicP(self):
	
		lalala = pygame.image.load(os.path.join('imgs','note.jpeg'))
		screen.blit(lalala,(0,0))
		pygame.display.flip()	

		songs = os.listdir("C:\Users\Matt\Documents\TEST\gui\musicfolder")#liste all items in given directory

	
		
		i = 0 
	#	pygame.mixer.music.load(songs[i])#loads song for play
	#	pygame.mixer.music.play()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
						i +=1
						value = songs[i % (len(songs))]
					#	print value

						pygame.mixer.music.load(value)
						pygame.mixer.music.play()
						
						id3r = id3reader.Reader(value)
						ArtistD = id3r.getValue ('performer')
						AlbumD = id3r.getValue ('album')
						
						screen.blit(lalala,(0,0))

						image = font.render("%s" % value, 1, (255,255,255))
						Artist = font.render("Artist: %s" % ArtistD, 1, (255,255,255))
						Album = font.render("Album: %s" % AlbumD, 1, (255,255,255))

						screen.blit(image, (0,0))
						screen.blit(Artist, (0,25))
						screen.blit(Album, (0,50))
						pygame.display.flip()
								

				if event.type == pygame.KEYDOWN and event.key == K_LEFT:
						i -=1
						value = songs[i % (len(songs))]
						print value

						pygame.mixer.music.load(value)
						pygame.mixer.music.play()
						
						id3r = id3reader.Reader(value)
						ArtistD = id3r.getValue ('performer')
						AlbumD = id3r.getValue ('album')
						
						screen.blit(lalala,(0,0))

						image = font.render("%s" % value, 1, (255,255,255))
						Artist = font.render("Artist: %s" % ArtistD, 1, (255,255,255))
						Album = font.render("Album: %s" % AlbumD, 1, (255,255,255))

						screen.blit(image, (0,0))
						screen.blit(Artist, (0,25))
						screen.blit(Album, (0,50))
						pygame.display.flip()

				if event.type == pygame.KEYDOWN and event.key == K_SPACE:
					Busy = pygame.mixer.music.get_busy()
					#doesn't work
					print Busy
					if Busy == False:
						pygame.mixer.music.unpause()
					if Busy == True:
						pygame.mixer.music.pause()

				if event.type == pygame.QUIT:
					sys.exit()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					pygame.mixer.music.stop()
					return self.MusicArtist()
	

	def ChooseNHL(self):
		NHL = pygame.image.load(os.path.join('imgs','NHL.jpg'))
		screen.blit(NHL,(0,0))

		NFL = pygame.image.load(os.path.join('imgs','NFL.jpg'))
		screen.blit(NFL,(300,0))

		NBA = pygame.image.load(os.path.join('imgs','NBA.jpg'))
		screen.blit(NBA,(0,200))

		MLB = pygame.image.load(os.path.join('imgs','MLB.jpg'))
		screen.blit(MLB,(300,200))
		pygame.display.flip()

		pygame.draw.rect(screen, (150,20,215), Rect((0,0), (299, 199)), 5)
		pygame.display.flip()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
					return self.ChooseNFL()

				if event.type == pygame.KEYDOWN and event.key == K_DOWN:
					return self.ChooseNBA()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					return self.nhlscreen()

				if event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.Choosesports()

				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()


	def ChooseNFL(self):
		NHL = pygame.image.load(os.path.join('imgs','NHL.jpg'))
		screen.blit(NHL,(0,0))

		NFL = pygame.image.load(os.path.join('imgs','NFL.jpg'))
		screen.blit(NFL,(300,0))

		NBA = pygame.image.load(os.path.join('imgs','NBA.jpg'))
		screen.blit(NBA,(0,200))

		MLB = pygame.image.load(os.path.join('imgs','MLB.jpg'))
		screen.blit(MLB,(300,200))
		pygame.display.flip()

		pygame.draw.rect(screen, (150,20,215), Rect((300,0), (299, 199)), 5)
		pygame.display.flip()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_LEFT:
					return self.ChooseNHL()

				if event.type == pygame.KEYDOWN and event.key == K_DOWN:
					return self.ChooseMLB()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					return self.nflscreen()

				if event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.Choosesports()

				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()


	def ChooseNBA(self):
		NHL = pygame.image.load(os.path.join('imgs','NHL.jpg'))
		screen.blit(NHL,(0,0))

		NFL = pygame.image.load(os.path.join('imgs','NFL.jpg'))
		screen.blit(NFL,(300,0))

		NBA = pygame.image.load(os.path.join('imgs','NBA.jpg'))
		screen.blit(NBA,(0,200))

		MLB = pygame.image.load(os.path.join('imgs','MLB.jpg'))
		screen.blit(MLB,(300,200))
		pygame.display.flip()

		pygame.draw.rect(screen, (150,20,215), Rect((0,200), (299, 199)), 5)
		pygame.display.flip()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
					return self.ChooseMLB()

				if event.type == pygame.KEYDOWN and event.key == K_UP:
					return self.ChooseNHL()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					return self.nbascreen()

				if event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.Choosesports()

				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()


	def ChooseMLB(self):
		NHL = pygame.image.load(os.path.join('imgs','NHL.jpg'))
		screen.blit(NHL,(0,0))

		NFL = pygame.image.load(os.path.join('imgs','NFL.jpg'))
		screen.blit(NFL,(300,0))

		NBA = pygame.image.load(os.path.join('imgs','NBA.jpg'))
		screen.blit(NBA,(0,200))

		MLB = pygame.image.load(os.path.join('imgs','MLB.jpg'))
		screen.blit(MLB,(300,200))
		pygame.display.flip()

		pygame.draw.rect(screen, (150,20,215), Rect((300,200), (299, 199)), 5)
		pygame.display.flip()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == K_LEFT:
					return self.ChooseNBA()

				if event.type == pygame.KEYDOWN and event.key == K_UP:
					return self.ChooseNFL()

				if event.type == pygame.KEYDOWN and event.key == K_RETURN:
					return self.mlbscreen()

				if event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.Choosesports()

				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()	

		

	def nhlscreen(self):
		pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)
		scoreImg = []
		for i in sportScores.getNHLScores():
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
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.ChooseNHL()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()

	def nflscreen(self):
		pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)
		scoreImg = []
		for i in sportScores.getNFLScores():
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
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.ChooseNFL()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()

	def nbascreen(self):
		pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)
		scoreImg = []
		for i in sportScores.getNBAScores():
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
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.ChooseNBA()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()

	def mlbscreen(self):
		pygame.draw.rect(screen, (0,0,0), (0,0, width, height), 0)
		scoreImg = []
		for i in sportScores.getMLBScores():
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
					sys.exit()

				elif event.type == KEYDOWN and event.key == K_BACKSPACE:
					return self.ChooseMLB()
	
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()


class Sports:
	nflScores = []
	nbaScores = []
	nhlScores = []
	def __init__(self): #the first thing that happens when you make a new "sports object"
		self.updateScores()

	def updateScores(self): #updates the scores
		self.nflScores = scores.getScores('nfl') #this calls get scores which is in the scores.py file
		self.nbaScores = scores.getScores('nba')
		self.nhlScores = scores.getScores('nhl')
		self.mlbScores = scores.getScores('mlb')
		print "scores updated"

	def printScores(self): #prints all of the scores
		print "NFL:"
		for game in self.nflScores:
			print game
		print "NBA:"
		for game in self.nbaScores:
			print game
		print "NHL:"
		for game in self.nhlScores:
			print game

	def getNFLScores(self):
		return self.nflScores

	def getNHLScores(self):
		return self.nhlScores

	def getNBAScores(self):
		return self.nbaScores

	def getMLBScores(self):
		return self.mlbScores


sportScores = Sports() #this creates a new sports object and calls the __in
startmenu = Mainmenu()	
startmenu.Chooseweather()
