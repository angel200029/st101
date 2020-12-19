from django.conf import settings


from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
from linebot.models import TemplateSendMessage,ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from linebot.models import ImagemapSendMessage, BaseSize, MessageImagemapAction, URIImagemapAction, ImagemapArea, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction
from linebot.models import TextSendMessage, AudioSendMessage, VideoSendMessage
from linebot.models import BubbleContainer, ImageComponent, BoxComponent, TextComponent, IconComponent, ButtonComponent, SeparatorComponent, FlexSendMessage, URIAction
from linebot.models import TextSendMessage, ImageSendMessage, LocationSendMessage, TemplateSendMessage,ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction
from linebot import LineBotApi, WebhookParser
#from hotelapi.models import booking
#from hotelapi.models import users

import datetime
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
def sendText(event):  #傳送文字
    try:
        message = TextSendMessage(  
            text="您好，我是企業資訊整合分析！\n很高興為您服務!☺
	    text="以下是我們提供的服務項目："
	    text="@網站連結\n@國內相關組織\n@國外相關組織\n@辨別洗錢小知識"
	    text="歡迎點選下方選單了解更多詳情!"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImage(event):  #傳送圖片
    try:
        message = ImageSendMessage(
            original_content_url = "https://i.imgur.com/4QfKuz1.png",
            preview_image_url = "https://i.imgur.com/4QfKuz1.png"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendStick(event):  #傳送貼圖
    try:
        message = StickerSendMessage(  #貼圖兩個id需查表
            package_id='1',  
            sticker_id='2'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendMulti6(event):  #多項傳送
    try:
        message = [  #串列
            StickerSendMessage(  #傳送貼圖
                package_id='1',  
                sticker_id='2'
            ),
            TextSendMessage(  #傳送y文字
                text = "這是 Pizza 圖片！"
            ),
            ImageSendMessage(  #傳送圖片
                original_content_url = "https://i.imgur.com/4QfKuz1.png",
                preview_image_url = "https://i.imgur.com/4QfKuz1.png"
            )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPosition(event):  #傳送位置
    try:
        message = LocationSendMessage(
            title='銘傳大學 經濟與金融學系',
            address='333桃園市龜山區德明路5號',
            latitude=24.98606112215958,  #緯度
            longitude=121.34118714180775  #經度
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendButton4(event):  #按鈕樣板
    try:
        message = TemplateSendMessage(
            alt_text='網站連結',
            template=ButtonsTemplate(
                    thumbnail_image_url  ='https://img.onl/vEgwNh' ,
                    title  =  '企業資訊整合分析' ,
                    text  =  '相關網站' ,
            actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='財報狗',
                        text='https://statementdog.com/'
                    ),
                    URITemplateAction(  #開啟網頁
                        label  =  'Yahoo股市' ,
                        uri  =  'https://tw.stock.yahoo.com/'
                    ),
                    PostbackTemplateAction(  #執行Postback功能,觸發Postback事件
                        label='回傳訊息',  #按鈕文字
                        #text='@購買披薩',  #顯示文字計息
                        data='action=buy'  #Postback資料
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendConfirm(event):  #確認樣板
    try:
        message = TemplateSendMessage(
            alt_text='系統回饋',
            template=ConfirmTemplate(
                text='喜歡我們的系統嗎？',
                actions=[
                    MessageTemplateAction(  #按鈕選項
                        label='是',
                        text='@yes'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='@no'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendImgCarousel2(event):  #圖片轉盤
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='文字訊息',
                            text='賣披薩'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/qaAdBkR.png',
                        action=PostbackTemplateAction(
                            label='回傳訊息',
                            data='action=sell&item=飲料'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPizza(event):
    try:
        message = TextSendMessage(
            text = '感謝您購買披薩，我們將盡快為您製作。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendYes(event):
    try:
        message = TextSendMessage(
            text='感謝您的喜歡，\n我們必將提供更好服務。♥',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
	
def sendNo(event):
    try:
        message = TextSendMessage(
            text='感謝您的回饋，\n我們必定努力改善！',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))	

def sendBack_buy(event, backdata):  #處理Postback
    try:
        text1 = '感謝您購買披薩，我們將盡快為您製作。\n(action 的值為 ' + backdata.get('action') + ')'
        text1 += '\n(可將處理程式寫在此處。)'
        message = TextSendMessage(  #傳送文字
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendImgmap(event):  #圖片地圖
    try:
        image_url = 'https://i.imgur.com/Yz2yzve.jpg'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 300
        message = ImagemapSendMessage(
            base_url=image_url,
            alt_text="圖片地圖範例",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                MessageImagemapAction(  #顯示文字訊息
                    text='你點選了紅色區塊！',
                    area=ImagemapArea(  #設定圖片範圍:左方1/4區域
                        x=0, 
                        y=0, 
                        width=imgwidth*0.25, 
                        height=imgheight  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='http://www.e-happy.com.tw',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.75, 
                        y=0, 
                        width=imgwidth*0.25, 
                        height=imgheight  
                    )
                ),
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendVedio(event):  #傳送影像
    try:
        message = VideoSendMessage(
            original_content_url=baseurl + 'robot.mp4',  #影片檔置於static資料夾
            preview_image_url=baseurl + 'robot.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))



def sendPosition(event):  #位置資訊
    try:
        text1 = "333桃園市龜山區德明路5號"
        message = [
            TextSendMessage(  #顯示地址
                text = text1
            ),
            LocationSendMessage(  #顯示地圖
                title = "銘傳大學 經濟與金融學系",
                address = text1,
                latitude = 24.98606112215958,
                longitude = 121.34118714180775
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendContact(event):  #聯絡我們
    try:
        message = TemplateSendMessage(
            alt_text = "聯絡方式",
            template = ButtonsTemplate(
                thumbnail_image_url='E6%91%B3%E7%9F%A2%E9%87%8Fhttps://images.app.goo.gl/zBW6GUcLBVZq4vD5A',
                title='聯絡方式',
                text='有任何問題歡迎詢問',
                actions=[
                    URITemplateAction(label='台北校區', uri='tel:0228824564')  #開啟打電話功能   
		    URITemplateAction(label='桃園校區', uri='tel:033507001') 
		URITemplateAction(label='基河校區', uri='tel:0228824564') 
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇想了解的法律資訊',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="金融法規", text="https://law.banking.gov.tw/Chi/default.aspx")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="民法", text="https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0000001")
                    ),
			QuickReplyButton(
                        action=MessageAction(label="刑事訴訟法", text="https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=C0010001")
                    ),
			 QuickReplyButton(
                        action=MessageAction(label="中華民國刑法", text="https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=C0000001")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="金管會", text="https://www.fsc.gov.tw/ch/index.jsp")
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def sendMulti2(event):  #多項傳送
    try:
        message = [  #串列

            TextSendMessage(  #傳送y文字
                text = "何謂洗錢？"
            ),
            ImageSendMessage(  #傳送圖片
                original_content_url ="https://img.itw01.com/images/2018/03/05/20/4828_rb0nUb_C75LEGQ.jpeg!r800x0.jpg",
                preview_image_url = "https://img.itw01.com/images/2018/03/05/20/4828_rb0nUb_C75LEGQ.jpeg!r800x0.jpg"
            ),

	   TextSendMessage(  #傳送y文字
                text = "洗錢:\n將其不法行為活動獲得的資金或財產，透過各種交易管道掩飾或隱匿， 轉換成為合法的資金或財產。"
            ),
	   TextSendMessage(  #傳送y文字
                text = "洗錢的架構:1.特定罪犯行為 2.取得不法利益 3.洗清黑錢"
            ),


            TextSendMessage(  #傳送y文字
                text ="https://www.youtube.com/watch?v=F-ESYoE0w0k"
	    ),

        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendButton3(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='重要資訊',
            template=ButtonsTemplate(
                thumbnail_image_url='https://evernote.com/blog/wp-content/uploads/2016/08/Facebook_LinkImage_1200x627-copy-1-300x300.png',  #顯示的圖片
                title=' ',  #主標題
                text='相關網站：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='"財報狗',
                        text='https://statementdog.com/'
                    ),
		    MessageTemplateAction( 
                        label='台灣公司網',
                        text='https://www.twincn.com/'
                    ),
		    MessageTemplateAction( 
                        label='台灣經濟研究院',
                        text='https://www.tier.org.tw/index.aspx'
                    ),
		   MessageTemplateAction( 
                        label='股市talk',
                        text='https://stock.cnyes.com/market/TWS:TSE01:INDEX'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendButton(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='網站連結',
            template=ButtonsTemplate(
                thumbnail_image_url='https://img.onl/vEgwNh',  #顯示的圖片
                title='企業資訊整合分析',  #主標題
                text='相關網站：',  #副標題
                actions=[
                URITemplateAction(
                        label='財報狗',
                        uri='https://statementdog.com/'
                    ),
                URITemplateAction(
                        label='台灣公司網',
                        uri='https://www.twincn.com/'
                    ),
		URITemplateAction(
                        label='台灣經濟研究院',
                        uri='https://www.tier.org.tw/index.aspx'
                    ),
		URITemplateAction(
                        label='股市talk',
                        uri='https://stock.cnyes.com/market/TWS:TSE01:INDEX'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))




def sendButtonb_out(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='防制洗錢小知識',
            template=ButtonsTemplate(
                thumbnail_image_url='https://cnews.com.tw/wp-content/uploads/%E5%8F%B0%E7%81%A3%E5%8F%8D%E6%B4%97%E9%8C%A2%E9%98%B2%E5%88%B6%E3%80%8C%E8%90%BD%E5%BE%8C%E3%80%8D-%E9%87%91%E7%AE%A1%E6%9C%83%E7%A0%94%E8%AD%B0%E7%9B%B8%E9%97%9C%E6%8E%AA%E6%96%BD.jpg',  #顯示的圖片
                title=' ',  #主標題
                text='國外相關組織：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='FATF',
                        text='https://www.fatf-gafi.org/home/'
                    ),
                    MessageTemplateAction( 
                        label='APG',
                        text='http://www.apgml.org/'
                    ),
                     MessageTemplateAction( 
                        label='艾格蒙聯盟',
                        text='https://egmontgroup.org/en'
                  

                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
	
def sendButtonb_in(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='防制洗錢小知識',
            template=ButtonsTemplate(
                thumbnail_image_url='https://cnews.com.tw/wp-content/uploads/%E5%8F%B0%E7%81%A3%E5%8F%8D%E6%B4%97%E9%8C%A2%E9%98%B2%E5%88%B6%E3%80%8C%E8%90%BD%E5%BE%8C%E3%80%8D-%E9%87%91%E7%AE%A1%E6%9C%83%E7%A0%94%E8%AD%B0%E7%9B%B8%E9%97%9C%E6%8E%AA%E6%96%BD.jpg',  #顯示的圖片
                title=' ',  #主標題
                text='國內相關組織：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='行政院防制洗錢辦公室',
                        text='https://www.amlo.moj.gov.tw/'
                    ),
                    MessageTemplateAction( 
                        label='法務部調查局洗錢防制處',
                        text='https://www.mjib.gov.tw/mlpc'
                    ),
                     MessageTemplateAction( 
                        label='金管會',
                        text='https://www.fsc.gov.tw/ch/index.jsp'
                  

                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
	  
def sendCarousel(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='其他',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT4NQBoplbhOoo3bc_Zgj37mraOw88ddrWP7LTZfpfnY7FcDr5m&usqp=CAU',
                        title='財經新聞',
                        text='國內外即時新聞統整',
                        actions=[
                            URITemplateAction(
                                label='洗錢防制之最終受益人查詢',
                                uri='https://reurl.cc/AqXVEe'
                            ),
                            MessageTemplateAction(
                                label='國際防制洗錢標準',
                                text='1.處罰洗錢及資恐行為2.沒收不法所得及進行目標制裁3.國際合作4.建立防治機制'
                            ),
		          
                             URITemplateAction(
                                label='最新資訊',
                                uri='https://www.amlo.moj.gov.tw/1461/1467/Lpsimplelist'
                            ),
                            
                        ]
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))



