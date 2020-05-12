# 2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
# 使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻;

# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

import datetime
import pymysql
import sys


def add():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "student")
    cursor = db.cursor()
    content = input("请输入留言内容:")
    name = input("请输入姓名:")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    sql = """INSERT INTO message_pad(content,
          name,time,is_delete)
         VALUES (%s,%s,%s,'0')"""
    try:
        # 执行sql语句
        cursor.execute(sql, (content, name, time))
        # 提交到数据库执行
        db.commit()
        print("插入数据成功！")
    except Exception as e:
        print("发生异常", e)
    finally:
        # 关闭数据库连接
        db.close()


def delete():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "student")
    cursor = db.cursor()
    delete_id = int(input("请输入要删除的id号:"))
    sql = """UPDATE message_pad SET is_delete = "1" WHERE ID = "%d" """ % delete_id
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("数据删除成功！")
    except Exception as e:
        print("发生异常", e)
    finally:
        # 关闭数据库连接
        db.close()


def update():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "student")
    cursor = db.cursor()
    update_id = input("请输入要修改的id号:")
    update_name = input("请输入修改后的姓名:")
    update_content = input("请输入修改后的留言内容:")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    sql = """UPDATE message_pad SET content = "%s", name = "%s", time = "%s" 
    WHERE ID = "%s"  """ % (update_content, update_name, time, update_id)
    sql1 = """select * from message_pad WHERE ID = "%s" and is_delete = '0' """ % update_id
    try:
        # 执行sql语句
        cursor.execute(sql1)
        myresult = cursor.fetchone()
        # print(myresult)
        if myresult is None:
            print("该记录已被删除或ID错误")
        else:
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print("数据修改成功！")
    except Exception as e:
        print("发生异常", e)
    finally:
        # 关闭数据库连接
        db.close()


def select():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "student")
    cursor = db.cursor()
    select_id = input("请输入要要查询的id号(输入0查询所有留言信息):")
    if select_id == '0':
        sql = """SELECT * FROM message_pad """
    else:
        sql = """SELECT * FROM message_pad WHERE ID = "%s" """ % select_id
    try:
        cursor.execute(sql)
        myresult = cursor.fetchall()
        if myresult is ():
            print("查询id不存在")
        for x in myresult:
            print(x)
    except Exception as e:
        print("发生异常", e)
    finally:
        # 关闭数据库连接
        db.close()


def main():
    while True:
        print("留言本数据库".center(50, '*'))
        print("1:增加留言")
        print("2:删除留言")
        print("3:修改留言")
        print("4:查询留言")
        print("0:退出程序")
        n = int(input("请选择功能:"))
        if n == 1:
            add()
        elif n == 2:
            delete()
        elif n == 3:
            update()
        elif n == 4:
            select()
        elif n == 0:
            sys.exit(0)
        else:
            print("输入有误请重新输入")


if __name__ == "__main__":
    main()
