#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random

#使用random模块，生成随机数，来初始化一个列表，元组；

list1=[random.randint(1,30) for i in range(10)]
tuple1=tuple([random.randint(1,100) for i in range(8)])
print("随机生成的列表为:",list1)
print("随机生成的元组为:",tuple1)
