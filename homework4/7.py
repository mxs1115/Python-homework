#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

#7 使用python代码统计一个文件夹中所有文件的总大小

def size1(s):
    if(s<1024):
        fsize=str(s)+"B"
    elif(s<1048576):
        fsize=str(s/1024)+"KB"
    elif(s<1073741824):
        fsize=str(s/1048576)+"MB"
    else:
        fsize=str(s/1073741824)+"GB"
    return fsize

def getfilesize():
    size=0
    path=input("请输入一个文件地址:")
    for root, dirs, files in os.walk(path):
        for f in files:
            size+=os.path.getsize(os.path.join(root, f))
            print(f)
    print(size1(size))

getfilesize()