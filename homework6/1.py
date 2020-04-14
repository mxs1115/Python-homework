#!/usr/bin/python3
# -*- coding: utf-8 -*-

#一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       #实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;

class Dog:
    list1=[{"颜色":"白色","数量":15,"价格":150},{"颜色":"黑色","数量":20,"价格":300},{"颜色":"黄色","数量":50,"价格":100}]
    def shop(self):
        for i in self.list1:
            for k,v in i.items():
                print(k,":",v,end='  ')
            print()
        x=input("请输入要购买的颜色:")
        y=int(input("请输入要购买的数量:"))
        for i in self.list1:
            if(x==i["颜色"]):
                if(y<=i["数量"]):
                    i["数量"]=i["数量"]-y
                    m=i["价格"]*y
                    print("购买完成,一共{}元".format(m))
                    break
                else:
                    print("库存量不足")
        else:
            print("未找到颜色为{}的狗".format(x))
    def print1(self):
        print("剩余库存情况：")
        for i in self.list1:
            for k,v in i.items():
                print(k,":",v,end='  ')
            print()

x=Dog()
x.shop()
x.shop()
x.print1()
