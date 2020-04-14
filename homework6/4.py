#!/usr/bin/python3
# -*- coding: utf-8 -*-


#四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
    #封装方法，求单个学生的总分，平均分，以及打印学生的信息。

class Students:
    def __init__(self,n,o,s,e,m,c):
        self.name=n
        self.old=o
        self.sex=s
        self.english=e
        self.maths=m
        self.chinese=c
    def total(self):
        print("{}的语数英总分为:{}".format(self.name,self.maths+self.chinese+self.english))
    def average_score(self):
        print("{}的语数英平均分为:{}".format(self.name,(self.chinese+self.maths+self.english)/3))
    def print_information(self):
        print("这位学生的姓名是:{},年龄{},性别:{},英语成绩:{},数学成绩:{},语文成绩:{}".format(self.name,self.old,self.sex,self.english,self.maths,self.chinese))
    
student1=Students("李明",19,"男",78,95,79)
student1.total()
student1.average_score()
student1.print_information()
