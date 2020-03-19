#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
#练习:  在window平台下练习os.path 相关方法的使用! 观察输出结果;

import os
 
#os.getcwd()
pwd = os.path.abspath('.')
print( os.path.basename(pwd) )   # 返回文件名
print( os.path.dirname(pwd) )    # 返回目录路径
print( os.path.split(pwd) )      # 分割文件名与路径
print( os.path.join(pwd) )  # 将目录和文件名合成一个路径
