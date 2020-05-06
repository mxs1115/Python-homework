#!/usr/bin/python
# -*- coding: UTF-8 -*-

#3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；


import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()
    print("连接地址: %s" % str(addr))
    while True:
        send_data=input("服务器发送消息:")
        clientsocket.send(send_data.encode('utf-8'))
        if send_data=='EOF':
            break
        if send_data=="quit":
            clientsocket.close()
            serversocket.close()
            exit()
        

        #读取消息
        msg = clientsocket.recv(1024)
        print("服务端接收:",msg.decode("utf-8"))
        print("读取完成")
        if msg == b"EOF":
            break
        if msg == b"quit":
            client.close()
            mySocket.close()
            print("程序结束\n")
            exit()