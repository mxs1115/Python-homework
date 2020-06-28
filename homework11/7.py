#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
from sqlalchemy import Column, create_engine, Integer, VARCHAR, and_
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


url2 = 'https://search.51job.com/list/000000,000000,0124,00,9,99,%2B,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
r = requests.get(url2, headers=headers).content
soup = BeautifulSoup(r, 'html.parser')
re_a1 = soup.find(type="hidden", id="hidTotalPage")
page = int(re_a1.attrs['value'])

zname = []
gname = []
area = []
money = []
time = []

for i in range(page):
    re_a2 = soup.find(class_="dw_table").findAll(class_="el")
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
            if k.string == '工作地点':
                continue
            else:
                area.append(k.string)

    for i in re_a2:
        for k in i(class_='t4'):
            if k.string == '薪资':
                continue
            else:
                money.append(k.string)

    for i in re_a2:
        for k in i(class_='t5'):
            if k.string == '发布时间':
                continue
            else:
                time.append(k.string)

    re_a3 = soup.findAll('li', class_='bk')
    for i in re_a3:
        for k in i('a'):
            nexturl = k.attrs['href']
    r = requests.get(nexturl, headers=headers).content
    soup = BeautifulSoup(r, 'html.parser')
# print(len(zname))
# print(len(gname))
# print(len(area))
# print(len(money))
# print(len(time))
Base = declarative_base()


class Python_engineer_51job(Base):
    # 表的名字:
    __tablename__ = 'python_engineer_51job'

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
    session = DBSession()
    for i in range(count):
        b = session.query(Python_engineer_51job)\
            .filter(and_(Python_engineer_51job.Position == zname[i], Python_engineer_51job.Company == gname[i], Python_engineer_51job.Area == area[i], Python_engineer_51job.Money == money[i], Python_engineer_51job.Time == time[i])).all()
        # (避免爬取更新造成数据库同一招聘信息多次重复加入)
        if not b:
            new_job = Python_engineer_51job(ID='0', Position=zname[i], Company=gname[i], Area=area[i], Money=money[i], Time=time[i])
            session.add(new_job)
            session.commit()
            # print("插入数据成功！")
        # else:
        #     print(i)
        #     for row in b:
        #         print(row.ID, row.Position, row.Company, row.Area, row.Money, row.Time)
except Exception as e:
    print("发生异常", e)
finally:
    # 关闭数据库连接
    session.close()


try:
    money_beijing = []
    session = DBSession()
    b = session.query(Python_engineer_51job).filter(Python_engineer_51job.Area.like('%北京%')).all()
    for row in b:
        money_beijing.append(str(row.Money))
except Exception as e:
    print("发生异常", e)
finally:
    # 关闭数据库连接
    session.close()

# print(money_beijing)
# print(len(money_beijing))
count = len(money_beijing)
m = 0
k = 0
for i in range(count):
    if re.match('.*万/月', money_beijing[i]):
        ma = re.findall(r'\d+\.\d+|\d+', money_beijing[i])
        max = float(ma[1])
        min = float(ma[0])
        m = (max+min)/2 + m
    elif re.match('.*千/月', money_beijing[i]):
        mi = re.findall(r'\d+\.\d+|\d+', money_beijing[i])
        max = float(mi[1])*0.1
        min = float(mi[0])*0.1
        m = (max+min)/2 + m
    elif re.match('.*元/天', money_beijing[i]):
        mi = re.findall(r'\d+\.\d+|\d+', money_beijing[i])
        m = float(mi[0]) * 0.0001*30 + m
    elif re.match('.*万/年', money_beijing[i]):
        mi = re.findall(r'\d+\.\d+|\d+', money_beijing[i])
        max = float(mi[1])/12
        min = float(mi[0])/12
        m = (max+min)/2 + m
    elif re.match('None', money_beijing[i]):
        k = k+1

count = count - k
average = m/count
print("51job网站上，北京地区2020年发布的Python开发工程师的职位的平均薪酬为{:.2f}万元/月".format(average))
