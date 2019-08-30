import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0",54421)
sock.bind(addr)
sock.listen(5)
for i in range(5):
    (connectedSock, clientAddress) = sock.accept()
    print(clientAddress)
try:
    msg = sock.recv(1024).decode()
except:
    sock.close()
    
sock.sendall(message.encode())




    
