import socket, sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8888)
while 1:
	message = raw_input("message: ")
	
	sent = sock.sendto(message, server_address)
	if message == "stop":
		break

sock.close()
