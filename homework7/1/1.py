#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import os

#1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；

os.chdir(r"homework7\1")
with open("webspiderUrl.txt",'r',encoding='utf8') as f:
    list1=[]
    while True:
        x=f.readline()
        if not x:
            break
        url=re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',x) 
        list1.append(str(url))

with open('Url.txt','w',encoding='utf8') as f:
    for x in list1:
        f.write(x)
        f.write("\n")