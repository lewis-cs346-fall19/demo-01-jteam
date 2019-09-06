import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
sock.bind(addr)
sock.listen(5)
while True:
	(connectedSock, clientAddress) = sock.accept()
	print("got 1")
	while True:
		try:
			msg = connectedSock.recv(1024).decode()
			print("got 2: " + msg + str(type(msg)))
       		output = len(msg) * "-"
 	      	connectedSock.sendall(output.encode())
 	      	print("got 3")
		except:
			connectedSock.close()
			print("got 4")
			break
		print("got 2: " + msg + str(type(msg)))
		output = len(msg) * "-"
		connectedSock.sendall(output.encode())
		print("got 3")
