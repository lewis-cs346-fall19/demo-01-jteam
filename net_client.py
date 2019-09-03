import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
sock.connect(addr)
for i in range(100)
	msg = i * " "
	sock.sendall(msg.encode())
	reply = sock.recv()
	print(sock.recv)
	sock.close()