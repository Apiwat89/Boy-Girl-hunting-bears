import pgzrun
from random import randint

def draw():
    if PlayGame and Advice: # game page & how to play
        background1.draw()
        MG[8].draw()
        MG[10].draw()
        MG[14].draw()
        sounds.powerful.stop()
        sounds.goldn.stop()
        sounds.hurt.stop()
    if Advice == False: # how to play
        screen.clear()
        background1.draw()
        MG[15].draw()
        screen.draw.text('5\n\n10\n\n20',center=(430,180),fontsize=48,color=(139,123,139))
        screen.draw.text('10\n\n20\n\n30',center=(430,430),fontsize=48,color=(139,123,139))
        sounds.powerful.stop()
        sounds.goldn.stop()
        sounds.hurt.stop()
    elif PlayGame == False: # enter the game
        if ReGame == False: # start a new game
            background.draw()
            MG[0].draw()
            MG[1].draw()
            MG[2].draw()
            MG[3].draw()
            MG[4].draw()
            MG[5].draw()
            MG[6].draw()
            MG[7].draw()
            MG[11].draw()
            MG[12].draw()
            MG[13].draw()
            MG[16].draw()
            playgame()
            screen.draw.text('> I-TEM <',center=(WIDTH/2,580),fontsize=20,color=(155,48,255))
        if GameOver == True: # game score page
            screen.clear()
            background2.draw()
            MG[9].draw()
            MG[16].draw()
            screen.draw.text(Display_Score,center=(WIDTH/2,330),fontsize=45,color=(139,139,0))
            screen.draw.text('Click to start the game.',center=(WIDTH/2,490),fontsize=18,color=(139,123,139))
            sounds.powerful.stop()
            sounds.hurt.stop()

            
def playgame(): # send to draw()
    if Time <= 60 and Time > 25:
        screen.draw.text(f'{Time}',center=(WIDTH/2,40),fontsize=50,color=(0,0,0))
    elif Time <= 25 and Time > 10:
        screen.draw.text(f'{Time}',center=(WIDTH/2,50),fontsize=70,color=(255,0,0))
    elif Time <= 10:
        screen.draw.text(f'{Time}',center=(WIDTH/2,HEIGHT/2),fontsize=150,color=(205,0,0))
    screen.draw.text(f'SCORE BOY\n{ScoreBoy}',center=(920,40),fontsize=30,color=(0,191,255))
    screen.draw.text(f'SCORE GIRL\n{ScoreGirl}',center=(80,40),fontsize=30,color=(255,110,180))
    MG[14].y = 600
    music.stop()

    
def endgame():
    global GameOver, Time, Display_Score
    Time -= 1
    if Time == 0:
        GameOver = True
        if ScoreBoy == ScoreGirl:
            Display_Score = 'EQUAL SCORE'
        elif ScoreBoy > ScoreGirl:
            Display_Score = f'> BOY WIN! : {ScoreBoy} <\nGIRL LOSE : {ScoreGirl}'
        elif ScoreBoy < ScoreGirl:
            Display_Score = f'> GIRL WIN! : {ScoreGirl} <\nBOY LOSE : {ScoreBoy}'
        sounds.goldn.play()
        sounds.gameover.play()

        
def on_mouse_down(pos,button):
    global PlayGame, Advice, GameOver, ReGame
    global Time, ScoreBoy, ScoreGirl
    if button == mouse.LEFT:
        if PlayGame:
            if MG[8].collidepoint(pos):
                PlayGame = False
                Time = 60
                ScoreBoy = 0
                ScoreGirl = 0
                MG[0].image = IMG[0][2][1]
                MG[1].image = IMG[1][3][1]
                sounds.powerful.play()
        elif MG[13].collidepoint(pos):
            ReGame = False
            Time = 60
            ScoreBoy = 0
            ScoreGirl = 0
            setting()
            sounds.click_of.play()
            for n in pos:
                sounds.powerful.stop()
                sounds.powerful.play()
        elif MG[16].collidepoint(pos):
            PlayGame = True
            MG[14].x, MG[14].y = WIDTH/2, 500
            sounds.click.play()
            sounds.powerful.stop()
            music.play('dirty')

        if MG[14].collidepoint(pos):
            Advice = False
            MG[8].x = MG[14].x = 0
            sounds.click.play()
            music.play('password')
        elif MG[15].collidepoint(pos):
            Advice = True
            MG[8].x, MG[8].y = WIDTH/2, 420
            MG[14].x, MG[14].y = WIDTH/2, 500
            sounds.click.play()
            music.stop()
            music.play('dirty')
            
        if GameOver:
            GameOver = False
            Time = 60
            ScoreBoy = 0
            ScoreGirl = 0
            setting()
            sounds.powerful.play()
            sounds.goldn.stop()

            
