import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
sock.bind(addr)
sock.listen(5)
while True:
	(connectedSock, clientAddress) = sock.accept()
	print("got 1")
	try:
		msg = sock.recv(1024).decode()
		print("got 2")
		output = msg.length() * "-"
		sock.sendall(output.encode())
		print("got 3")
	except:
		sock.close()
		print("got 4")