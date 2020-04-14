#!/usr/bin/python3
# -*- coding: utf-8 -*-

#六  用面向对象,实现一个学生Python成绩管理系统;
    #   学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
    #   实现对学生信息及成绩的增,删,改,查方法;


import os,sys

class Student:
    def __init__(self):
        self.Class=""
        self.Number=""
        self.Name=""
        self.Score=""
    

def search(stulist,Number):
    for item in stulist:
        if item.Number==Number:
            return True
def Add(stulist,stu):
        if(search(stulist,stu.Number)==True):
            print("学号已存在")
            return False
        stulist.append(stu)
        with open("Student6.txt",'a') as f:
            f.write(stu.Class+" ")
            f.write(stu.Number+" ")
            f.write(stu.Name+" ")
            f.write(stu.Score+"\n")
        print("添加成功")
def Search(stulist,Number):
    count=0
    n=len(stulist)
    for item in stulist:
        if item.Number==Number:
            print("{:12}{:12}{:12}{}".format("班级","学号","姓名","Python成绩"))
            print("{:15}{:15}{:15}{}".format(item.Class,item.Number,item.Name,item.Score))
            break
        count=count+1
    if(count==n):
        print("没有该学生学号！")
def Del(stulist,Number):
    count=0
    n=len(stulist)
    for item in stulist:
        if(item.Number==Number):
            stulist.remove(item)
            print("删除成功!")
            break
        count=count+1
    if(count==n):
        print("没有该学生学号!")
    with open("Student6.txt",'w') as f:
        for stu in stulist:
            f.write(stu.Class+" ")
            f.write(stu.Number+" ")
            f.write(stu.Name+" ")
            f.write(stu.Score+"/n")
def Change(stulist,Number):
    count = 0
    for item in stulist:
        if item.Number==Number:
            stulist.remove(item)
            with open("Student6.txt", "w") as f:
                for stu in stulist:
                    f.write(stu.Class+" ")
                    f.write(stu.Number+" ")
                    f.write(stu.Name+" ")
                    f.write(stu.Score+"/n")
            stu=Student()
            stu.Class=input("请输入班级:")
            stu.Number=input("请输入学号:")
            stu.Name=input("请输入姓名:")
            stu.Score=input("请输入Python成绩:")
            Add(stulist,stu)
def All_information(stulist):
    print("{:12}{:12}{:12}{}".format("班级","学号","姓名","Python成绩"))
    for item in stulist:
        print("{:15}{:15}{:15}{}".format(item.Class,item.Number,item.Name,item.Score))
def Init(stulist):
    print("初始化......")
    if(os.path.exists("Student6.txt")==True):
        with open("Student6.txt",'r') as f:
            for line in f:
                stu = Student()
                line = line.strip("\n")
                s = line.split(" ")
                stu.Class=s[0]
                stu.Number=s[1]
                stu.Name=s[2]
                stu.Score=s[3]
                stulist.append(stu)
    else:
        with open("Student6.txt",'w') as f:
            pass
    print("初始化成功")
    main()
def main():
    while(True):
        print("*" * 50)
        print()
        print("         学生信息管理系统     ")
        print("")
        print("          1:添加学生信息")
        print("          2:查询学生信息")
        print("          3:删除学生信息")
        print("          4:修改学生信息")
        print("          5:显示所有学生信息")
        print("          0:退出系统")
        print(" ")
        print("*" * 50)
        choose=input("请输入要选择操作的序号:")
        if(choose=='1'):
            stu=Student()
            stu.Class=input("请输入班级:")
            stu.Number=input("请输入学号:")
            stu.Name=input("请输入姓名:")
            stu.Score=input("请输入Python成绩:")
            Add(stulist,stu)
        elif(choose=='2'):
            Number=input("请输入学生的学号:")
            Search(stulist,Number)
        elif(choose=='3'):
            Number=input("请输入学生的学号:")
            Del(stulist,Number)
        elif(choose=='4'):
            Number=input("请输入学生的学号:")
            Change(stulist,Number)
        elif(choose=='5'):
            All_information(stulist)
        elif(choose=='0'):
            sys.exit(0)
        else:
            print("输入有误，请重新输入")
            print()
    
    

stulist=[]
Init(stulist)




    

            

