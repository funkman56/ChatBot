# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:31:24 2019

@author: User
"""

'''
line chat bot 資料庫查詢
'''

import psycopg2               #外部檔名不能取psycopg2 會發生問題
conn = psycopg2.connect(
                        database = "d10j5v2k8o52ad",
                        user = "iqidhdxsayqefc",
                        password = "651dbbe748aa3c1283216db6ad30c2b849e70678f31622533ceee03d0e9f4b26",
                        host = "ec2-54-225-106-93.compute-1.amazonaws.com",
                        port = "5432"                                               
                        )
                        #資料庫名稱 使用者名稱 密碼 主機位置 使用通道
cur = conn.cursor()

cur.execute("select * from product")
rows = cur.fetchall()

for data in rows :
    print(data[1])
    print(data[2])


conn.close()