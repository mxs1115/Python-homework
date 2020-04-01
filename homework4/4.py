#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import hashlib

#4  (继续上面的练习) 模拟用户登录:
     #5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);

with open("student1.txt",'r') as f:
            list1=[]
            while True:
                s=f.readline()
                if not s:
                    break
                #s=s.rstrip()
                s=s.split()
                list(s)
                list1.append(s)
k=0
name=input("请输入姓名：")
m=len(list1)
for i in list1:
    if(i[0]==name):
        number=input("请输入账号：")
        if(i[1]==number):
            password=input("请输入密码：")
            password1=hashlib.md5()
            password1.update(password.encode('utf-8'))
            if(password1.hexdigest()==i[2]):
                print("您登陆成功")
                break
            else:
                print("您登陆失败，密码错误")
                break
        else:
            print("账号输入有误")
            break
    else:
        k+=1
        if(k<=m):
            continue
        else:
            print("姓名输入有误")
            break
    