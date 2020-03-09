#!/usr/bin/python3
# -*- coding: utf-8 -*-

#定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；

list1=[1,2,3,4,5,6,7,"333df"]
list2=[4,8,11,1,88,"333df"]
c=[x for x in list1 if x in list2]
print("两个列表中相同的元素有")
print(c)
