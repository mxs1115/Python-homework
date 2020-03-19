#!/usr/bin/python
# -*- coding: UTF-8 -*-

#同级文件夹里面打开
#练习:   一个文件内容的如下,请读取文件的内容, 并输出;
           # 姓名      学号      分数
           # 张三      101         78
           # 李四      102         87
           # 王五       103        83

import os
os.chdir(r"test\a")
print("当前工作路径：",os.getcwd())
with open(r"aaa.txt", "r") as file:
     print(file.read())

