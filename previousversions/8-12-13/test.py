import MenuAnimation
import pygame, os
size = width, height = 600, 400
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
imageWidth = width/2

mainHeightOrigin = height/10
mainHeight = height - (height/10)		
imageHeight = int(mainHeight*(.75))
mainImageOrigin = ((width/2)-(imageWidth/2), ((mainHeight/2)-(imageHeight/2))+mainHeightOrigin)
clock = pygame.time.Clock()


def loadIcons():
	icons = [loadImage('weather.png'), loadImage('music.png'), loadImage('sports.png'), loadImage('pong.png'), loadImage('messages.png')]
	return icons
		
def loadImage(path):
	return pygame.image.load(os.path.join('imgs',path))

if __name__ == "__main__":
	animator = MenuAnimation.AnimationGenerator()
	icons = loadIcons()
	while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
					
				if event.type == pygame.KEYDOWN:
					if event.key == K_RIGHT:
						print ""						
					
					if event.key == K_LEFT:
						print ""						
					if event.key == K_ESCAPE:
						sys.exit()
			animator.timeIncriment()
			clock.tick(30)
			pygame.draw.rect(screen, (0,0,0),(0,0,width,height),0)
			animator.paintImages(screen, icons[0], icons[1], icons[2])
			pygame.display.flip()