def update():
    global Index
    Index = (Index + 1) % 3
    
    if keyboard.LEFT:
        MG[0].x -= 6
        MG[0].image = IMG[0][2][Index]
    elif keyboard.RIGHT:
        MG[0].x += 6
        MG[0].image = IMG[0][3][Index]
    elif keyboard.UP:
        MG[0].y -= 6
        MG[0].image = IMG[0][1][Index]
    elif keyboard.DOWN:
        MG[0].y += 6
        MG[0].image = IMG[0][0][Index]
    
    if keyboard.A:
        MG[1].x -= 6
        MG[1].image = IMG[1][2][Index]
    elif keyboard.D:
        MG[1].x += 6
        MG[1].image = IMG[1][3][Index]
    elif keyboard.W:
        MG[1].y -= 6
        MG[1].image = IMG[1][1][Index]
    elif keyboard.S:
        MG[1].y += 6
        MG[1].image = IMG[1][0][Index]

    if MG[0].x <= 0: MG[0].x = WIDTH-1
    elif MG[0].x >= WIDTH: MG[0].x = 0
    if MG[0].y <= 0: MG[0].y = HEIGHT-1
    elif MG[0].y >= HEIGHT: MG[0].y = 0
    if MG[1].x <= 0: MG[1].x = WIDTH-1
    elif MG[1].x >= WIDTH: MG[1].x = 0
    if MG[1].y <= 0: MG[1].y = HEIGHT-1
    elif MG[1].y >= HEIGHT: MG[1].y = 0
        
    item()
    score()

    ''' Continue random_item8() '''
    MG[7].y += MG[7].speed
    if MG[7].y > HEIGHT:
        item()()()()()()()()()





''' Function to pull to use '''

def item(): # send to update() and score()
    MG[2].angle -= 2.5
    MG[3].angle += 2
    MG[4].angle -= 0.5
    MG[5].angle += 1.5
    MG[6].angle -= 1
    MG[11].angle += 2.5
    MG[12].angle -= 2
    if MG[2].angle == 360: MG[2].angle = 0
    def random_item1():
        global ITEM1
        while ITEM1:
            ITEM1 = False
            MG[2].x = randint(MG[2].width, WIDTH - MG[2].width)
            MG[2].y = randint(MG[2].height, HEIGHT - MG[2].height)
        def random_item2():
            global ITEM2
            while ITEM2:
                ITEM2 = False
                MG[3].x = randint(MG[3].width, WIDTH - MG[3].width)
                MG[3].y = randint(MG[3].height, HEIGHT - MG[3].height)
            def random_item3():
                global ITEM3
                while ITEM3:
                    ITEM3 = False
                    MG[4].x = randint(MG[4].width, WIDTH - MG[4].width)
                    MG[4].y = randint(MG[4].height, HEIGHT - MG[4].height)
                def random_item4():
                    global ITEM4
                    while ITEM4:
                        ITEM4 = False
                        MG[5].x = randint(MG[5].width, WIDTH - MG[5].width)
                        MG[5].y = randint(MG[5].height, HEIGHT - MG[5].height)
                    def random_item5():
                        global ITEM5
                        while ITEM5:
                            ITEM5 = False
                            MG[6].x = randint(MG[6].width, WIDTH - MG[6].width)
                            MG[6].y = randint(MG[6].height, HEIGHT - MG[6].height)
                        def random_item6():
                            global ITEM6
                            while ITEM6:
                                ITEM6 = False
                                MG[11].x = randint(MG[11].width, WIDTH - MG[11].width)
                                MG[11].y = randint(MG[11].height, HEIGHT - MG[11].height)
                            def random_item7():
                                global ITEM7
                                while ITEM7:
                                    ITEM7 = False
                                    MG[12].x = randint(MG[12].width, WIDTH - MG[12].width)
                                    MG[12].y = randint(MG[12].height, HEIGHT - MG[12].height)
                                def random_item8():
                                    MG[7].x = randint(MG[7].width, WIDTH - MG[7].width)
                                    MG[7].y = 0
                                    MG[7].speed = randint(3,15)
                                return random_item8
                            return random_item7
                        return random_item6
                    return random_item5
                return random_item4
            return random_item3
        return random_item2
    return random_item1


