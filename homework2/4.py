#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
s=" sdfeege 123ABC ,$"
def count1(str):
    s=0
    n=0
    k=0
    e=0
    for i in str:
        if i.isalpha():
            s+=1
        elif i.isdigit():
            n+=1
        elif i.isspace():
            k+=1
        else:
            e+=1
    print("字母有{}个，数字有{}个，空格有{}个，其他字符有{}个".format(s,n,k,e))

count1(s)
    