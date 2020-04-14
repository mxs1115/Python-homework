#!/usr/bin/python3
# -*- coding: utf-8 -*-


#三、定义一个字典类：dictclass。完成下面的功能：
#dict = dictclass({你需要操作的字典对象})
#1 删除某个key
#del_dict(key)
#2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
#get_dict(key)
#3 返回键组成的列表：返回类型;(list)
#get_key()
#4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
#update_dict({要合并的字典})

class dictclass():
    def __init__(self,d):
        self.dict1=d
    def del_dict(self,key):
        del self.dict1[key]
    def get_dict(self,key):
        for k in self.dict1.keys():
            if(k==key):
                return self.dict1[key]
        else:
            return "not found"
    def get_key(self):
        list1=[]
        for k in self.dict1.keys():
            list1.append(k)
        return list1
    def update_dict(self,d2):
        self.dict1.update(d2)
        list1=[]
        for v in self.dict1.values():
            list1.append(v)
        return list1

dict=dictclass({"A":1,"B":2,"C":3,"D":4,"李明":"学生"})
dict.del_dict("李明")
print(dict.get_dict("李明"))
print(dict.get_dict("B"))
print(dict.get_key())
print(dict.update_dict({"E":5,"F":6}))
