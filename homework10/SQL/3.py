#③ 查询姓黄并且“名”是一个字的学生；

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = """ 
SELECT * FROM students WHERE name like '黄_'
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