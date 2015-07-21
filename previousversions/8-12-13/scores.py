import urllib

def getScores(sport):
	url = "http://sports.espn.go.com/%s/bottomline/scores" % sport
	page = urllib.urlopen(url).read()
	hasNext = True
	i = 1
	games = []
	while hasNext:
		if "left%d" %i in page:
			left = page.find("left%d" %i)
			right = page.find("right%d" %i)
			if i>9:
				strin = page[left+7:right-7]
			else:
				strin = page[left+6:right-7]
			games.append(strin.replace('%20', " "))
			i+=1
		else:
			hasNext = False
	return games

