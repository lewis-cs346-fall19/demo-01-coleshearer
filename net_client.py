import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost",54421)
sock.connect(addr)
for i in range(5):
    msg = input()
    sock.sendall()
    print(sock.recv())
