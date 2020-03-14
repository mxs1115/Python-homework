#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 定义一个函数, 打印输出n以内的斐波那契数列;

def Fibonacci(n):
    f1=0
    f2=1
    fn=1
    while(fn<=n):
        print(fn,end=" ")
        fn=f2+f1
        f1=f2
        f2=fn
m=int(input("请输入要打印多少以内的斐波那契数列"))
Fibonacci(m)

