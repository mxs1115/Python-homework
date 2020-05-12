# ① 查询所有男生的姓名，年龄，所在班级名称；

# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = """ 
SELECT students.name,students.age,classes.name FROM students left join classes on students.cls_id=classes.id 
where students.gender = '男'
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