#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；

import logging,os

def qi(fun):
    def w(*args):
        x=fun(*args)
        logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.INFO)
        logging.info('进行了一次加法运算')
        return x
    return w

@qi
def jia(a,b):
    x=a+b
    return x 

print(jia(1,2))