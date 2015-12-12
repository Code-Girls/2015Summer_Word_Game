#!/usr/bin/python
# coding=UTF-8
#-*-coding:utf-8-*-

# 1 - Import library
import pygame
from pygame.locals import *
import math
import random


# 2 - Initialize the game
pygame.init()
list = []
start = 1
textPositon = [(100,120),(100,210),(100, 300),(100, 390)]
keys = [False, False]
               
# background w&h
width, height = 1000, 420
screen=pygame.display.set_mode((width, height))
#keyboard
keys = [False, False]
#words = []
healthvalue=194
textPosition = [(200,120),(300,120)]


# 3 - Load image
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")
background = pygame.image.load("resources/images/background.png")
healthbar = pygame.image.load("resources/images/healthbar.png")


# 4 - Load Audio
lose = pygame.mixer.Sound("resources/music/lose.wav")
win = pygame.mixer.Sound("resources/music/win.mp3")
right = pygame.mixer.Sound("resources/music/right.mp3")
wrong = pygame.mixer.Sound("resources/music/wrong.wav")
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('resources/music/backgroundmusic.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.7)

# 5- Load Vocabularies
#vocabularies
Easy = [("a proposition assumed as apremise in an argument","hypothesis") , ("an act or instance of noticing or perceiving","observation") , ("the separating of any material or abstract entity into its constituent elements","analysis") , ("to show or exhibit","display") , ("a balustraded or railed elevated platform projecting from the wall of a building", "balcony") , ("an act or instance of working or acting together for a common purpose or benefit","cooperation") , ("mutual discussion and arrangement of the terms of a transaction or agreement","negotiation") , ("a mental image or conception","fancy") , ("an animal hunted or seized for food, especially by a carnivorous animal","prey") , ("delightful","charming") , ("to reply or answer in words","respond") , ("to fill with an animating","inspire") , ("any powerful or compelling emotion or feeling","passion") , ("the act of putting to a special use or purpose","application") , ("heaviness or weight","gravity") , ("to set or place apart","isolate") , ("having or expressing a meaning","significant") , ("skilled","proficient") , ("worthy of imitation","exemplary") , ("not proud or arrogant","humble")]
Median = [("to gather or collect, often in gradual degrees" , "accumulate") , ("a written account of another person's life" , "biography") , ("to enter forcefully as an enemy; go into with hostile intent","invade") , ("a wistful desire to return in thought or in fact to a former time in one's life, to one's home or homeland", "nostalgia") , ("to anger, enrage", "provoke") , ("to hasten the occurrence of", "precipitate") , ("the highest point " , "summit") , ("to support" , "advocate") , ("decorate sth" , "embellish") , ("to make a distinction in favor of or against a person or thing on the basis of the group rather than according to actual merit", "discriminate") , ("to overcome completely in mind or feeling", "overwhelm") , ("worldly-wise; not naive", "sophisticated") , ("the treatment of disease or disorders, as by some remedial process", "therapy") , ("deviating from a standard", "abnormal") , ("to surprise in such a manner as to disillusion", "dismay"), ("an occupation, activity, or pursuit in which such interest is shown", "enthusiasm") , (" a liking or preference", "inclination") , ("worthy of note or notice" , "notable") , ("occurring or coming later or after", "subsequent") , ("wait to act because of fear, indecision, or disinclination", "hesitate")]
Difficult = [("having or exhibiting a strongly marked","temperamental") , ("to throw into confusion or disorder","confound") , ("having an old fashioned attractiveness or charm","quaint") , ("of or relating to pathology","pathological") , ("causing or tending to cause sleep","soporific") , ("derived from gratification of the senses","voluptuous") , ("any prop or support","buttress") , ("to struggle clumsily or helplessly","flounder") , ("a mournful sound resembling a dirge","dirge") , ("a plain characterized by coarse grasses and scattered tree growth","savanna") , ("to dispossess a person of ownership","expropriation") , ("to push slightly or gently","nudge") , ("of little value or account","picayune") , ("immature or inexperienced","callow") , ("beginning to exist or develop","nascent") , ("readily or plainly seen" , "palpable") , ("an elderly woman of stately dignity","dowager") , ("a bent or curved piece of tough wood used by the Australian Aborigines as a throwing club","boomerang") , ("to poke or jab with or as if with something pointed","prod") , ("characteristic of an uncle","avuncular")]
# 6 - drawing
running = 1
exitcode = 0
chosenTuples = []
values = []
#keys = []
english = []
pygame.font.init()
font = pygame.font.Font(None, 16)
index = random.randint(0, len(Easy)-1)
englishWord = Easy[index][1]
defWord = [Easy[index][0], Easy[random.randint(0, len(Easy)-1)][0], Easy[random.randint(0, len(Easy)-1)][0], Easy[random.randint(0, len(Easy)-1)][0]]
defHeight = [100, 190, 280, 370]
iniheight = [100, 190, 280, 370]
englishPos = [width-150, iniheight[random.randint(0, 3)]]
velx = 2
vely = 90
checked = 0

while running:
    #clear the screen before drawing it again
    screen.fill(0)
    # draw the background
    screen.blit(background,(0,0))  
    # red healthbar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        a = 0
        screen.blit(health, (health1+8,8))  
    # 6.1 draw the Chinese Word
    for i in xrange(1,21):
        list.append(i)
    randomList = random.sample(list,4)
    randomAnswer = random.sample(randomList,1)
    
    # 6.2 - Draw clock
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((180000-pygame.time.get_ticks())/60000)+":"+str((180000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)

    #write Chinese Words on the left
    pygame.font.init()
    font = pygame.font.Font(None, 16)
    for i in range(0,4):
        word = font.render(defWord[i], True, (0,20,20)) 
        textRect = word.get_rect()
        screen.blit(word, (50,100+i*90))


    #write English Words on the right
    pygame.font.init()
    font = pygame.font.Font(None, 16)
    word = font.render(englishWord, True, (20,0,20)) 
    screen.blit(word, (englishPos[0], englishPos[1]))
    englishPos[0] -= velx

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
##        check event:
##            keyDown:
##                k_UP:
##                    englishPos[1] -= vely
##                k_DOWN:
##                    -= 90
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                englishPos[1] -= 90
                if englishPos[1] < 0:
                    englishPos = 100
                #keys[0] = True
            elif event.key == K_s:
                englishPos[1] += 90
                if englishPos[1] > height:
                    englishPos = 380
                #keys[1]=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_s:
                keys[1] = False
                
    #English Word and Health Bar
##    if keys[0]:
##        englishPos[1]-=90
##    elif keys[1]:
##        englishPos[1]+=90
##
##    englishWord.getRect
##    set rect.top
##    rect.left

    for exp in defHeight:
        if checked == 0:
            if englishPos[1] == exp and englishPos[0] < 100:
                healthvalue -= 0
                checked = 1
            elif englishPos[0] < 100 and englishPos[1]!= exp:
                healthvalue -= random.randint(10, 20)
                checked = 1
# change the time and difficulty of vocabulary
    if pygame.time.get_ticks() < 60000:
        if englishPos[0] < 100:
            i = random.randint(0, len(Easy)-1)#correct explanation 
            englishWord = Easy[i][1]
            englishPos = [width-150, defHeight[random.randint(0,len(defHeight)-1)]]
            #randomly choose 4 explainations
            lastint = random.randint(0, len(Easy)-1)
            defWord = [Easy[lastint][0]] 
            wordCount = 0
            while wordCount < 3:
                index = random.randint(0, len(Easy)-1)
                if index != lastint:
                    defWord.append(Easy[index][0])
                    lastint = index
                    wordCount += 1
            #randomly replace one of them with the correct one
            defWord[random.randint(0, 3)] = Easy[i][0]
            checked = 0
    elif 60001 < pygame.time.get_ticks() < 120000:
        if englishPos[0] < 100:
            i = random.randint(0, len(Easy)-1)
            englishWord = Median[i][1]
            englishPos = [width-150, defHeight[random.randint(0,len(defHeight)-1)]]
            lastint = random.randint(0, len(Median)-1)
            defWord = [Median[lastint][0]] 
            wordCount = 0
            while wordCount < 3:
                index = random.randint(0, len(Median)-1)
                if index != lastint:
                    defWord.append(Median[index][0])
                    lastint = index
                    wordCount += 1
            #randomly replace one of them with the correct one
            defWord[random.randint(0, 3)] = Median[i][0]
            checked = 0
    elif 120001 < pygame.time.get_ticks() < 180000:
        if englishPos[0] < 100:
            i = random.randint(0, len(Easy)-1)
            englishWord = Difficult[i][1]
            englishPos = [width-150, defHeight[random.randint(0,len(defHeight)-1)]]
            lastint = random.randint(0, len(Difficult)-1)
            defWord = [Difficult[lastint][0]] 
            wordCount = 0
            while wordCount < 3:
                index = random.randint(0, len(Difficult)-1)
                if index != lastint:
                    defWord.append(Difficult[index][0])
                    lastint = index
                    wordCount += 1
            #randomly replace one of them with the correct one
            defWord[random.randint(0, 3)] = Difficult[i][0]
            checked = 0

    #update the screen
    pygame.display.flip()
    #10 - Win/Lose check
    if pygame.time.get_ticks()>=180000:
        running=0
        exitcode=0
        screen.blit(gameover, (0,0))
    if healthvalue<=0:
        running=0
        exitcode=0
        screen.blit(gameover, (0,0))

    # 11 - Win/lose display        
if exitcode==0:
    screen.fill(0)
    screen.blit(gameover, (0,0))
    pygame.display.flip()
     # 8 - loop through the events
while 1:
    for event in pygame.event.get():
          #check if X
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
                 
     
