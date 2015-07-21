class CalcVars():

	#This class is a place to hold redundent variables used in the menu animator
	#that may be useful in other places. Give a reference to the instance generated in
	#the main gui and all other classes will be able to access these values without 
	#recalculating them.
	
	def __init__(self, width, height):
		self.padding = 0
		self.width = width
		self.height = height
		self.imageWidth = width/2
		self.mainHeightOrigin = height/10
		self.mainHeight = height - (height/10)
		self.imageHeight = int(self.mainHeight*(.75))
		self.mainImageOrigin = ((width/2)-(self.imageWidth/2), ((self.mainHeight/2)-(self.imageHeight/2))+self.mainHeightOrigin)
		self.subImageWidth = int(self.imageWidth*.8)
		self.subImageHeight = int(self.imageHeight*.8)
		self.leftImageOrigin = (((-self.subImageWidth/2)-self.padding), ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		self.rightImageOrigin = ((width-(self.subImageWidth/2)+self.padding), ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		self.farRightOrigin = ((width+(self.subImageWidth/2)+self.padding), ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		self.farLeftOrigin = (((-self.subImageWidth/2)-self.padding)-self.subImageWidth, ((self.mainHeight/2)-(self.subImageHeight/2))+self.mainHeightOrigin)
		self.numberOfChangeFrames = 15.0
		