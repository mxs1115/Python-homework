#!/usr/bin/python
# -*- coding: UTF-8 -*-

#练习:  读取文件里面的内容(包含中文), 进行打印输出显示;
#  注意:  请设置文件的不同编码格式进行观察;  另外,文件内容中包含中文字符;

import os
import sys


with open(r"test\b\baa.txt", "r",encoding='utf8') as file:
     print("utf8编码:")
     print(file.read())

print()

with open(r"test\b\ba.txt", "r",encoding='gbk') as file:
     print("gbk编码:")
     print(file.read())
