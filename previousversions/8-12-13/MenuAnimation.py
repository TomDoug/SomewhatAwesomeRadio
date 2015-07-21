import pygame
class AnimationGenerator():
	def __init__(self, calcVars):

		print "Aminator initalized"
		self.animationTimeIncreasing = True
		self.animationTime = 0
		self.calcVars = calcVars
		self.LEFT = 0
		self.RIGHT = 1

	
	def paintImages(self, screen, imageList, currentSelection):
		#be sure to draw you background before invoking this method
		
		###############################
		#sets the index for the left and right images
		if currentSelection > 0:
			left = currentSelection-1
		else:
			left = len(imageList) - 1
		
		if currentSelection < len(imageList)-1:
			right = currentSelection+1
		else:
			right = 0
		###############################
		
		###############################
		#paints the left and right images to the screen
		screen.blit(pygame.transform.scale(imageList[left], (self.calcVars.subImageWidth, self.calcVars.subImageHeight)),self.calcVars.leftImageOrigin)
		screen.blit(pygame.transform.scale(imageList[right], (self.calcVars.subImageWidth, self.calcVars.subImageHeight)),self.calcVars.rightImageOrigin)
		###############################
		
		###############################
		#modifys the main image to corrispond to the animation and adding it to the 
		#newly created surface sur
		img = imageList[currentSelection]
		sur = pygame.Surface((self.calcVars.imageWidth, self.calcVars.imageHeight))
		sur.set_colorkey((255,1,255))
		pygame.draw.rect(sur,(255,1,255),(0,0,self.calcVars.width,self.calcVars.height),0)
		sur.blit(pygame.transform.scale(img,(self.calcVars.imageWidth-self.animationTime, self.calcVars.imageHeight-self.animationTime)),(self.animationTime/2,self.animationTime/2))
		###############################
		
		###############################
		#takes sur and draws it to the screen
		screen.blit(sur, self.calcVars.mainImageOrigin)
		###############################
		self.timeIncriment()
		
		#--->be sure to update the status bar and flip the screen in your loop<--------------
		
	def animateChange(self, screen, imageList, currentSelection, direction, changeFrameCounter):
		#direction 0-left    1-right
		#currentSelection- selection before change
		#be sure to set the background before invoking this method
		
		################################
		#This number will be used throughout the method
		frameRatio = (changeFrameCounter/self.calcVars.numberOfChangeFrames)
		################################
		
		################################
		#assign the inexes for all of the images.
		if direction == self.RIGHT:
			old = currentSelection
			new = old +1
			leaving = old -1
			entering = new +1
			if entering >len(imageList)-1:
				entering = entering - len(imageList)
			if new > len(imageList) - 1:
				new = new - len(imageList)
		
		elif direction == self.LEFT:
			old = currentSelection
			new = old -1
			leaving = old+1
			entering = new-1
			if old > len(imageList) -1:
				old = old-len(imageList)
			if leaving > len(imageList) -1:
				leaving = leaving-len(imageList)
		else:
			print "ERROR INVALID DIRECTION"
		#################################
			
		#The animation will be handled by 2 different blocks. The left and right blocks
		
		#################################
		#begining of right block
		if direction == self.RIGHT:
			
			################################
			#image leaving screen
			leavingImageXDistance = self.calcVars.leftImageOrigin[0] - self.calcVars.farLeftOrigin[0]
			leavingImage = pygame.transform.scale(imageList[leaving],(self.calcVars.subImageWidth, self.calcVars.subImageHeight))
			screen.blit(leavingImage,(self.calcVars.leftImageOrigin[0]-(frameRatio*leavingImageXDistance), self.calcVars.leftImageOrigin[1]))
			################################
			
			################################
			#old image
			oldImageXDistance = self.calcVars.mainImageOrigin[0]-self.calcVars.leftImageOrigin[0]
			oldImageYDistance = self.calcVars.mainImageOrigin[1]-self.calcVars.leftImageOrigin[1]
			oldImageTransformDistanceHeight = self.calcVars.imageHeight - self.calcVars.subImageHeight
			oldImageTransformDistanceWidth  = self.calcVars.imageWidth - self.calcVars.subImageWidth
			
			oldImage = pygame.transform.scale(imageList[old],(int(self.calcVars.imageWidth-(frameRatio*oldImageTransformDistanceWidth)),int(self.calcVars.imageHeight-(frameRatio*oldImageTransformDistanceHeight))))
			screen.blit(oldImage,(self.calcVars.mainImageOrigin[0]-(frameRatio*oldImageXDistance), self.calcVars.mainImageOrigin[1]-(frameRatio*oldImageYDistance)))
			################################
			
			################################
			#new image
			newImageXDistance = self.calcVars.rightImageOrigin[0]-self.calcVars.mainImageOrigin[0]
			newImageYDistance = self.calcVars.mainImageOrigin[1]-self.calcVars.rightImageOrigin[1]
			newImageTransformDistanceHeight = self.calcVars.imageHeight - self.calcVars.subImageHeight
			newImageTransformDistanceWidth  = self.calcVars.imageWidth - self.calcVars.subImageWidth
			
			newImage = pygame.transform.scale(imageList[new],(int(self.calcVars.subImageWidth + (frameRatio*newImageTransformDistanceWidth)),int(self.calcVars.subImageHeight+(frameRatio*newImageTransformDistanceHeight))))
			screen.blit(newImage,(self.calcVars.rightImageOrigin[0]-(frameRatio*newImageXDistance), self.calcVars.rightImageOrigin[1]+(frameRatio*newImageYDistance)))

			################################
			
			################################
			#image entering screen
			enteringImageXDistance = self.calcVars.farRightOrigin[0]-self.calcVars.rightImageOrigin[0]
			enteringImage = pygame.transform.scale(imageList[entering],(self.calcVars.subImageWidth, self.calcVars.subImageHeight))
			screen.blit(enteringImage,(self.calcVars.farRightOrigin[0]-(frameRatio*enteringImageXDistance), self.calcVars.leftImageOrigin[1]))

			################################
		#################################
		#begining of left block
		if direction == self.LEFT:
			################################
			#image entering screen
			enteringImageXDistance = self.calcVars.leftImageOrigin[0]-self.calcVars.farLeftOrigin[0]
			enteringImage = pygame.transform.scale(imageList[entering],(self.calcVars.subImageWidth, self.calcVars.subImageHeight))
			screen.blit(enteringImage,(self.calcVars.farLeftOrigin[0]+(frameRatio*enteringImageXDistance), self.calcVars.leftImageOrigin[1]))
			################################
			
			################################
			#old image
			oldImageXDistance = self.calcVars.mainImageOrigin[0]-self.calcVars.rightImageOrigin[0]
			oldImageYDistance = self.calcVars.mainImageOrigin[1]-self.calcVars.rightImageOrigin[1]
			oldImageTransformDistanceHeight = self.calcVars.imageHeight - self.calcVars.subImageHeight
			oldImageTransformDistanceWidth  = self.calcVars.imageWidth - self.calcVars.subImageWidth
			
			oldImage = pygame.transform.scale(imageList[old],(int(self.calcVars.imageWidth-(frameRatio*oldImageTransformDistanceWidth)),int(self.calcVars.imageHeight-(frameRatio*oldImageTransformDistanceHeight))))
			screen.blit(oldImage,(self.calcVars.mainImageOrigin[0]-(frameRatio*oldImageXDistance), self.calcVars.mainImageOrigin[1]-(frameRatio*oldImageYDistance)))
			################################
			
			################################
			#new image
			newImageXDistance = self.calcVars.mainImageOrigin[0]-self.calcVars.leftImageOrigin[0]
			newImageYDistance = self.calcVars.mainImageOrigin[1]-self.calcVars.leftImageOrigin[1]
			newImageTransformDistanceHeight = self.calcVars.imageHeight - self.calcVars.subImageHeight
			newImageTransformDistanceWidth  = self.calcVars.imageWidth - self.calcVars.subImageWidth
			
			newImage = pygame.transform.scale(imageList[new],(int(self.calcVars.subImageWidth + (frameRatio*newImageTransformDistanceWidth)),int(self.calcVars.subImageHeight+(frameRatio*newImageTransformDistanceHeight))))
			screen.blit(newImage,(self.calcVars.leftImageOrigin[0]+(frameRatio*newImageXDistance), self.calcVars.leftImageOrigin[1]+(frameRatio*newImageYDistance)))
	
			################################
			
			################################
			#image leaving screen
			leavingImageXDistance = self.calcVars.farRightOrigin[0]-self.calcVars.rightImageOrigin[0]
			leavingImage = pygame.transform.scale(imageList[leaving],(self.calcVars.subImageWidth, self.calcVars.subImageHeight))
			screen.blit(leavingImage,(self.calcVars.rightImageOrigin[0]+(frameRatio*enteringImageXDistance), self.calcVars.rightImageOrigin[1]))

			################################

						
		#return (changeFrameCounter < self.calcVars.numberOfChangeFrames)
		#Tells you if the image is still chaging
		#be sure to incriment/reset the change frame counter and the status bar, also flip screen
		
	def timeIncriment(self):
		if self.animationTimeIncreasing:
			self.animationTime += 1
		else:
			self.animationTime -= 1
		
		if self.animationTime > 10 or self.animationTime < 1:
				self.animationTimeIncreasing = not self.animationTimeIncreasing
