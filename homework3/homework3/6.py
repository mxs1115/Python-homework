#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from collections import Counter

#6  在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
   # 比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......)

def File_similarity(f1,f2):
   with open(f1,"r") as f11:
      s1=f11.read()
      s1=s1.replace(',',' ')
      s1=s1.replace('.',' ')
      s1=s1.replace('  ',' ')
      s1=s1.replace('!',' ')
      s1=s1.replace('\n',' ')
      s1=s1.split(' ')
      s1=Counter(s1)
   with open("f1_word_frequency_count.txt","w") as f:
      d1 = sorted(s1.items(), key=lambda x: x[1], reverse=True)
      for i in d1:
         f.write("{}:{}\n".format(i[0],i[1]))
   with open(f2,"r") as f22:
      s2=f22.read()
      s2=s2.replace(',',' ')
      s2=s2.replace('.',' ')
      s2=s2.replace('  ',' ')
      s2=s2.replace('!',' ')
      s2=s2.replace('\n',' ')
      s2=s2.split(' ')
      s2=Counter(s2)
   with open("f2_word_frequency_count.txt","w") as f:
      d2 = sorted(s2.items(), key=lambda x: x[1], reverse=True)
      for i in d2:
         f.write("{}:{}\n".format(i[0],i[1]))
   
   d1=d1[0:11]
   d11=[]
   for i in d1:
      d11.append(i[0])
   d2=d2[0:11]
   d22=[]
   for i in d2:
      d22.append(i[0])
   c=[x for x in d11 if x in d22]
   l=len(c)
   Similarity_degree=l/10
   print("两篇文章相似度为{}%".format(Similarity_degree*100))


File_similarity("f1.txt","f2.txt")
