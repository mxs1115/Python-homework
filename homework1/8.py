#!/usr/bin/python3
# -*- coding: utf-8 -*-

#设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
a={1201:["李华",3,5000],1202:["李明",5,8000],1203:["小明",2,3500],1204:["张强",6,8500],1205:["张三",5,8000],1206:["李四",7,9500],1207:["王二",3,4500],1208:["小红",1,3000],1209:["小张",6,5500],1210:["小白",6,8500]}
b=sorted(a.items(),key=lambda x: x[1][2],reverse=True)
for i in range(10):
    print(b[i])