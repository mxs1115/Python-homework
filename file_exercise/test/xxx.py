##!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

#同级目录下的子目录里面打开

os.chdir("test")
with open(r"b\ba.txt","r") as file:
    print(file.read())


