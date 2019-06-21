# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:47:14 2019

@author: User
"""

import requests
import json

def getPM25(area) :
    url ="http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
    response = json.loads(requests.get(url,verify = False).text)
    site = []
    pm25 = []
    aqi = []
    status = []
    time = []
    
    for stat in response :
        site.append(stat["SiteName"])
        pm25.append(stat["PM2.5"])
        aqi.append(stat["AQI"])
        status.append(stat["Status"])
        time.append(stat["PublishTime"])
        
    info = list(zip(pm25,aqi,status,time))
    data = dict(zip(site,info))
    
    score = data.get(area,"無此地區資料")
    
    if score != "無此地區資料" :
        
        if score[2] == "設備維護" :
            score = "地區 : "+area+"\n"+ "PM2.5 : "+score[0]+"\n" + "AQI : "+"設備維護中"+"\n" +"觀測時間 : "+score[3]
                     
        else :
            value = int(score[1])
            if value <= 50 :
                score = "地區 : "+area+"\n"+ "PM2.5 : "+score[0]+"\n" + "AQI : "+score[1]+" ("+"綠燈"+")"+"\n" +"空氣品質 : "+score[2]+"\n" +"觀測時間 : "+score[3] 
            elif value <=100 :
                score = "地區 : "+area+"\n"+ "PM2.5 : "+score[0]+"\n" + "AQI : "+score[1]+" ("+"黃燈"+")"+"\n" +"空氣品質 : "+score[2]+"\n" +"觀測時間 : "+score[3]
            elif value <= 150 :
                score = "地區 : "+area+"\n"+ "PM2.5 : "+score[0]+"\n" + "AQI : "+score[1]+" ("+"橘燈"+")"+"\n" +"空氣品質 : "+score[2]+"\n" +"觀測時間 : "+score[3]
            elif value <= 200 :
                score = "地區 : "+area+"\n"+ "PM2.5 : "+score[0]+"\n" + "AQI : "+score[1]+" ("+"紅燈"+")"+"\n" +"空氣品質 : "+score[2]+"\n" +"觀測時間 : "+score[3]
            elif value <= 300 :
                score = "地區 : "+area+"\n"+ "PM2.5 : "+score[0]+"\n" + "AQI : "+score[1]+" ("+"紫燈"+")"+"\n" +"空氣品質 : "+score[2]+"\n" +"觀測時間 : "+score[3]
            else :
                score = "地區 : "+area+"\n"+ "PM2.5 : "+score[0]+"\n" + "AQI : "+score[1]+" ("+"嚴重危害"+")"+"\n" +"空氣品質 : "+score[2]+"\n" +"觀測時間 : "+score[3]
       
            
    return score



