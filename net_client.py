import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
print("got here")
for i in range(100):
	sock.connect(addr)
	print("got 1")
	msg = i * "O"
	sock.sendall(msg.encode())
	print("got 2")
	reply = sock.recv(1024).decode()
	print(reply)
	sock.close()
	print("got 3")