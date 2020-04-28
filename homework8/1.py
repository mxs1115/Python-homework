#!/usr/bin/python
# -*- coding: UTF-8 -*-

#1  有100个同学的分数：数据请用随机函数生成；
#     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#    B 利用线程池来实现；

import random
import threading,time
from multiprocessing import Pool

number=0

def pscore(score,name):
    global number
    for i in range(20):
        time.sleep(0.1)
        print("{}号线程:".format(name),score[number],end="  ")
        if((number+1)%5==0):
            print()
        number=number+1



score=[random.randint(0,100)  for i in range(100) ]

if __name__ == '__main__':
    print('*'*50)
    print("A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息")
    t1 = threading.Thread(target=pscore,args=(score,'1'))
    t2 = threading.Thread(target=pscore,args=(score,'2'))
    t3 = threading.Thread(target=pscore,args=(score,'3'))
    t4 = threading.Thread(target=pscore,args=(score,'4'))
    t5 = threading.Thread(target=pscore,args=(score,'5'))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    time.sleep(3)
    print()
    print('*'*50)
    print("B 利用线程池来实现")

    po=Pool(3)
    for i in range(5):
        po.apply_async(pscore,(score,i+1))
    print("----start----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print()
    print("-----end-----")
    




