import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8080))
print("UDP服务器在端口：8080准备就绪......")
while True:
    data, address = s.recvfrom(2048)
    print("接收到一次传输:" + bytes.decode(data))
    s.sendto(data.upper(), address)
