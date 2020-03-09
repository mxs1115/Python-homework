#!/usr/bin/python3
# -*- coding: utf-8 -*-

#给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出

s="People always say that we are lacking of the eyes of realizing the beauty in life.that,of,the,the"
s=s.replace(',',' ')
s=s.replace('.',' ')
s=s.split(' ')
dict1={}
for k in s:
    if k in dict1:
        dict1[k]+=1
    else:
        dict1[k]=1
b=sorted(dict1.items(),key=lambda y: y[1],reverse=True)
print(b)