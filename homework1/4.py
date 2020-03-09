#!/usr/bin/python3
# -*- coding: utf-8 -*-

#判断用户输入的年份是否为闰年

x=int(input('请输入一个年份: '))
if (x%400==0 or (x%4==0 and x%100!=0)):
    print(x,"是闰年")
else:
    print(x,"不是闰年")