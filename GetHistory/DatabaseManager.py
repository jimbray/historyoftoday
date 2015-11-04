#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jimbray
@contact: jimbray16@gmail.com
@site: 
@software: PyCharm
@file: DatabaseManager.py
@time: 2015/11/4 16:36
"""

import sqlite3

def insertHistoryList(history_list):
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('database.db')
    #将数据库编码修改为
    conn.text_factory = str

    #创建一个游标
    cursor = conn.cursor()

    #执行SQL，创建history表
    create_history_table = '''CREATE TABLE IF NOT EXISTS history (title TEXT, url TEXT, content TEXT)'''
    conn.execute(create_history_table)

    #执行语句，插入数据
    for history in history_list:
        # conn.execute('INSERT INTO history VALUES (NULL, ?, ?, ?)', *row)
        # query = 'INSERT INTO history (title, url, content) VALUES (' + history['title'] + ',' + history['url'] + ',' + history['content'] + ")"
        values = history['title']+","+history['url']+","+history['content']

        conn.execute("INSERT INTO history (title, url, content) VALUES (?, ?, ?)", (history['title'], history['url'], history['content'], ))

    #通过日rowcount获得插入的行数(貌似无效)
    row_count = cursor.rowcount
    print row_count
    #关闭游标
    cursor.close()

    #提交事物
    conn.commit()

    #关闭连接
    conn.close()






if __name__ == '__main__':
    insertHistoryList([])