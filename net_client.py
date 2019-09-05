import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 40836)
print("got here")
sock.connect(addr)
for i in range(100):
	msg = (i + 1) * "O"
	print("got 1:" + msg)
	sock.sendall(msg.encode())
	print("got 2")
	reply = sock.recv(1024).decode()
	print("got 3(" + reply + ")")
sock.close()
print("got 3")