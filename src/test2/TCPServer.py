import socket

s = socket.socket()
s.bind(("127.0.0.1", 8080))
s.listen(5)
print("TCP服务器在端口：8080准备就绪......")
while True:
    c, _ = s.accept()
    recv_data = c.recv(1024)
    print("接收到一次传输：" + bytes.decode(recv_data))
    send_data = recv_data.upper()
    c.send(send_data)
    c.close()
