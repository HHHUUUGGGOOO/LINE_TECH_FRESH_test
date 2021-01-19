#############################################################################
# FileName     [ course.py ]
# PackageName  [ carousel ]
# Synopsis     [ handle course's bubble container ]
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
# [[修課學期, 教授照片, 課程名稱, 教授名字, C++], ...]
# C++
alg = ['大三下', 'https://i.imgur.com/wB4QE0K.jpg', 'Algorithm', 'Prof. 張耀文', 'C++']
EDA = ['大二下', 'https://i.imgur.com/Om1trmj.jpg', 'Intro of EDA', 'Prof. 江介宏', 'C++']
DsnP = ['大二上', 'https://i.imgur.com/JySOygr.png', 'DSnP', 'Prof. 黃鍾揚', 'C++']
CS = ['大一下', 'https://i.imgur.com/Vk2sEUc.jpg', 'Intro of Computer Science', 'Prof. 于天立', 'C++']

# Python
ML = ['預計大三下', 'https://i.imgur.com/GIskEyS.jpg', 'Machine Learning', 'Prof. 李宏毅', 'Python']
Data_Structure = ['大三上', 'https://i.imgur.com/KulysSR.jpg', 'Data Structure', 'Prof. 顏嗣鈞', 'Python']
Linear_Alg = ['大二上', 'https://i.imgur.com/GIskEyS.jpg', 'Linear Algebra', 'Prof. 李宏毅', 'Python']
Programming = ['大一上', 'https://i.imgur.com/mbBpwa4.jpg', 'Computer Programming', 'Prof. 林宗男', 'Python']

# Theoretics
Game_Theory = ['大一下', 'https://i.imgur.com/Blwsf9z.jpg', 'Game Theory', 'Prof. 呂學一', 'Theoretics']

# NTU Presentation
Presentation = ['大一上', 'https://i.imgur.com/AFq9HgX.jpg', 'NTU Presentation', 'Prof. 葉丙成', 'Practical']

data = [alg, EDA, DsnP, CS, ML, Data_Structure, Linear_Alg, Programming, Game_Theory, Presentation]

#############################################################################
#                                function                                   #
#############################################################################
def get_course_carousel():
    global data, alg, EDA, DsnP, CS, ML, Data_Structure, Linear_Alg, Programming, Game_Theory, Presentation
    bubble = list()
    for courses in data:
        bubble.append(my_course(courses))

def my_course(my_class: list):
    # [[修課學期, 教授照片, 課程名稱, 教授名字, C++], ...]
    return BubbleContainer(
        size='mega',
        header=BoxComponent(
            layout='vertical',
            padding_all='xl',
            padding_bottom='none',
            background_color='#f8f8f8',
            contents=[
                BoxComponent(
                    layout='horizontal',
                    spacing='none',
                    margin='none',
                    padding_top='md',
                    contents=[
                        TextComponent(
                            size='xxl',
                            gravity='center',
                            text=my_class[0],
                            align='start',
                            color='#495057',
                        )
                    ]
                )
            ]
        ),
        body=BoxComponent(
            layout='vertical',
            padding_top='none',
            background_color='#f8f8f8',
            contents=[
                BoxComponent(
                    layout='vertical',
                    padding_all='md',
                    background_color='#f8f8f8',
                    contents=[
                        BoxComponent(
                            layout='horizontal',
                            padding_all='md',
                            background_color='#f8f8f8',
                            contents=[
                                ImageComponent(
                                    url=my_class[1],
                                    size='4xl',
                                    aspect_mode='fit',
                                    aspect_ratio='8:5'
                                )
                            ]
                        ),
                        BoxComponent(
                            layout='vertical',
                            padding_top='md',
                            padding_bottom='md',
                            contents=[
                                BoxComponent(
                                    layout='horizontal',
                                    contents=[
                                        TextComponent(
                                            text=my_class[2],
                                            style='normal',
                                            size='lg',
                                            color='#222E38',
                                            wrap=False
                                        )
                                    ]
                                ),
                                BoxComponent(
                                    layout='horizontal',
                                    contents=[
                                        TextComponent(
                                            text=my_class[3],
                                            style='normal',
                                            size='sm',
                                            color='#6A7E8D'
                                        )
                                    ]   
                                )
                            ]
                        ),
                        BoxComponent(
                            layout='vertical',
                            padding_top='md',
                            spacing='lg',
                            contents=[
                                TextComponent(
                                    text=my_class[4],
                                    align='start',
                                    color='#222E38',
                                    size='xl',
                                    weight='bold'
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        footer=BoxComponent(
            layout='vertical',
            padding_all='none',
            background_color='#F8F8F8',
            contents=[
                ButtonComponent(
                    color='#097AC5',
                    action=URIAction(
                        label='Github',
                        uri='https://github.com/HHHUUUGGGOOO'
                    )
                )
            ]
        )
    )