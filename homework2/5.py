#!/usr/bin/python3
# -*- coding: utf-8 -*-

#写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;

def measure1(dict1):
    for i,m in dict1.items():
        if len(m) > 2:
            dict1[i] = m[0:2]
    return dict1
dict2 = {'1201':'mxsmxs','number':'12123','ssss':[111,123,1234]}
dict3=measure1(dict2)
print(dict3)