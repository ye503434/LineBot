from flask import Flask , request

import json , time

# import Line Message Api 相關函式庫
from linebot import LineBotApi , WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent , TextMessage , TextSendMessage , StickerSendMessage , ImageSendMessage , LocationSendMessage


app = Flask(__name__)
def weather(address):
    result = {}
    code = 'CWA-9F11B97E-26B6-4BC7-BF69-EBE271BBBEA9' #氣象的Token
    url = [f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization={code}',
           f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization={code}']//天氣和氣象觀測API網址
    for item in url :
        req = request.get(item)
        data = req.json() ## .load 讀取json檔 .loads解析JSON字串 .json處理API回傳
        station = data['records']['Station']
        
    
    
    
@app.route("/", methods = ["POST"])
def lineBot():
    
    access_token = "KSt0aeep3aTpoKS09/24tGmBk6foB/48lqzhyqHskcfZvH92nUY77ubZglFTr+sET2EwzpXleXRyZUEYJq8Pb2yFOZSVUmHlCxGaUB8HqtHLyB6wEsas2VpNuhbPnIHRmDKttkisjYNE9C8EcEJWlQdB04t89/1O/w1cDnyilFU="
    channel_secret = "9f87acee45e386ede9c8ed3aca65cc95"
    lineBotApi = LineBotApi(access_token) # 確認 token
    handler = WebhookHandler(channel_secret) #確認 secret 

    body = request.get_data(as_text=True)
    try :
        json_data = json.loads(body) # json編譯
        print(json_data)
        
        signature = request.headers["X-Line_Signature"] #加入回傳的 headers
        handler.handle(body,signature)
        tk = json_data["events"][0]["replyToken"]
        userId = json_data["events"][0]["source"]["userId"]
        type = json_data["events"][0]["message"]["type"]
        
        if type == "text":
            msg = json_data["events"][0]["message"]["text"]
            if msg == "雷達迴波圖" or msg == "雷達迴波" :
                
                lineBotApi.push_message(userId , TextSendMessage(text = "馬上找給你!稍等"))
                imgUrl = f"https://cwaopendata.s3.ap-northeast-1.amazonaws.com/Observation/O-A0058-002.png?{time.time_ns()}"
                imgMessage = ImageSendMessage(original_content_url=imgUrl , preview_image_url=imgUrl)
                lineBotApi.reply_message(tk,imgMessage)
                
            else : 
                
                textMessage = TextSendMessage(text=msg)
                lineBotApi.reply_message(tk,textMessage)
                
    except Exception as e:
        print(e)
    return "OK"
if __name__ == "__main__":
    app.run(port = 5000 , debug=True)
