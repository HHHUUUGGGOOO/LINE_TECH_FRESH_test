#############################################################################
# FileName     [ motivation.py ]
# PackageName  [ carousel ]
# Synopsis     [ output motivation ]
# Author       [ Meng-Hung (Hugo), Chen ]
# Copyright    [ Copyleft(c) 2021 ]
#############################################################################

#############################################################################
#                                 import                                    #
#############################################################################


#############################################################################
#                                function                                   #
#############################################################################
# stage = ['begin', 'rookie in cardbo', 'engineer in cardbo', 'target']
def text_stage(stage: str):
  text = ''
  if stage == 'begin':
    text = 'Jul, 2020\n I teamed up to register for both Bussiness and App contest held for LINE TECH FRESH.'
  if stage == 'rookie in cardbo':
    text = 'Aug, 2020\n One of my friend in NTUEE invited me to join in their startup, Cardbo. After evaluating, I decided to join in and exited from my contest team in order to focus on learning and developing LINEbot in Cardbo team'
  if stage == 'engineer in cardbo':
    text = 'Sep, 2020\n Because I just began to learn how to develop LINEbot, I was first assigned to analyze user action; hence design a way to calculate flow and is able to shape every individual\'s action. Until Dec, 2020, I had the chance to charge for the new version LINEbot development.'
  if stage == 'target':
    text = 'Dec, 2020\n I participated in the \"LINE TECH PULSE 2020\", and had the chance to talk with LINE engineer, Hugo (same name as me). Maybe be fascinated by the joyful working space, tough competition, big chance to cooperate with top engineers in LINE, I have had a dream since then, that is, to work as an excellent engineer of LINE'
  
  return text

def image_stage(stage: str):
  url = ''
  if stage == 'begin':
    url = 'https://i.imgur.com/MtPGElS.jpg'
  if stage == 'rookie in cardbo':
    url = 'https://i.imgur.com/1O7KpqE.jpg'
  if stage == 'engineer in cardbo':
    url = 'https://i.imgur.com/zuf84NF.jpg'
  if stage == 'target':
    url = 'https://i.imgur.com/ZLcQ8PU.jpg'
  
  return url
