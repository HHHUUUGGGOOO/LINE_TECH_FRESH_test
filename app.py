#############################################################################
# FileName     [ app.py ]
# PackageName  [ main ]
# Synopsis     [ run LINEbot ]
# Author       [ Meng-Hung (Hugo), Chen ]
# Copyright    [ Copyleft(c) 2021 ]
#############################################################################

#############################################################################
#                                 import                                    #
#############################################################################
# python kits
import os
import time
from datetime import datetime, timedelta
from flask import Flask, request, abort
from message import text_message, follow_event_message
from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import (
  MessageEvent, TextMessage, TextSendMessage, LocationMessage,
  FollowEvent, UnfollowEvent
)
# files
from token_file import token
from user import User
from message import text_message, follow_event_message

#############################################################################
#                                parameter                                  #
#############################################################################
app = Flask(__name__)

line_bot_api = LineBotApi(token.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(token.CHANNEL_SECRET)

users = dict()
checked_at = datetime.now() # the right time user enter this LINEbot

#############################################################################
#                                  event                                    #
#############################################################################
# Callback
@app.route("/callback", methods=['POST'])
def callback():
    global checked_at
    # clean cache after 10 minutes leaving unused
    if datetime.now() > checked_at + timedelta(minutes=10):
        checked_at = datetime.now()
        result = clean_user_cache()
        print(result)
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:  
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# Message event
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global users

    line_id = event.source.user_id
    if line_id not in users.keys():
        users[line_id] = User(line_id)
    
    line_bot_api.reply_message(event.reply_token, text_message(users[line_id], event.message.text))

# Follow
@handler.add(FollowEvent)
def handle_follow_event(event):
    global users

    line_id = event.source.user_id
    if line_id not in users.keys():
        users[line_id] = User(line_id)
    
    line_bot_api.reply_message(event.reply_token, follow_event_message(users[line_id]))

# Unfollow
@handler.add(UnfollowEvent)
def handle_unfollow_event(event):
    line_id = event.source.user_id
    if line_id in users.keys():
        users.pop(line_id, None)

# Clean user
@app.route("/cleaning", methods=['POST'])
def clean_user_cache():
    global users

    remove_list = list()
    user_list = list()
    for user_id, user in users.items():
        if datetime.now() > user.api.auth_updated_at + timedelta(minutes=30) and user.tutorial_step == 1:
            remove_list.append(user_id)
            users.pop(user_id, None)
        else:
            user_list.append(user_id)
        
    return {
        'user_list': user_list,
        'removed:': remove_list
    }

#############################################################################
#                                 execute                                   #
#############################################################################
if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 80))
    port = int(os.environ.get('PORT', 80))   

    # app.run(host='0.0.0.0', port=port)
    AppRun = Process(target=app.run, kwargs=dict(host='0.0.0.0', port=port, threaded=True))
    RCC = Process(target=RegularGetTokenAndCleanCache, kwargs=dict(account=account, sec = 600))
    AppRun.start(); RCC.start()
    # AppRun.join()
    RCC.join()#直到RCC執行完後，AppRun才會去執行下一次，但RCC永遠不會執行完^^
