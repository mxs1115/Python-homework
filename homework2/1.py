#!/usr/bin/python3
# -*- coding: utf-8 -*-

#写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者

def rt(a):
    return len(a)
n=eval(input("请输入一个字符串或列表或是元组,字符串请加引号"))
print("它的长度为",rt(n))