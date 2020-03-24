#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

#5 文件编程小项目

s="""
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind
"""
try:
    with open("Blowing in the wind.txt","w") as f:
        f.write(s)
    with open("Blowing in the wind.txt","r+") as f:
        old=f.read()
        f.seek(0)
        f.write("Blowin’ in the wind   Bob Dylan")
        f.write(old)
    with open("Blowing in the wind.txt","a+") as f:
        f.write("1962 by Warner Bros.lnc.")
    with open("Blowing in the wind.txt","r") as f:
        print(f.read())
    
except IOError as e:
    print(e)


