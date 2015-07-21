import socket, sys, pickle
from threading import Thread
import os, songClass
import pexpectTest, MySQLdb
class server(Thread):
	def run(self):
		self.running = True
		self.host = ''
		self.port = 9026
		
	#	raspi = '192.168.1.111'
	#	self.db = MySQLdb.connect(host=raspi, user='root', passwd='pi', db='SuperAwesomeRadio')
	#	self.cur = db.cursor()
	#	self.db.autocommit()
		
		self.songs = []
		x = 0
		for (dirpath, dirname, filenames) in os.walk(os.getenv("HOME")+'/Music'): 
		
			for i in filenames:
				if i.find('.mp3') != -1:
					path = dirpath + "/" + i
					#makes a new instance of the song class for each song
					self.songs.append(songClass.song(path))
					if x == 0:
						self.currentSong = songClass.song(path)
					x+=1	
		self.connect()
	def connect(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print 'socket created'
		
		self.mpg = pexpectTest.mpg()
		
		self.num = 0
		
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		self.s.bind((self.host, self.port))

		print "Socket binded"

		self.s.listen(5)

		self.clsock, addr = self.s.accept()
		self.inputLoop()
			
	
	def inputLoop(self):
		while self.running:
			inMess = self.getMessage()
			print inMess
			if inMess == "getSongs":
				self.getSongs()
			if inMess == 'quit':
				self.running = False
				break
			if inMess == '0':
				print "playing"
				self.mpg.play(self.currentSong)
				cur.execute("SELECT filename FROM TimesPlayed")
				lis = cur.fetchall()
			#	if self.currentsong in lis:
			#		self.cur.execute("UPDATE TimesPlayed SET times_played = times_played + 1 where filename=" + self.currentSong)
			#	else:
			#		self.cur.execute("INSRET INTO TimesPlayed(filename, times_played) VALUES(" + self.currentSong + ",1)")
			if inMess == '1':
				print "Stopping Song"
				self.mpg.stop()
			if inMess == '2':
				print "pausing"
				self.mpg.pause()
			if inMess.find("loadSong:") != -1:
				print "loading" + inMess[9:]
				self.loadSong(inMess[9:])
		
		self.clsock.close()
		self.s.close()
		self.connect()

	def sendMessage(self, message):
		self.clsock.send(message)
	def getSongs(self):
		pick = pickle.dumps(self.songs)
		open('p.txt', 'w+').write(pick)

		self.sendMessage(pick)
	def getMessage(self):
		d = ''
		string = ""
				
		string = self.clsock.recv(1024)
		if string == 'quit':
			self.running = False
			print "stopp"
		return string
	def loadSong(self, son):
		self.currentSong = son

t = server()
t.start()
