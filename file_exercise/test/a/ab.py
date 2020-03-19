#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

#上一级文件目录中的其他文件夹中打开
os.chdir(r"test/a")
with open("../b/ba.txt","r") as file:
    print(file.read())