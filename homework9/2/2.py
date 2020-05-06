#!/usr/bin/python
# -*- coding: UTF-8 -*-

#2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；

from socket import *

def main():
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(('127.0.0.1',8888))
    while(True):
        recv_data = udp_socket.recvfrom(1024)
        recv_info = str(recv_data[0].decode("gbk"))
        recv_addr = recv_data[1]
        print("接收到的信息是：%s，内容来自：%s" % (recv_info, recv_addr))

if __name__=='__main__':
    main()

