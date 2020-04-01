#!/usr/bin/python3
# -*- coding: utf-8 -*-

import  os
import hashlib


#3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
       # Tom   admin   XXXXX
       # Jack   root      XXXXX   

with open("student1.txt",'w') as f:
    for i in range(5):
        name=input("请输入第{}个同学的姓名：".format(i+1))
        number=input("请输入第{}个同学的账号：".format(i+1))
        password=input("请输入第{}个同学的密码：".format(i+1))
        password1=hashlib.md5()
        password1.update(password.encode('utf-8'))
        f.write(name+"    "+number+"   "+password1.hexdigest()+'\n')
