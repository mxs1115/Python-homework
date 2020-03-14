#!/usr/bin/python3
# -*- coding: utf-8 -*-

#编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)

def cacluate():
    a=int(input("请输入第一个数"))
    b=int(input("请输入第二个数"))
    c=input("请输入要执行的运算（(+-*/）")
    if(c=="+"):
        print(a+b)
    elif(c=="-"):
        print(a-b)
    elif(c=="*"):
        print(a*b)
    elif(c=="/"):
        print(a/b)
cacluate()