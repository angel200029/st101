from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
#from linebot.models import MessageEvent, TextSendMessage
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent
from module import func
from urllib.parse import parse_qsl
from hotelapi.models import users
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
           
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
     
        for event in events:
            user_id = event.source.user_id
            if not (users.objects.filter(uid=user_id).exists()):
              unit = users.objects.create(uid=user_id)
              unit.save()
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                  
                   mtext = event.message.text
                
                   
                   if   mtext == '@功能介紹':
                        func.sendText(event)
                        
                   elif mtext == '@國內相關組織':
                        func.sendQuickreply(event)
    
                   elif mtext == '@傳送位置':
                        func.sendPosition(event)
    
                   elif mtext == '@法律資訊':
                        func.sendQuickreply(event)
              
                   
                   elif mtext == '@國外相關組織':
                        func.sendButtonb_out(event)
                        
                   elif mtext == '@國內相關組織':
                        func.sendButtonb_in(event)
                        
                   elif mtext == '@財經新聞':
                        func.sendCarousel(event)
    
                   elif mtext == '@系統回饋':
                        func.sendConfirm(event)
    
                   elif mtext == '@Yes':
                        func.sendYes(event)
                
                   elif mtext == '@No':
                        func.sendNo(event)
               
                   elif mtext == '@位置資訊':
                        func.sendPosition1(event)

                   elif mtext == '@聯絡方式':
                        func.sendContact(event)
                        
                   elif mtext == '@法律資訊':
                        func.sendQuickreply(event)
                        
                   elif mtext == '@網站連結':
                        func.sendButton3(event) 
                        
                   elif mtext == '@何謂洗錢':
                        fun.sendMulti2(event)
                        
                   elif mtext[:3] == '###' and len(mtext) > 3:  #處理LIFF傳回的FORM資料
                        func.manageForm(event, mtext, user_id)

                   elif mtext[:6] == '123456' and len(mtext) > 6:  #推播給所有顧客
                        func.pushMessage(event, mtext)

            if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))   #取得Postback資料
                if backdata.get('action') == 'sell':
                  func.sendData_sell(event, backdata)
                if backdata.get('action') == 'yes':
                  func.sendYes(event, event.source.user_id) 

            else:            
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
               
        return HttpResponse()

    else:
        return HttpResponseBadRequest()



