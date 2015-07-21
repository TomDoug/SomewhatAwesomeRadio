from threading import Thread
import socket, time
import pickle, songClass
class MusicPlayer():
	
	songs = []
	artists = []
	def __init__(self):
		host = '192.168.1.150'
		#host = '127.0.0.1'
		port = 9000
		self.num = 0
		self.songList = []
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((host,port))
		self.sendMessage("getSongs")
		songString = self.getMessage()
		time.sleep(2)
		#open('cli.txt', 'w+').write(songString)
		
		self.songList = pickle.loads(songString)
		#for i in self.songList:
		#	print i.filePath
		#sendMessage('stop')
		
	def load(self, filepath):
		self.sendMessage("loadSong:" + filepath)

	def getMessage(self):
		string = ""
		#d = self.s.recv(1024)
		d = ""
		self.s.settimeout(4)
		while 1:
			string = string + d
			try:
				d = self.s.recv(1024)
			except: break
			#if d.find("ABCEND"):break
		return string#[:len(string)-6]
	def sendMessage(self, message):
		self.s.send(message)
	def play(self):
		self.sendMessage('0')
	def loadNext(self):
		self.stop()
		self.sendMessage("loadSong:" + self.songList[self.num].filePath)
		self.num +=1
	def stop(self):
		self.sendMessage('1')
	def pause(self):
		self.sendMessage('2')
	def messageLoop(self):
		while 1:
			mess = raw_input('what is your message: ')
			if mess == 'play':
				self.play()
			elif mess == 'pause':
				self.pause()
			elif mess.find('load') != -1:
				self.loadNext()
			elif mess == 'stop':
				self.stop()
			else:
				self.sendMessage(mess)
			if mess == 'quit':break