def score(): # send to def update()
    global ITEM1, ITEM2, ITEM3, ITEM4, ITEM5, ITEM6, ITEM7
    global ScoreBoy, ScoreGirl

    '''
        if is ScoreBoy 
        elif is ScoreGirl
                          '''
    if MG[0].colliderect(MG[2]):
        ScoreBoy += 5
        ITEM1 = True
        item()()
        sounds.scorep.play()
    elif MG[1].colliderect(MG[2]):
        ScoreGirl += 5
        ITEM1 = True
        item()()
        sounds.scorep.play()
    if MG[0].colliderect(MG[3]):
        ScoreBoy += 10
        ITEM2 = True
        item()()()
        sounds.scorep.play()
    elif MG[1].colliderect(MG[3]):
        ScoreGirl += 10
        ITEM2 = True
        item()()()
        sounds.scorep.play()
    if MG[0].colliderect(MG[4]):
        ScoreBoy += 20
        ITEM3 = True
        item()()()()
        sounds.scorep.play()
    elif MG[1].colliderect(MG[4]):
        ScoreGirl += 20
        ITEM3 = True
        item()()()()
        sounds.scorep.play()
    if MG[0].colliderect(MG[5]):
        ScoreBoy -= 10
        ITEM4 = True
        item()()()()()
        sounds.scored.play()
    elif MG[1].colliderect(MG[5]):
        ScoreGirl -= 10
        ITEM4 = True
        item()()()()()
        sounds.scored.play()
    if MG[0].colliderect(MG[6]):
        ScoreBoy -= 20
        ITEM5 = True
        item()()()()()()
        sounds.scored.play()
    elif MG[1].colliderect(MG[6]):
        ScoreGirl -= 20
        ITEM5 = True
        item()()()()()()
        sounds.scored.play()
    if MG[0].colliderect(MG[11]):
        ScoreBoy += 5
        ITEM6 = True
        item()()()()()()()
        sounds.scorep.play()
    elif MG[1].colliderect(MG[11]):
        ScoreGirl += 5
        ITEM6 = True
        item()()()()()()()
        sounds.scorep.play()
    if MG[0].colliderect(MG[12]):
        ScoreBoy += 10
        ITEM7 = True
        item()()()()()()()()
        sounds.scorep.play()
    elif MG[1].colliderect(MG[12]):
        ScoreGirl += 10
        ITEM7 = True
        item()()()()()()()()
        sounds.scorep.play()
    if MG[0].colliderect(MG[7]):
        ScoreBoy -= 30
        item()()()()()()()()()
        sounds.hurt.play()
    elif MG[1].colliderect(MG[7]):
        ScoreGirl -= 30
        item()()()()()()()()()
        sounds.hurt.play()

        
def I_M_A_G_E_S():
    global MG, IMG

    boy = Actor('boy1',(900,HEIGHT/2))
    girl = Actor('girl1',(100,HEIGHT/2))
    
    item1 = Actor('item1',(600,380))
    item_1 = Actor('item1',(400,380))
    item2 = Actor('item2',(600,200))
    item_2 = Actor('item2',(400,200))
    item3 = Actor('item3',(WIDTH/2,HEIGHT/2))
    item4 = Actor('item4',(WIDTH/2,140))
    item5 = Actor('item5',(WIDTH/2,450))
    item6 = Actor('item6')

    logogame = Actor('logogame',(WIDTH/2,200))
    playbutton = Actor('playbutton',(WIDTH/2,420))
    advicebutton = Actor('advicebutton',(WIDTH/2,500))
    aboutitem = Actor('aboutitem',(WIDTH/2,HEIGHT/2))
    resetbutton = Actor('resetbutton',(950,560))
    homebutton = Actor('homebutton',(50,560))
    scoreboard = Actor('scoreboard',(WIDTH/2,HEIGHT/2))
    
    MG = [boy,girl,item1,item2,item3,item4,item5,item6,playbutton,scoreboard,logogame,
          item_1,item_2,resetbutton,advicebutton,aboutitem,homebutton]
    IMG = [(('boy1','boy2','boy1'),('boy3','boy4','boy3'),('boy5','boy6','boy5'),('boy7','boy8','boy7')),
           (('girl1','girl2','girl1'),('girl3','girl4','girl3'),('girl5','girl6','girl5'),('girl7','girl8','girl7'))]
    return MG,IMG


