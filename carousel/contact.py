#############################################################################
# FileName     [ contact.py ]
# PackageName  [ carousel ]
# Synopsis     [ my contact way ]
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
def contact_me():
    contact_contents = list()
    Facebook_link = 'https://www.facebook.com/profile.php?id=100009578771776'
    Github_link = 'https://github.com/HHHUUUGGGOOO'
    Mail_link = 'mailto:b07901103@ntu.edu.tw'
    info = [['Facebook', '陳孟宏', Facebook_link], ['Github', 'HHHUUUGGGOOO', Github_link], ['E-mail', 'b07901103@ntu.edu.tw', Mail_link]]
    for detail in info:
        contact_contents.append(BoxComponent(
            layout='horizontal',
            padding_start='xxl',
            padding_end='xxl',
            background_color='#FFFFFF',
            margin='none',
            contents=[
                BoxComponent(
                    layout='vertical',
                    contents=[
                        TextComponent(
                            text=detail[0],
                            size='md',
                            color='#222E38',
                            weight='bold'
                        ),
                        TextComponent(
                            text=detail[1],
                            size='xs',
                            color='#6A7E8D'
                        )
                    ]
                ),
                BoxComponent(
                    layout='vertical',
                    width='100px',
                    contents=[
                        ButtonComponent(
                            color='#097AC5',
                            offset_bottom='md',
                            action=URIAction(
                                label='link',
                                url=detail[2]
                            )
                        )
                    ]
                )
            ]
        ))
    return BubbleContainer(
        body=BoxComponent(
            layout='vertical',
            padding_all='0px',
            contents=[
                BoxComponent(
                    layout='vertical',
                    contents=[
                        ImageComponent(
                            url='https://i.imgur.com/91v54MO.jpg',
                            size='full',
                            aspect_mode='cover',
                            aspect_ratio='4:3',
                            gravity='center'
                        )
                ),
                BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    padding_top='sm',
                    padding_bottom='sm',
                    offset_top='none',
                    background_color='#095AA3',
                    contents=[
                        BoxComponent(
                            layout='horizontal',
                            padding_start='xxl',
                            padding_end='xxl',
                            contents=[
                                TextComponent(
                                    text='These are my contact ways！',
                                    wrap=True,
                                    color='#FFFFFF',
                                    align='center',
                                    size='15px'
                                )
                            ]
                        )
                    ]
                ),
                BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    padding_top='md',
                    offset_top='none',
                    background_color='#FFFFFF',
                    contents=contact_contents
                ),
                ButtonComponent(
                    style='link',
                    height='sm',
                    color='#097AC5',
                    action=URIAction(
                        label='Mobile',
                        url='tel:+886-966540165'
                    )         
                )
            ]
        )
    )