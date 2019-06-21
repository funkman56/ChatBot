# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:43:24 2019

@author: User
"""

import psycopg2               #外部檔名不能取psycopg2 會發生問題


def getProduct(msg="1"):
    
    conn = psycopg2.connect(
                        database = "d10j5v2k8o52ad",
                        user = "iqidhdxsayqefc",
                        password = "651dbbe748aa3c1283216db6ad30c2b849e70678f31622533ceee03d0e9f4b26",
                        host = "ec2-54-225-106-93.compute-1.amazonaws.com",
                        port = "5432"                                               
                        )
                        #資料庫名稱 使用者名稱 密碼 主機位置 使用通道
    cur = conn.cursor()

    if msg == "1" :
        cur.execute("select * from product")
    else :
        cur.execute("select name,prices from product where name like '%{}%'".format(msg))
        
    rows = cur.fetchall()
    content = ""   
    for data in rows :
        content = content + str(data[1]) +'\n'


    conn.close()
    return content