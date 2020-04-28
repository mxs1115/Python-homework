#!/usr/bin/python
# -*- coding: UTF-8 -*-


#3  多进程练习：
#计算1～100000之间所有素数的个数， 要求如下:
#- 编写函数判断一个数字是否为素数，然后统计素数的个数；
#-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
#-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

import time
from multiprocessing import Process, Queue
from multiprocessing import Pool
import multiprocessing


def isprime(x):
    n=2
    while( n < x ):
        if( x%n == 0 ):
            break
        else:
            n=n+1
            continue   
    if( n == x ):
        return x
    else:
        return 0

def isprime_number(name,q,q1,share_lock):
    while(True):
        if not q1.empty():
            k=int(q1.get(True))
            y=isprime(k)
            #print(y)
            #print('{}:{}'.format(name,y))
        else:
            break
        if(y!=0):
            share_lock.acquire()
            q.put(y)
            share_lock.release()
        #time.sleep(0.001)

def isprime_number0():
    n=0
    for i in range(1,10001):
        x=2
        while( x < i ):
            if( i%x == 0 ):
                break
            else:
                x=x+1
                continue   
        if( x == i ):
            n=n+1
    #time.sleep(0.001)
    print(n)

def isprime_number10():
    q=Queue(10000)
    q1=Queue(10000)
    share_lock = multiprocessing.Manager().Lock()
    for i in range(1,10001):
        q1.put(i)
    p1 = Process(target=isprime_number, args=('1',q,q1,share_lock))
    p2 = Process(target=isprime_number, args=('2',q,q1,share_lock))
    p3 = Process(target=isprime_number, args=('3',q,q1,share_lock))
    p4 = Process(target=isprime_number, args=('4',q,q1,share_lock))
    p5 = Process(target=isprime_number, args=('5',q,q1,share_lock))
    p6 = Process(target=isprime_number, args=('6',q,q1,share_lock))
    p7 = Process(target=isprime_number, args=('7',q,q1,share_lock))
    p8 = Process(target=isprime_number, args=('8',q,q1,share_lock))
    p9 = Process(target=isprime_number, args=('9',q,q1,share_lock))
    p10 = Process(target=isprime_number, args=('10',q,q1,share_lock))
    startime=time.time()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    endtime=time.time()
    print(q.qsize())
    print("10个多进程:",endtime-startime)
    

 
if __name__=='__main__':
    q=Queue(10000)
    q1=Queue(10000)
    share_lock = multiprocessing.Manager().Lock()
    for i in range(1,10001):
        q1.put(i)
    p1 = Process(target=isprime_number, args=('1',q,q1,share_lock))
    p2 = Process(target=isprime_number, args=('2',q,q1,share_lock))
    p3 = Process(target=isprime_number, args=('3',q,q1,share_lock))
    p4 = Process(target=isprime_number, args=('4',q,q1,share_lock))
    startime=time.time()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    endtime=time.time()
    print(q.qsize())
    print("4个多进程:",endtime-startime)

    startime=time.time()
    isprime_number0()
    endtime=time.time()
    print("非多进程:",endtime-startime)

    isprime_number10()


    