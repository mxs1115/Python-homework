#!/usr/bin/python3
# -*- coding: utf-8 -*-

#打印输出9*9乘法表
for i in range(1,10):
    for k in range(1,i+1):
        print("%d*%d=%d"%(k,i,k*i),end=" ")
    print()
