#############################################################################
# FileName     [ skill.py ]
# PackageName  [ carousel ]
# Synopsis     [ handle skill's bubble container ]
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
# [python logo, 'Python', 'Project name', 'course', github link]
category = ['python', 'c++', 'matlab']
py_logo = 'https://i.imgur.com/mDd4HGq.jpg'
c_logo = 'https://i.imgur.com/gtJYuvD.png'
matlab_logo = 'https://i.imgur.com/XhH3OQt.png'

# Python
CS_PA = [py_logo, 'Python', 'Snake AI', 'Computer Science', 'https://github.com/HHHUUUGGGOOO/Intro-of-Computer-Science.git']
vpy_PA = [py_logo, 'Python', 'Baseball Path Simulation', 'Physics', 'https://github.com/HHHUUUGGGOOO/Phisics_vpython.git']
Data_Structure_PA = [py_logo, 'Python', 'Page Rank / Hash', 'Dara Structure', 'https://github.com/HHHUUUGGGOOO/Data-Structure.git']

# C++
DSnP_PA = [c_logo, 'C++', 'Fraig', 'DSnP', 'https://github.com/HHHUUUGGGOOO/DSnP.git']
EDA_PA = [c_logo, 'C++', 'X-Value Equivalence', 'Intro of EDA', 'https://github.com/HHHUUUGGGOOO/Intro-of-EDA.git']
Alg_PA = [c_logo, 'C++', 'Cycle Removal', 'Algorithm', 'https://github.com/HHHUUUGGGOOO/Algorithm.git']

# MATLAB
Quantum_PA = [matlab_logo, 'MATLAB', 'QIA', 'Communication System', 'https://github.com/HHHUUUGGGOOO/Communication-System.git']

#############################################################################
#                                function                                   #
#############################################################################
# Python --> 計概作業 / 普物vpython final / 資結PA
# C++ --> DSnP / EDA final / 演算法PA
# MATLAB --> 通信
def get_skill_carousel():
    global category, py_logo, c_logo, matlab_logo, CS_PA, vpy_PA, Data_Structure_PA, DSnP_PA, EDA_PA, Alg_PA, Quantum_PA
    bubble = list()
    py = [CS_PA, vpy_PA, Data_Structure_PA]
    c = [DSnP_PA, EDA_PA, Alg_PA]
    mat = [Quantum_PA]
    info = [py, c, mat]
    for cat in info:
        bubble.append(my_skill(cat))
    return CarouselContainer(
        contents=bubble 
    )

def my_skill(cat: list):
    # [[python logo, 'Python', 'Project name', 'course', github link], ...]
    skill_contents = list()
    for detail in cat:
        skill_contents.append(BoxComponent(
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
                            text=detail[2],
                            size='md',
                            color='#222E38',
                            weight='bold'
                        ),
                        TextComponent(
                            text=detail[3],
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
                                label='github link',
                                uri=detail[4]
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
                            url=detail[0],
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
                                    text=detail[1],
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
                    contents=skill_contents
                )
            ]
        )
    )