def setting():
    MG[0].x = 900
    MG[1].x = 100
    MG[5].y = 140
    MG[6].y = 450
    MG[2].x = MG[3].x = 600
    MG[3].y = MG[12].y = 200
    MG[2].y = MG[11].y = 380
    MG[11].x = MG[12].x = 400
    MG[4].x = MG[5].x = MG[6].x = WIDTH/2
    MG[0].y = MG[1].y = MG[4].y = HEIGHT/2
    MG[0].image = IMG[0][2][1]
    MG[1].image = IMG[1][3][1]




    
TITLE = 'Boy & Girl hunting bears'
WIDTH = 1000
HEIGHT = 600
background = Actor('background')
background1 = Actor('background1')
background2 = Actor('background2')
Time = 0
Index = 0
ScoreBoy = 0
ScoreGirl = 0
PlayGame = True
Advice = True
ReGame = False
GameOver = False
ITEM1 = False
ITEM2 = False
ITEM3 = False
ITEM4 = False
ITEM5 = False
ITEM6 = False
ITEM7 = False
I_M_A_G_E_S()
item()()()()()()()()()
clock.schedule_interval(endgame,1.0)
music.play('dirty')

pgzrun.go()





'''

1. เก็บ หมี จะได้คะแนน
2. หมี มี 3 สี แต่ละสีคะแนนก็จะต่างกันออกไป
3. เก็บอะไรที่ไม่ใช่ หมี คะแนนจะถูกหัก
4. สิ่งของที่ไม่ใช่ หมี มี 3 แบบ แต่ละแบบคะแนนที่ถูกหักก็จะต่างกันออกไป

'''



''' Description :)                                          Function
=====================================================================

                                                          I_M_A_G_E_S                                                          
➥ manage photo collections

                        MG  :  IMG = Character animation only
[0] = boy                   :  
[1] = girl                  :  
[2] = item1                 |  
[3] = item2                 |  
[4] = item3                 :  
[5] = item4                 :  
[6] = item5                 |  
[7] = item6                 |  
[8] = playbutton            |  
[9] = scoreboard            :  
[10] = logogame             :  
[11] = item_1               |  
[12] = item_2               |  
[13] = resetbutton          |
[14] = advicebutton         : 
[15] = aboutitem            |
[16] = homebutton           |

=====================================================================
                             
                                                                 item

➥ manage random spawn items

function call . . .

random_item1 >>> item()() 
random_item2 >>> item()()()
random_item3 >>> item()()()()
random_item4 >>> item()()()()()
random_item5 >>> item()()()()()()
random_item6 >>> item()()()()()()()
random_item7 >>> item()()()()()()()()
random_item8 >>> item()()()()()()()()()

item() = item revolves around itself

=====================================================================

                                                             playgame
➥ manage game play
- show seconds
- show score @Real-Time
- stop music of @global

---------------------------------------------------------------------

                                                              endgame
➥ manage game ending
- Show winner and loser scores
- play music of game score page

---------------------------------------------------------------------

                                                        on_mouse_down
➥ manage clicks and reset settings
- reset time
- reset score
- reset character
- reset item
sounds.powerful is music.powerful or .wav is .mp3

---------------------------------------------------------------------

                                                                score
➥ manage points
- score +,- @Real-Time
- random items

---------------------------------------------------------------------

                                                               update
➥ manage character movements
- animation character
- animation item

---------------------------------------------------------------------

                                                                 draw
➥ manage screen display
- home page 
- game play page
- score page

---------------------------------------------------------------------
'''


