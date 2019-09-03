import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
print("got here")
for i in range(100):
	sock.connect(addr)
	print("got there")
	msg = i * " "
	sock.sendall(msg.encode())
	reply = sock.recv(1024)
	print(reply)
	sock.close()