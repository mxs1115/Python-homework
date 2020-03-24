#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

#1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；

def input1():
    list1=[]
    while True:
        s=input("请输入数据：(输入空行结束)")
        if not s:
            return list1
        list1.append(s)

def write_file(list):
    try:
        with open("input.txt","w") as f:
            for x in list:
                f.write(x)
                f.write("\n")
    except IOError as e:
        print(e)
    print("写入文件成功!")

write_file(input1())