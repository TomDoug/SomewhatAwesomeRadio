import urllib2


class MusicInterface():
	def __init__(self):
		self.ip = 'localhost'
		print "MusicInterface init"
	def getSongs(self):
		songs = urllib2.urlopen("http://"+self.ip + "/").read()
		print songs
	def playSong(self, song):
		urllib2.urlopen("http://" + self.ip +"/play/" + song)
	def pause(self):	
		urllib2.urlopen("http://" + self.ip +"/pause")
	def stop(self):
		urllib2.urlopen("http://" + self.ip +"/stop")

if __name__ == "__main__":
	m = MusicInterface()
	m.getSongs()
