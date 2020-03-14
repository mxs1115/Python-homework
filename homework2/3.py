#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random

#编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#数字列表请用随机数函数生成;

def print_OddNumber( list1 ):
    print("传入列表为：",list1)
    print("列表中的奇数有:")
    for i in list1:
        if( i%2 != 0 ):
            print(i)

list1=[random.randint(1,50) for i in range(10) ]
print_OddNumber(list1)