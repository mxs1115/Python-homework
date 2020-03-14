#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 编写一个函数,接收n个数字，求这些参数数字的和;

def sum1( *var ):
    s=0
    for i in var:
        s=s+i
    print("总和为：", s)

sum1(1,3,4,6,10,100)