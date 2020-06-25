#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
from sqlalchemy import Column, create_engine, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 7 在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区改职位的平均薪酬；


# url = 'https://www.51job.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3765.400 QQBrowser/10.6.4153.400'}
#
# r = requests.get(url, headers=headers).content
# soup = BeautifulSoup(r, 'html.parser')
# re_a = soup.find(id='topIndex').find(href=re.compile('search'))
#
# # print(re_a.attrs['href'])
#
# url1 = re_a.attrs['href']
# r = requests.get(url1, headers=headers).content
# soup = BeautifulSoup(r, 'html.parser')
# re_a1 = soup.find(class_='dw_choice').find(class_="in").find('a')
# #print(re_a1.attrs['href'])


url2 = 'https://search.51job.com/list/010000,000000,0124,01,9,99,%2B,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=#search'
r = requests.get(url2, headers=headers).content
soup = BeautifulSoup(r, 'html.parser')
re_a2 = soup.find(class_="dw_table").findAll(class_="el")
zname = []
gname = []
area = []
money = []
time = []

for i in re_a2:
    for k in i('p'):
        for m in k('span'):
            for l in m('a'):
                zname.append(l.attrs['title'])

for i in re_a2:
    for k in i(class_='t2'):
        for m in k('a'):
            gname.append(m.attrs['title'])

for i in re_a2:
    for k in i(class_='t3'):
        area.append(k.string)
area.pop(0)

for i in re_a2:
    for k in i(class_='t4'):
        money.append(k.string)
money.pop(0)

for i in re_a2:
    for k in i(class_='t5'):
        time.append(k.string)
time.pop(0)

Base = declarative_base()


class Python_engineer_beijing(Base):
    # 表的名字:
    __tablename__ = 'python_engineer_beijing'

    # 表的结构:
    ID = Column(Integer, primary_key=True)
    Position = Column(VARCHAR(255))
    Company = Column(VARCHAR(255))
    Area = Column(VARCHAR(255))
    Money = Column(VARCHAR(255))
    Time = Column(VARCHAR(255))


engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/python-engineer')
DBSession = sessionmaker(bind=engine)

try:
    count = len(zname)
    for i in range(count):
        session = DBSession()
        b = session.query(Python_engineer_beijing)\
            .filter(Python_engineer_beijing.Position == zname[i], Python_engineer_beijing.Company == gname[i], Python_engineer_beijing.Area == area[i], Python_engineer_beijing.Money == money[i]).all()
        if not b:
            new_job = Python_engineer_beijing(ID='0', Position=zname[i], Company=gname[i], Area=area[i], Money=money[i], Time=time[i])
            session.add(new_job)
            session.commit()
            print("插入数据成功！")
except Exception as e:
    print("发生异常", e)
finally:
    # 关闭数据库连接
    session.close()

count = len(money)
max = 0
min = 0
for i in range(count):
    if re.match('.*万', money[i]):
        ma = re.findall(r'\d+\.\d+|\d+', money[i])
        max = max+float(ma[1])
        min = min+float(ma[0])
    else:
        mi = re.findall(r'\d+\.\d+|\d+', money[i])
        max = max+float(mi[1])*0.1
        min = min+float(mi[0])*0.1


max = max/count
min = min/count
print("51job网站上，北京地区2020年发布的Python开发工程师的职位的平均薪酬为{:.2f}--{:.2f}万元".format(min, max))
