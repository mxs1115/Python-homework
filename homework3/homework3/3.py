#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

#3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出

def student():
    try:
        with open("student.txt") as f:
            list1=[]
            while True:
                s=f.readline()
                if not s:
                    break
                #s=s.rstrip()
                s=s.split()
                list(s)
                list1.append(s)
    except IOError as e:
        print(e)
    list1=sorted(list1,key=lambda y:y[2],reverse=True)
    for i in list1:
        list2=[" "]
        k=len(i[1])
        m=5
        while(m>k):
            list2.append("  ")
            #print(list2)
            m-=1
        print(i[0],"     ",i[1],"".join(list2),i[2])

student()