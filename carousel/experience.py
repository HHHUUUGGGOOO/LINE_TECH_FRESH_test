#############################################################################
# FileName     [ experience.py ]
# PackageName  [ carousel ]
# Synopsis     [ handle experience's bubble container ]
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
#                                parameter                                  #
#############################################################################
# [該活動照片url, 該活動名字, 該活動我的頭銜, 該活動頭銜時間]
# 2020 卡伯團隊一員
pic_1 = 'https://i.imgur.com/zuf84NF.jpg'
cardbo_2020 = [pic_1, 'Cardbo Team', 'Engineer', 'Aug,2020 - now']

# 2020 宿營總召
pic_2 = 'https://i.imgur.com/v8LzMeF.jpg'
EE_camp = [pic_2, 'NTUEE Orientation Camp', 'Event General Coordinator', 'Aug,2020']

# 2020 GIS國際部部員
pic_3 = 'https://i.imgur.com/Hg4dn92.jpg'
GIS_2020 = [pic_3, 'GIS Taiwan 2020', 'Officer of Delegate Affairs', 'Oct,2019 - now']

# 2020 ATCC參賽
pic_4 = 'https://i.imgur.com/MtPGElS.jpg'
ATCC_2020 = [pic_4, 'ATCC commercial contest', 'Team Member', 'May,2020']

# 2018 台大簡報大賽第10名
pic_5 = 'https://i.imgur.com/3davbUK.jpg'
Presentation_2018 = [pic_5, 'NTU Presentation Contest', '10-th place', 'Dec,2018']

# 2018 NASA營隊 project manager
pic_6 = 'https://i.imgur.com/ETXtkqM.jpg'
NASA_2018 = [pic_6, 'HASSE NASA Camp', 'Project Manager', 'Jul,2018']

exp_data = [cardbo_2020, EE_camp, GIS_2020, ATCC_2020, Presentation_2018, NASA_2018]

#############################################################################
#                                function                                   #
#############################################################################
# 2020 卡伯團隊一員
# 2020 宿營總召
# 2020 GIS國際部部員
# 2020 ATCC參賽
# 2018 台大簡報大賽第10名
# 2018 NASA營隊 project manager
def get_exp_carousel():
    global exp_data, cardbo_2020, EE_camp, GIS_2020, ATCC_2020, Presentation_2018, NASA_2018
    bubble = list()
    for exp in exp_data:
        bubble.append(my_experience(exp))
    return CarouselContainer(
        contents=bubble
    )

def my_experience(exp: list):
    # [該活動照片url, 該活動名字, 該活動我的頭銜, 該活動頭銜時間]
    return BubbleContainer(
        body=BoxComponent(
            layout='vertical',
            padding_all='0px',
            contents=[
                BoxComponent(
                    layout='vertical',
                    contents=[
                        ImageComponent(
                            url=exp[0],
                            size='full',
                            aspect_mode='cover',
                            aspect_ratio='4:3',
                            gravity='center'
                        )
                    ]
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
                                    text=exp[1],
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
                    contents=[
                        BoxComponent(
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
                                            text=exp[2],
                                            size='md',
                                            color='#222E38',
                                            weight='bold'
                                        ),
                                        TextComponent(
                                            text=[3],
                                            size='xs',
                                            color='#6A7E8D'
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    )