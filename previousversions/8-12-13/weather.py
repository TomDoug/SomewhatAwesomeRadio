import urllib
class weather:

	def __init__(self):
		self.url = "http://w1.weather.gov/xml/current_obs/KBUF.rss"
		self.page = urllib.urlopen(self.url).read()
		self.body = self.page[self.page.find('<item>')+8:]
		self.date = str(self.page[(self.page.find('<lastBuildDate>')+15):self.page.find('</lastBuildDate>')-5])
		self.title = str(self.body[self.body.find('<title>')+8:self.body.find('</title>')])
		self.description = str(self.body[self.body.find('<br />]]>')+10:self.body.find('Last Updated')])
	def getDate(self):
		return self.date
	def getTitle(self):
		return self.title
	def getDescription(self):
		return self.description

if __name__ == '__main__':
	w = weather()
	print w.getDescription()
