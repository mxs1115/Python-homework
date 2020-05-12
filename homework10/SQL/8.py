#⑧  查询学生的平均年龄

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = """ 
SELECT round(avg(age),2) FROM students 
"""

try:
   cursor.execute(sql)
   avg1=cursor.fetchone()
   print("学生的平均年龄为:{}".format(avg1[0]))
except Exception as e:
    print("发生异常", e)
finally:
# 关闭数据库连接
   db.close()