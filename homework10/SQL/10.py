# ⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
# | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
# | 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
# | 中性   | 金星                                                       |
# | 保密   | 凤姐                                                       |


# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = """ 
SELECT gender,group_concat(name separator ',') from students  group by gender
"""

try:
   cursor.execute(sql)
   myresult = cursor.fetchall()
   for x in myresult:
      print("|", "%-20s%20s%-40s" % (x[0], "|", x[1]), '|')
except Exception as e:
    print("发生异常", e)
finally:
# 关闭数据库连接
   db.close()

