#!/usr/bin/python3
# -*- coding: utf-8 -*-

#前面2个元素为0，1，输出100以内的斐波那契数列
f1=0
f2=1
print(f1,end=" ")
print(f2,end=" ")
for fn in range(101):
    if(fn==f1+f2):
        print(fn,end=" ")
        f1=f2
        f2=fn
    
