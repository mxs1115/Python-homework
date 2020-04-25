#!/usr/bin/python
# -*- coding: UTF-8 -*-


#4 爬取这个网址上http://www.python3.vip/doc/prac/python/0001/，所有的Python练习题题目和答案；保存到txt文件中（只保留文字）；

from bs4 import BeautifulSoup
import requests
import re,os

url="http://www.python3.vip/doc/prac/python/0001/"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'}
r = requests.get(url,headers=headers).content.decode('utf-8')
soup = BeautifulSoup(r,'html.parser')
re_a = soup.find(id='main').ul.find_all('a')
list = []
for i in re_a:
   list.append(i.attrs['href'])
print(list)


data = []
os.chdir(r"homework7\4")
for x in list:
	test = requests.get(x, headers=headers).content.decode('utf-8')
	#print(x)
	
	soup_test = BeautifulSoup(test, 'html.parser')
	title = soup_test.find(class_="page__title").text
	#print(soup_test.find(class_="page__title").text)
	tm = soup_test.find(class_="content").text
	with open('text-py.txt','a+',encoding='utf-8') as f:
		f.write(title+'\n')
		f.write(tm+'\n')
		f.write('*'*50+'\n')
		f.write('\n')
    