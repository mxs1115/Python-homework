#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random

#随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
    #A---成绩>=90;  
    #B-->成绩在 [80,90)
    #C-->成绩在 [70,80)
    #D-->成绩<70

def grade(list1):
    g=[]
    for i in list1:
        if(i>=90):
            g.append("{}-->A".format(i))
        elif(i>=80):
            g.append("{}-->B".format(i))
        elif(i>=70):
            g.append("{}-->C".format(i))
        else:
            g.append("{}-->D".format(i))
    print("评定等级如下：")
    print(g)
score=[random.randint(0,100) for i in range(20)]
grade(score)