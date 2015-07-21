import socket, sys, pygame
from threading import Thread

class server(Thread):
	def run(self):
		self.host = ''
		self.port = 8888
		
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print "socket created"
		
		s.bind((self.host, self.port))

		print "Socket has been binded"
		while 1:
			d = s.recvfrom(1024)
			data = d[0]
			addr = d[1]

			print "Message[" + addr[0] + ':' + str(addr[1]) + '] - '+ data.strip()
			if data.strip() == "stop":
				event = pygame.event.Event(pygame.QUIT)
				pygame.event.post(event)
				break
			if data.strip() == "right":
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_RIGHT})
				pygame.event.post(event)
			if data.strip() == "left":
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_LEFT})
				pygame.event.post(event)
			if data.strip() == "up":
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_UP})
				pygame.event.post(event)
			if data.strip() == "down":
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_DOWN})
				pygame.event.post(event)
			if data.strip() == "escape":
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_ESCAPE})
				pygame.event.post(event)
			if data.strip() == "enter":
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_RETURN})
				pygame.event.post(event)
			if data.strip() == "backspace":
				event = pygame.event.Event(pygame.KEYDOWN, {'key':pygame.K_BACKSPACE})
				pygame.event.post(event)


		print "server stopped"
		s.close()
#s = server()
#s.start()
