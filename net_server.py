#Author: Jonah Little

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
sock.bind(addr)
sock.listen(5)
while True:
	(connectedSock, clientAddress) = sock.accept()
	print("here")
	try:
		msg = connectedSock.recv(1024).decode()
		if msg == "":
			raise Exception("No data")
		print(msg)
		print("anywhere")
		reply = len(msg) * "-"
		connectedSock.sendall(reply.encode())
		print("time")
	except:
		connectedSock.close()