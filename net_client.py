#Author: Jonah Little

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
for i in range(100):
	sock.connect(addr)
	msg = (i + 1) * "O"
	sock.sendall(msg.encode())
	reply = sock.recv(1024).decode()
	print(reply)
	sock.close()