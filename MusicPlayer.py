import sys, os
import pygame
from songClass import song
from pygame.locals import *
import sqlite3
from pprint import pprint

class MusicPlayer:
	def __init__(self):
		self.lol = 1
		self.playlist = []
		self.shuffle = False
		self.con = None
		self.create_songs()
		songs = []
		
		for i in songs:
			print i.song

	def playSong(self, song):
		self.loadSong(song)
		self.play()

	def play(self):
		pygame.mixer.music.play(0)
		pygame.mixer.music.pause()
		pygame.mixer.music.play(0)

	def pause(self):
		pygame.mixer.music.pause()

	def unpause(self):
		pygame.mixer.music.unpause()

	def stop(self):
		pygame.mixer.music.stop()

	def load(self, song):
		pygame.mixer.music.load(song.filePath)

	def get_pos(self):
		return pygame.mixer.music.get_pos()

	def get_current_song(self):
		return self.currentSong

	def create_songs(self):
		self.songs = []
		self.artists = []
		try:
			self.con = sqlite3.connect('songs.db')
			self.cur = self.con.cursor()
			self.cur.execute("SELECT * FROM Songs ORDER BY Title ASC")
			songs = self.cur.fetchall()
			
		except sqlite3.Error, e:
			print str(e)

		for s in songs:	
			self.songs.append(song(s[0]))


		try:
			self.con = sqlite3.connect('songs.db')
			self.cur = self.con.cursor()
			self.cur.execute("SELECT DISTINCT Artist FROM Songs ORDER BY Artist ASC")
			arts = self.cur.fetchall()
			
		except sqlite3.Error, e:
			print str(e)


		for i in arts:
			self.artists.append(i[0])
				
		#pprint(self.artists)

	def get_songs_by_artist(self, artist):
		match = []
		try:
			self.con = sqlite3.connect('songs.db')
			self.cur = self.con.cursor()
			self.cur.execute("SELECT * FROM Songs WHERE Artist=? ORDER BY Title ASC", ([artist]))
			res = self.cur.fetchall()

			for s in res:	
				match.append(song(s[0]))
			print "found songs?"
			
		except sqlite3.Error, e:
			print str(e)
			print "SQL ERROR"

		
		pprint(match)
		
		return match

	def get_song_by_title(self, title):
		self.get_song_from_list_by_title(self.songs, title)

	def get_song_from_list_by_title(self, list, title):
		for i in list:
			if i.song is title:
				return i
