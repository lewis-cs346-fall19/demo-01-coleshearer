import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost",54421)
sock.connect(addr)
for i in range(5):
    msg = input()
    sock.sendall(msg.encode())
    #print(sock.recv(1024).decode())
    print("received")
