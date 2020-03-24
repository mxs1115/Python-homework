#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

#2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx

def read_file():
    try:
        with open("input.txt","r") as f:
            list1=[]
            while True:
                s=f.readline()
                if not s:
                    break
                list1.append(s)
    except IOError as e:
        print(e)
    for i,s in enumerate(list1,start=1):
        print("第{}行：{}".format(i,s),end="")

read_file()