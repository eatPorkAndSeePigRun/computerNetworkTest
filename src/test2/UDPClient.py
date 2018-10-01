import socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send_data = input("输入要转换的字符串：")
c.sendto(str.encode(send_data), ("127.0.0.1", 8080))
recv_data = c.recv(2048)
print("From UDP Server:" + bytes.decode(recv_data))
