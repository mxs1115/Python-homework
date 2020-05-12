#⑥ 查询未删除男生信息，按年龄降序

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = """ 
SELECT * FROM students WHERE gender = '男' and is_delete = 0 order by age desc
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