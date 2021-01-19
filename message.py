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
  ButtonsTemplate, URITemplateAction, VideoSendMessage, ImageSendMessage
)
# files
from user import User
from carousel import quick_reply, skill, experience, course, greeting, motivation, contact

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
        messages.append(TextSendMessage(text='Nice to meet you！What part of me do you wanna know more！😇', quick_reply=quick_reply.get_quick_reply(['contact', 'skill','experience', 'course', 'motivation'])))
        return messages
    # Motivation's 4 stages
    if msg.lower() in ['begin', 'rookie in cardbo', 'engineer in cardbo', 'target']:
        # text: 簡述 / image: 代表照片 / quick_reply: 可以重新選
        messages = list()
        messages.append(TextSendMessage(text=motivation.text_stage(msg.lower())))
        messages.append(ImageSendMessage(
            original_content_url = motivation.image_stage(msg.lower()),
            preview_image_url = motivation.image_stage(msg.lower()),
            quick_reply=quick_reply.get_quick_reply(['Begin', 'Rookie in Cardbo', 'Engineer in Cardbo', 'Target'])
        )) 
        return messages
    # Contact  
    if msg.lower() == "contact":
        user.mode = 1  
        return FlexSendMessage(alt_text="contact me", contents=contact.contact_me())
    # Skill
    elif msg.lower() == "skill":
        user.mode = 2
        return FlexSendMessage(alt_text="my skill and project", contents=skill.get_skill_carousel())
    # Experience
    elif msg.lower() == "experience":
        user.mode = 3
        return FlexSendMessage(alt_text="my experience", contents=experience.get_exp_carousel())
    # Course
    elif msg.lower() == "course":
        user.mode = 4
        return FlexSendMessage(alt_text="my course", contents=course.get_course_carousel())
    # Motivation
    elif msg.lower() == "motivation":
        user.mode = 5
        return TextSendMessage(text='Below is my progress, or say "journey", in LINE development, hope you can enjoy, too！', quick_reply=quick_reply.get_quick_reply(['Begin', 'Rookie in Cardbo', 'Engineer in Cardbo', 'Target']))
    # Introduction Video
    elif msg.lower() == "self intro":
        user.mode = 6
        messages = list()
        messages.append(TextSendMessage(text='🙋‍♂️Hi！I am Hugo Chen, an undergraduate studied in NTUEE.\n📸The attached video is my brief introduction！\n😇If wanna know me more, please click your interested section below！'))
        messages.append(VideoSendMessage(
            original_content_url = 'https://cardbogo.slack.com/files/U0182KKAUNP/F01KV71LSAC/self-intro.mp4',
            preview_image_url = 'https://i.imgur.com/RtuVLZQ.jpg'
        ))        
        return messages
    # handle other input message
    else:
        return FlexSendMessage(alt_text="Choose one！", contents=greeting.get_greeting_carousel(['contact', 'skill', 'experience', 'course', 'motivation', 'self intro']))

# Follow event
def follow_event_message(user: User):
    user.tutorial_step = 0
    messages = list()
    messages.append(TextSendMessage(text='🙋‍♂️Hi！I am Hugo Chen, an undergraduate studied in NTUEE.\n📸The attached video is my brief introduction！\n😇If wanna know me more, please click your interested section below！'))
    messages.append(VideoSendMessage(
        original_content_url = 'https://cardbogo.slack.com/files/U0182KKAUNP/F01KV71LSAC/self-intro.mp4',
        preview_image_url = 'https://i.imgur.com/RtuVLZQ.jpg',
        quick_reply=quick_reply.get_quick_reply(['Finish！'])
    ))
    
    return messages

# Error handling
def error_message(msg):
    return TextSendMessage(text='Sorry for the busy server...😓')