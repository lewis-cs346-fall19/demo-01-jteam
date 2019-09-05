import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
sock.bind(addr)
sock.listen(5)
(connectedSock, clientAddress) = sock.accept()
while True:
	print("got 1")
	try:
		msg = connectedSock.recv(1024).decode()
		print("got 2: " + msg)
		output = msg.length() * "-"
		connectedSock.sendall(output.encode())
		print("got 3")
	except:
		connectedSock.close()
		print("got 4")
		break
print("finished")