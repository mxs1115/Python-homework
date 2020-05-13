# 3  对2中的表结构，用SQLAchemy模块来实现同样的操作；

# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

from datetime import datetime
import datetime
import sys
from sqlalchemy import Column, create_engine, Integer, DateTime, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Message_pad(Base):
    # 表的名字:
    __tablename__ = 'message_pad'

    # 表的结构:
    ID = Column(Integer, primary_key=True)
    content = Column(VARCHAR(255))
    name = Column(VARCHAR(255))
    time = Column(DateTime)
    is_delete = Column(Integer)


engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/student')
DBSession = sessionmaker(bind=engine)


def add():
    try:
        session = DBSession()
        content = input("请输入留言内容:")
        name = input("请输入姓名:")
        time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        new_message = Message_pad(ID='0', content=content, name=name, time=time, is_delete='0')
        session.add(new_message)
        session.commit()
        print("插入数据成功！")
    except Exception as e:
        print("发生异常", e)
    finally:
        # 关闭数据库连接
        session.close()


def delete():
    try:
        session = DBSession()
        delete_id = int(input("请输入要删除的id号:"))
        session.query(Message_pad).filter(Message_pad.ID == delete_id).update({'is_delete': '1'})
        session.commit()
        print("数据删除成功！")
    except Exception as e:
        print("发生异常", e)
    finally:
        # 关闭数据库连接
        session.close()


def update():
    try:
        session = DBSession()
        update_id = input("请输入要修改的id号:")
        update_name = input("请输入修改后的姓名:")
        update_content = input("请输入修改后的留言内容:")
        time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        session.query(Message_pad).filter(Message_pad.ID == update_id).update({'name': update_name, 'content': update_content, 'time': time})
        session.commit()
        print("数据修改成功！")
    except Exception as e:
        print("发生异常", e)
    finally:
        # 关闭数据库连接
        session.close()


def select():
    try:
        session = DBSession()
        select_id = input("请输入要要查询的id号(输入0查询所有留言信息):")
        if select_id == '0':
            a = session.query(Message_pad).all()
            if not a:
                print("数据库为空")
            else:
                for row in a:
                    print(row.ID, row.content, row.name, row.time, row.is_delete)
        else:
            b = session.query(Message_pad).filter(Message_pad.ID == select_id).all()
            if not b:
                print("查询ID不存在")
            else:
                for row in b:
                    print(row.ID, row.content, row.name, row.time, row.is_delete)
    except Exception as e:
        print("发生异常", e)
    finally:
        # 关闭数据库连接
        session.close()


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
