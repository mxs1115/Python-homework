#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,time

#6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 
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



def fileshow():
    path=input("请输入一个文件路径：")
    print("{:<30}{:<30}{:<30}{}".format("名称","日期","类型","大小"))
    filist=[]
    filist = os.listdir(path)
    for f in filist:
        f=os.path.join(path,f)
        timeStruct = time.localtime(os.path.getctime(f))
        if(os.path.isfile(f)):
            print("{:<32}{:<32}{:<30}{}".format(os.path.basename(f),time.strftime('%Y-%m-%d %H:%M:%S',timeStruct),os.path.splitext(f)[1]+"文件",size1(os.path.getsize(f))))
        if(os.path.isdir(f)):
            print("{:<32}{:<32}{:<30}".format(os.path.basename(f),time.strftime('%Y-%m-%d %H:%M:%S'),"文件夹"))

fileshow()