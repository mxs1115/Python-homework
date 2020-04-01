#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys,os


#5  通过Python来模拟实现一个txt文件的拷贝过程;


def copy(path1,path2):
    with open(path1,'r') as f:
            s=f.read()
            a=os.path.basename(path1)
    os.chdir(path2)
    with open(a,'w') as f:
        f.write(s)
    print("文件拷贝成功,拷贝文件在{}目录下".format(path2))


copy(r'123\333.txt','321')