#!/usr/bin/python
# -*- coding: UTF-8 -*-

#2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   #请查资料，Python的 requests库，如何判断一个网址可以访问；


import threading
import requests
import time

number=0

def geturl():
    list_url=[]
    with open(r'homework8\url_data.txt','r') as f:
        while(True):
            s=f.readline()
            if not s:
                break
            s=s.replace('\n','')
            s=s.split(';')
            list_url=list_url+s
    return list_url



def getHtml(url): 
    try:    
        r = requests.get(url,timeout=3)   
        code=r.status_code
        if(code==200):
            return url+"访问正常"
        else:
            return url+"存在异常"
    except:
         return "产生异常"

def url_visit(n,list_url,name):
    global number
    while(True):
        if(number<n):
            time.sleep(0.1)
            print("{}号线程:".format(name),getHtml(list_url[number]))
            number=number+1
        else:
            break


list_url=geturl()
n=len(list_url)

if __name__ == '__main__':
    t1 = threading.Thread(target=url_visit,args=(n,list_url,'1'))
    t2 = threading.Thread(target=url_visit,args=(n,list_url,'2'))
    t3 = threading.Thread(target=url_visit,args=(n,list_url,'3'))
    t4 = threading.Thread(target=url_visit,args=(n,list_url,'4'))
    t5 = threading.Thread(target=url_visit,args=(n,list_url,'5'))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()