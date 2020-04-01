#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from collections import Counter

# 8 京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

def create_ipfile():
    with open("ip.txt",'w') as f:
        for i in range(1200):
            f.write("172.25.254."+str(random.randint(1,255))+'\n')

def statistics():
    ip_count={}
    with open("ip.txt",'r') as f:
        s1=f.read()
        s1=s1.split('\n')
        s1=Counter(s1)
        d1=sorted(s1.items(), key=lambda x: x[1], reverse=True)[:10]
        for i in d1:
            print(i)

create_ipfile()
statistics()