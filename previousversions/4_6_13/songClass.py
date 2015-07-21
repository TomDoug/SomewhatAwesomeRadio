import id3reader
class song():
	artist = ""
	song = " "
	filePath = ""
	album = ""
	index = -1
	def __init__(self, fileP):
		self.filePath = fileP
		try:

			id3r = id3reader.Reader(self.filePath)
			self.artist = id3r.getValue('performer')
			self.album = id3r.getValue('album')
			self.song = id3r.getValue('title')
		except:
			pass
