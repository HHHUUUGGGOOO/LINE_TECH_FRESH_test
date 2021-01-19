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
alg = ['a', 'https://i.imgur.com/wB4QE0K.jpg', 'Algorithm', 'Prof. a', 'C++']
EDA = ['a', 'https://i.imgur.com/Om1trmj.jpg', 'Intro of EDA', 'Prof. a', 'C++']
DsnP = ['a', 'https://i.imgur.com/JySOygr.png', 'DSnP', 'Prof. a', 'C++']
CS = ['a', 'https://i.imgur.com/Vk2sEUc.jpg', 'Intro of Computer Science', 'Prof. a', 'C++']

# Python
ML = ['a', 'https://i.imgur.com/GIskEyS.jpg', 'Machine Learning', 'Prof. a', 'Python']
Data_Structure = ['a', 'https://i.imgur.com/KulysSR.jpg', 'Data Structure', 'Prof. a', 'Python']
Linear_Alg = ['a', 'https://i.imgur.com/GIskEyS.jpg', 'Linear Algebra', 'Prof. a', 'Python']
Programming = ['a', 'https://i.imgur.com/mbBpwa4.jpg', 'Computer Programming', 'Prof. a', 'Python']

# Theoretics
Game_Theory = ['a', 'https://i.imgur.com/Blwsf9z.jpg', 'Game Theory', 'Prof. a', 'Theoretics']

# NTU Presentation
Presentation = ['a', 'https://i.imgur.com/AFq9HgX.jpg', 'NTU Presentation', 'Prof. a', 'Practical']

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
        )
    )