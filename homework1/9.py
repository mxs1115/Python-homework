#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import sys

#设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；

print("*****猜数字游戏*****")
x=random.randint(1,21)
i=0
n=int(input("请输入最多猜的次数"))
while(i<n):
    a=int(input("请输入一个1--20之间的整数"))
    if(a==x):
        print("恭喜你猜对啦！")
        sys.exit(0)
    else:
       i=i+1
       if(i<n):
           print("没有猜对，再试一次")
print("游戏结束，猜数失败")
sys.exit(0)