#############################################################################
# FileName     [ greeting.py ]
# PackageName  [ carousel ]
# Synopsis     [ choose one part ]
# Author       [ Meng-Hung (Hugo), Chen ]
# Copyright    [ Copyleft(c) 2021 ]
#############################################################################

#############################################################################
#                                 import                                    #
#############################################################################
# python kits
import json
from linebot.models import (
  CarouselContainer, BubbleContainer, BoxComponent, 
  TextComponent, ButtonComponent, IconComponent,
  MessageAction, ImageComponent, URIAction, 
  LinearGradientBackground, FillerComponent, SeparatorComponent
)

#############################################################################
#                                function                                   #
#############################################################################
def get_greeting_carousel(parts: list):
    buttons = []
    elements = []
    for i, part in enumerate(parts):
        elements.append(ButtonComponent(
            color='#097AC5',
            action=MessageAction(
                label=part,
                text=part
            )
        ))
        if i % 2 == 1:
            buttons.append(BoxComponent(
                layout="horizontal",
                color='#097AC5',
                contents=list(elements)
                ))
            elements = []
    
    return CarouselContainer(
        contents=[
            BubbleContainer(
                size='mega',
                body=BoxComponent(
                    layout="vertical",
                    background_color='#f8f8f8',
                    contents=[
                        TextComponent(
                            align='start',
                            color='#222E38',
                            text='😇If wanna know me more, please click your interested section below！',
                            size='md',
                            weight='regular',
                            wrap=True
                        )
                    ]
                ),
                footer=BoxComponent(
                    layout="vertical",
                    padding_all='none',
                    background_color='#F8F8F8',
                    contents=list(buttons)
                )
            )
        ]
    )