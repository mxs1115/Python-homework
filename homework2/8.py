#!/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import Counter

#请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
 #例如，输入 aaaabbc，输出：a:4

def most(str):
    count=Counter(str)
    b=sorted(count.items(),key=lambda y:y[1],reverse=True)
    print("出现次数最多的字符为:")
    print("{}:{}".format(b[0][0],b[0][1]))
s=input("请输入一串字符：")
most(s)

