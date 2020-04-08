#!/usr/bin/python3
# -*- coding: utf-8 -*-


#4  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
 #    三个目标函数分别为：
 #   A 打印输出20000之内的素数；
 #    B 计算整数2-10000之间的素数的个数；
 #    C 计算整数2-M之间的素数的个数；
 # 可以观看给的视频材料，仿照示例来做；

import time

def outerA(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print("运行时间为%s"%(end_time - start_time))
    return inner

def outerB(func):
    def inner(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print("运行时间为%s"%(end_time - start_time))
    return inner

def outerC(func):
    def inner():
        start_time = time.time()
        r=func()
        end_time = time.time()
        return r
        print("运行时间为%s"%(end_time - start_time))
    return inner

@outerA
def Afun():
    list1=[]
    for i in range(2,20000):
        for k in range(2,i):
            if (i%k==0):
                break
        else:
            list1.append(i)
    print("20000之内的素数有:")
    print(list1)

@outerB
def Bfun(k,w):
    list1=[]
    number=0
    if(k<2):
        k=2
    for i in range(k,w+1):
        for k in range(2,i):
            if (i%k==0):
                break
        else:
            list1.append(i)
            number=number+1
    print("{}到{}之间的素数个数为{}个".format(k,w,number))


@outerC
def Cfun():
    x=int(input("请输入一个大于2数:"))
    list1=[]
    number=0
    for i in range(2,x):
        for k in range(2,i):
            if (i%k==0):
                break
        else:
            list1.append(i)
            number=number+1
    return "2到{}之间的素数有{}个".format(x,number)

Afun()
Bfun(2,10000)
print(Cfun())

                