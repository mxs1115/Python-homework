#⑦  查询女生的总数

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = """ 
SELECT count(*) FROM students WHERE gender ="女" 
"""

try:
   cursor.execute(sql)
   number = cursor.fetchone()
   print("女生总人数:{}".format(number[0]))
except Exception as e:
    print("发生异常", e)
finally:
# 关闭数据库连接
   db.close()