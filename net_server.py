import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
sock.bind(addr)
sock.listen(5)
while True:
	(connectedSock, clientAddress) = sock.accept()
	try:
		msg = connectedSock.recv(1024).decode()
		output = msg.length() * "-"
		connectedSock.sendall(output.encode())
	except:
		sock.close()