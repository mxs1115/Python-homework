#!/usr/bin/python
# -*- coding: UTF-8 -*-

#4 多进程通讯：
  #编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；

from multiprocessing import Process, Queue
import time, random
import multiprocessing



# 写数据进程执行的代码:
def write(q):
  while(True):
    #print('Process to write: %s' % os.getpid())
    value=input("请输入信息:")
    q.put(value)
    time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
  while(True):
    #print('Process to read: %s' % os.getpid())
    value = q.get(True)
    print('接收消息:%s' % value)
    time.sleep(random.random())

if __name__=='__main__':
  q = Queue()
  #while(True):
  pr = Process(target=read, args=(q,))
  pr.start()
  write(q)
  time.sleep(2)
  
  #pr.join()