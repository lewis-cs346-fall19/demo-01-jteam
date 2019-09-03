import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
sock.bind(addr)
sock.listen(5)
while True
	(connectedSock, clientAddress) = sock.accept()
	try
		msg = sock.recv(1024).decode()
		output = msg.length() * "-"
		sock.sendall(output.encode())
	except
		sock.close()