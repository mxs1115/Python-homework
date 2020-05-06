#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname() 

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
try:
    s.connect((host, port))
    print("连接到服务器")
except :                         
    print ('连接不成功')


# 接收小于 1024 字节的数据
while(True):
    msg = s.recv(1024)  
    print("客户端接收：%s" % msg.decode("utf-8"))#把接收到的数据进行解码
    print("读取完成")	
    if msg == b"EOF":
        break
    if msg == b"quit":
        s.close()
        print("程序结束\n")
        exit()


    #发送消息
    msg = input("客户端发送:")
    s.send(msg.encode(encoding='utf-8'))
    print("发送完成")
    if msg == "EOF":
        break
    if msg == "quit":
        s.close()
        print("程序结束\n")
        exit()       
print("程序结束\n")
 
