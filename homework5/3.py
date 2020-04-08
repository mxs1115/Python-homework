#!/usr/bin/python3
# -*- coding: utf-8 -*-


#3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

def outer(f):
    def inner(*args,**kwargs):
        username=input('请输入账号:')
        password=input("请输入密码:")
        if username=='123' and password=='123':
            ret=f(*args,**kwargs)
            return ret
        else:
            print("登陆失败")
    return inner

@outer
def fun1():
    print("运行成功!")

@outer
def fun2(a,b):
    x=a+b
    return x

fun1()
print(fun2(3,4))
