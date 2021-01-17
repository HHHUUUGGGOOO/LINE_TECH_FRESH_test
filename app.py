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
import os
import time
from datetime import datetime, timedelta
from flask import Flask, request, abort
from message import text_message, location_message, follow_event_message
from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import (
  MessageEvent, TextMessage, TextSendMessage, LocationMessage,
  FollowEvent, UnfollowEvent
)

#############################################################################
#                                parameter                                  #
#############################################################################
app = Flask(__name__)