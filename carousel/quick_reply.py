#############################################################################
# FileName     [ quick_reply.py ]
# PackageName  [ carousel ]
# Synopsis     [ handle quick reply ]
# Author       [ Meng-Hung (Hugo), Chen ]
# Copyright    [ Copyleft(c) 2021 ]
#############################################################################

#############################################################################
#                                 import                                    #
#############################################################################
# python kits
from linebot.models import QuickReply, QuickReplyButton, MessageAction

#############################################################################
#                                function                                   #
#############################################################################
def get_quick_reply(keywords: list):
    items = list()
    for keyword in keywords:
        items.append(QuickReplyButton(
            action=MessageAction(
            label=keyword,
            text=keyword
            )
        ))
    return QuickReply(
        items=items
    )