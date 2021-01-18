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
    # First you need to finish the self introduction video
    if user.tutorial_step < 1 and msg != 'Finish！':
        return TextSendMessage(text='Please click \"Finish！\" to start！', quick_reply=quick_reply.get_quick_reply(['Finish！']))
    # Finish the video
    if (msg == 'Finish！'):
        user.tutorial_step = 1
        messages = list()
        messages.append(TextSendMessage(text='Nice to meet you！What part of me do you wanna know more！😇', quick_reply=quick_reply.get_quick_reply(['contact', 'skill','experience', 'course', 'motivation']))))
        return messages
    # Contact
    if msg == "contact":
        user.mode = 1
    # Skill
    elif msg == "skill":
        user.mode = 2
    # Experience
    elif msg == "experience":
        user.mode = 3
    # Course
    elif msg == "course":
        user.mode = 4
    # Motivation
    if msg == "motivation":
        user.mode = 5
    # Introduction Video
    if msg == "intro video":
        user.mode = 6

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