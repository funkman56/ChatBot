from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('wFGkZIP5odabH5KM07U/N3qd5PF6vMepJTSPaw3+b4Lrqje9mqf0AB9abhfMahICbAvpUgevegxa/GT1KxndEepoHWzvg9o26VjpiARwoDf8NLcm9BQPndv098s4/34WutIraPvqdYLW6NpPxZBv/AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('d92d0b39551e6ae90cbcc1b8cad1e83f')


def GetRubbish():                  #新北市垃圾車資訊
    url = "https://data.ntpc.gov.tw/od/data/api/28AB4122-60E1-4065-98E5-ABCCB69AACA6?$format=json"
    response = json.loads(requests.get(url).text)
    content = ""
    for data in response :
        content += data["car"] + "-" + data["location"] + "\n"
    
    return content

def GetTextkey(text):             #關鍵字查詢       
    content = {"中興" : "在台中的一所大學",
               "空汙" : "請輸入空氣品質查詢"
               }
    return content.get(text,"我不懂你在說甚麼耶 ヾ(´・ω・｀)ノ")
    

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


glasses = 0
air = 0

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
           
    msg = event.message.text
    
    global glasses
    global air
    
    status = 1                           #區別送圖片和送文字    
    
    if "垃圾車" in msg :
        
        txt = GetRubbish()
        
    elif "Tiffany" in msg :
                         
        txt = "她在這\nhttps://tinyurl.com/yxhyttxt"
    
    elif "彩虹小屋" in msg :
        
        message = ImageSendMessage(original_content_url="https://media-cdn.tripadvisor.com/media/photo-s/0e/13/82/36/colorful-beach-houses.jpg",
                                   preview_image_url="https://media-cdn.tripadvisor.com/media/photo-s/0e/13/82/36/colorful-beach-houses.jpg"
                                  )
        status = 2                        #區別送圖片和送文字
    
    elif "眼鏡" in msg :
        glasses = 1
        txt = QueryGlasses.getProduct()  #從自己建立的資料庫抓取資料
    
    elif "空氣" in msg :
        air = 1
        txt = "請輸入要查詢的地區"
             
    else :   
#        txt = event.message.text        #鸚鵡回話linenot 答什麼回什麼
        if glasses == 1 :
            txt = QueryGlasses.getProduct(msg)
            glasses = 0                  # 中止詢問 
        elif air == 1 :
            txt = getAqi.getPM25(msg)
            air = 0
        else :
            txt = GetTextkey(msg)
        
    if status == 1 :
                   
        message = TextSendMessage(text = txt)
         
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
import requests
import json
import QueryGlasses
import getAqi

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
