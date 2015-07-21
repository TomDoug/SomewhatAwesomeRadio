import serial, time, pygame
from threading import Thread
class Serial(Thread):
	def run(self):
		ser = serial.Serial(
			port = '/dev/ttyACM0',
			baudrate = 9600)
		ser.open()
		while 1:
			re = ser.read(1)
			time.sleep(.2)
			if re == '2':
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_RIGHT})
				pygame.event.post(event)
				
			if re == '3':
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_LEFT})
				pygame.event.post(event)
			if re == '4':
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_RETURN})
				pygame.event.post(event)
			if re == '5':
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_BACKSPACE})
				pygame.event.post(event)
a = Serial()
a.start()
