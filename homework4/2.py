#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

#2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；


def count():
    # 转为时间数组s
    list1=["周天","周一","周二","周三","周四","周五","周六"]
    s=input("请输入一个日期(格式为x-y-z)")
    time = datetime.strptime(s,"%Y-%m-%d")
    x=int(time.strftime('%W'))
    print("{}是第{}周，{}".format(s,time.strftime('%W'),list1[int(time.strftime('%w'))]))
    time1=str(time.year)+"-02-17"
    time1 = datetime.strptime(time1, "%Y-%m-%d")
    x1=int(time1.strftime('%W'))
    print("{}是校历第{}周".format(s,x-x1+1))

count()