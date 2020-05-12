#② 查询所有查询编号小于4或没被删除的学生；

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = """ 
SELECT * FROM students WHERE id < 4 or is_delete = 0 
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