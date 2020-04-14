#!/usr/bin/python3
# -*- coding: utf-8 -*-


#二 定义一个学生Student类。有下面的类属性：
#1 姓名 name
#2 年龄 age
#3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
#类方法：
#1 获取学生的姓名：get_name() 返回类型:str
#2 获取学生的年龄：get_age() 返回类型:int
#3 返回3门科目中最高的分数。get_course() 返回类型:int
#写好类以后，可以定义2个同学测试下:


class Student:
    def __init__(self,n,a,c,m,e):
        self.name=n
        self.age=a
        if not isinstance(c, int):
            raise ValueError('score must be an integer!')
        if not isinstance(m, int):
            raise ValueError('score must be an integer!')
        if not isinstance(e, int):
            raise ValueError('score must be an integer!')
        self.chinese=c
        self.maths=m
        self.english=e
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        list1=[]
        list1.append(self.chinese)
        list1.append(self.maths)
        list1.append(self.english)
        b=sorted(list1,reverse=True)
        return b[0]

student1=Student("张三",16,88,79,96)
student2=Student("李四",18,90,89,76)
print("{}岁的{}最高分数为{}".format(student1.get_age(),student1.get_name(),student1.get_course()))
print("{}岁的{}最高分数为{}".format(student2.get_age(),student2.get_name(),student2.get_course()))