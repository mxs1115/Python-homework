#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import datetime
from collections import deque

# 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
   # 提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)


list1=[random.randint(1,30) for i in range(10)]

starttime1 = datetime.datetime.now()
list1.insert(0, 'x')
list1.append('y')
endtime1 = datetime.datetime.now()
t1=(endtime1 - starttime1).total_seconds()

starttime2 = datetime.datetime.now()
q=deque(list1)
q.append('x')
q.appendleft('y')
list1=list(q)
endtime2 = datetime.datetime.now()
t2=(endtime2 - starttime2).total_seconds()

print("实现尾部插入和头部插入列表自带函数运行时间与deque来实现运行时间的差值为:{}".format(t1-t2))
