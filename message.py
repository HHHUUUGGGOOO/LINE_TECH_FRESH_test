#############################################################################
# FileName     [ message.py ]
# PackageName  [ main ]
# Synopsis     [ handle LINEbot message ]
# Author       [ Meng-Hung (Hugo), Chen ]
# Copyright    [ Copyleft(c) 2021 ]
#############################################################################

#############################################################################
#                                 import                                    #
#############################################################################
# python kits
from linebot.models import (
  TextSendMessage, FlexSendMessage, TemplateSendMessage, 
  ButtonsTemplate, URITemplateAction, VideoSendMessage
)
# files
from user import User
from carousel import quick_reply, skill, experience, course

#############################################################################
#                                function                                   #
#############################################################################
# Handle message
def text_message(user: User, msg: str):
    return TextSendMessage(text='你好嘻嘻~ (text message)')

# Follow event
def follow_event_message(user: User):
    user.tutorial_step = 0
    messages = list()
    messages.append(TextSendMessage(text='🙋‍♂️Hi！I am Hugo Chen, an undergraduate studied in NTUEE.\n📸The attached video is my brief introduction！\n😇If wanna know me more, please click your interested section below！'))
    messages.append(VideoSendMessage(
        original_content_url = 'https://storage.googleapis.com/cardbo-images/linebot/tutorial-setting.mp4',
        preview_image_url = 'https://storage.googleapis.com/cardbo-images/linebot/tutorial-setting-cover.jpg',
        quick_reply=quick_reply.get_quick_reply(['Finish！'])
    ))
    
    return messages

# Error handling
def error_message(msg):
    return TextSendMessage(text='Sorry for the busy server...😓')