import pygame, sys, os
import MusicPlayer
from songClass import song
from pygame.locals import *
from pprint import pprint


class MusicPage:

	def __init__(self, screen, clock, statusBar):
		#constants
		self.ITEMS_ON_PAGE = 10
		self.ITEM_SPACING = 25
		self.ITEM_PADDING = 100
		self.ITEM_X = 100
		self.SELECTION_BOX_WIDTH = 300

		self.online = False

		self.selection = 0
		self.hold_selection = 0
		self.first_item = 0

		print "music page initialized"
		self.statusBar = statusBar
		self.running = False
		self.screen = screen

		self.current_list = [] # this will either be artists or songs by an artist
		
		self.list_is_artists = 1

		self.clock = clock
		self.mainScreenOrigin = ((0,screen.get_height()/10))
		self.mainScreenSize = ((screen.get_width(), screen.get_height() - (screen.get_height()/10)))
		
		self.background = pygame.image.load(os.path.join('imgs', 'mainbackground.jpg'))
		#self.background = pygame.transform.scale(self.background, (self.mainScreenSize))
		self.background = pygame.Surface((self.mainScreenSize))
		self.background.fill((0,0,0))

		self.mp = MusicPlayer.MusicPlayer()	

		self.current_list = self.mp.artists

		self.font = pygame.font.Font(None, 36)

		self.current_song = 0

	def checkSelectionBounds(self):
		if self.current_song < 0:
			self.current_song = 0

		if self.current_song < self.first_item:
			self.first_item = self.current_song

		if self.current_song > (self.first_item + self.ITEMS_ON_PAGE - 1):
			self.first_item = (self.current_song - self.ITEMS_ON_PAGE) + 1


	def drawSelectionBox(self):
		s = pygame.Surface((self.SELECTION_BOX_WIDTH, self.ITEM_SPACING))  # the size of your rect
		s.set_alpha(64)                # alpha level
		s.fill((255,255,255))           # this fills the entire surface
		self.screen.blit(s, (self.ITEM_X, ((self.current_song - self.first_item) * self.ITEM_SPACING)+self.ITEM_PADDING))    # (0,0) are the top-left coordinates

	def drawList(self):
		for i in range(0, self.ITEMS_ON_PAGE):
			try:
				if i < len(self.current_list):
					if self.list_is_artists:
						item = self.font.render(str(self.current_list[i+self.first_item]), 1, (150,234,255))
					else:
						item = self.font.render(str(self.current_list[i+self.first_item].song), 1, (150,234,255))

					self.screen.blit(item, (self.ITEM_X, (self.ITEM_SPACING*i) + self.ITEM_PADDING))
			except:
				continue#print "Encoding error"
		
		
	def draw(self):
		self.screen.blit(self.background, (self.mainScreenOrigin))

		time = self.font.render(str(self.mp.get_pos()), 1, (10,234,255))
		self.screen.blit(time, (300, 300))
		
		self.drawList()
		self.drawSelectionBox()

		self.statusBar.update()
		pygame.display.flip()
		
	def update(self):
		self.draw()

	def print_current_selection(self):
		if self.list_is_artists:
			print "current_selection: %s " % self.current_list[self.current_song]
		else:
			print "current_selection: %s " % self.current_list[self.current_song].song
	
	def musicMainLoop(self):
		while 1:
			self.clock.tick(30)
			for event in pygame.event.get():
			
			###keydown events
				if event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						sys.exit()
					if event.key == K_BACKSPACE:
						self.running = False
					if event.key == K_UP:
						self.current_song -= 1
						if self.current_song < 0:
							self.current_song = 0
						self.print_current_selection()
						self.checkSelectionBounds()
						#self.print_current_song()
					if event.key == K_DOWN:
						self.current_song += 1
						if self.current_song > len(self.current_list) - 1:
							self.current_song = len(self.current_list) - 1
						self.print_current_selection()
						#self.print_current_song()
						self.checkSelectionBounds()
					if event.key == K_p:
						self.mp.pause()
					if event.key == K_u:
						self.mp.unpause()
					if event.key == K_l:
						print self.songs[self.current_song].filePath
						self.mp.load(self.songs[self.current_song])
					if event.key == K_q:
						self.mp.play()
					if event.key == K_s:
						self.mp.stop()
					if event.key == K_g:
						self.songs = self.mp.get_songs_by_artist('Taylor Swift')
						self.print_current_song()
					if event.key == K_RETURN:
						if self.list_is_artists:
							self.list_is_artists = 0
							self.current_list = self.mp.get_songs_by_artist(self.current_list[self.current_song])
							self.hold_selection = self.current_song
							self.current_song = 0
						else:
							self.mp.load(self.current_list[self.current_song])
							self.mp.play()
						
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
		self.musicMainLoop()

