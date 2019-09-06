#Author: Jonah Little

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
sock.bind(addr)
sock.listen(5)
while True:
	(connectedSock, clientAddress) = sock.accept()
	while True:
		try:
			msg = connectedSock.recv(1024).decode()
			print(msg)
			reply = len(msg) * "-"
			connectedSock.sendall(reply.encode())
		except:
			connectedSock.close()
			break