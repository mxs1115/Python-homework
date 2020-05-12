# ⑨ 分别统计性别为男/女的人年龄平均值

# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = """ 
SELECT gender,round(avg(age),2) from students where gender='男' or gender='女'  group by gender
"""

try:
   cursor.execute(sql)
   myresult = cursor.fetchall()
   for x in myresult:
      print(x)
except Exception as e:
    print("发生异常", e)
finally:
# 关闭数据库连接
   db.close()