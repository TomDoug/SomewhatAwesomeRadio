import scores
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
