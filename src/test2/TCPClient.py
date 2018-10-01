import socket

c = socket.socket()
c.connect(("127.0.0.1", 8080))
send_data = input("输入要转换的字符串：")
c.send(str.encode(send_data))
recv_data = c.recv(1024)
print("From TCP Server:" + bytes.decode(recv_data))
c.close()
