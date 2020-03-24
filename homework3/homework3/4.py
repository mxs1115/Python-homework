#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import string

#4 题目要求：
 #在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
 #将当前img目录所有以.png结尾的后缀名改为.jpg.

def creat_file():
    
    list2=[]
    for i in range(10):
        list2.append("".join(random.sample(string.ascii_letters+string.digits,4)))
    os.mkdir('img')
    for name in list2:
        f=open('img/'+name+'.png',"w+")
        f.close

def Suffix_modification(directory,old_suffix,new_suffix):
    if os.path.exists(directory):
        pngfile=[name for name in os.listdir(directory) if name.endswith(old_suffix)]
        file_name=[os.path.splitext(name)[0] for name in pngfile]
        for name in file_name:
            oldname=os.path.join(directory,name+old_suffix)
            newname=os.path.join(directory,name+new_suffix)
            os.rename(oldname,newname)
        print("{}文件已改为{}文件".format(old_suffix,new_suffix))

creat_file()
Suffix_modification('img','.png','.jpg')