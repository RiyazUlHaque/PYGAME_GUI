import pygame as pg
import time
import random as rnd

x = pg.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
dgreen = (0,150,0)
blue = (0,0,255)
pink = (255,128,180)
dpink = (180,0,100)
orchid = (155,50,204)
sblue=(0,191,255)
dsblue = (30,4,200)
yellow = (255,255,0)
gold = (255,215,0)
orange = (255,127,0)
brown = (185,122,87)
clock = pg.time.Clock()
clock.tick(10)
DspH = 600
DspW = 1160
LC = pg.mixer.Sound('roundclear.wav')
horn = pg.mixer.Sound('horn.wav')
game_won = pg.mixer.Sound('roundclear.wav')
busS = pg.mixer.Sound('bus.wav')
startS = pg.mixer.Sound('gamesound1.wav')
pg.mixer.music.load('stealth2wav.wav')
pg.mixer.music.play(-1)
game_overS = pg.mixer.Sound('gameoverwav.wav')
pauseS = pg.mixer.Sound('pause2.wav')

TF = pg.mixer.Sound('tractorfollowingwav.wav')
pg.mixer.Sound.set_volume(TF,0.5)
#gpic = pg.image.load('faculty1.png')
tcr1 = pg.image.load("tcr1.png")
bg1 = pg.image.load("bg1.png")
bg2 = pg.image.load("bg2.png")
ex = pg.image.load("ex.png")
fcS = pg.image.load("fcS.png")
tr1 = pg.image.load("tr1.png")
tr2 = pg.image.load("tr2.png")
fac1 = pg.image.load("fac1.png")
fac2=  pg.image.load("fac2.png")
guard = pg.image.load("guard.png")
boyA = pg.image.load("boy1.png")
boyB = pg.image.load("boy2.png")
sboy1 = pg.image.load("sboy1.png")
sboy2 = pg.image.load("sboy2.png")
fc1 = pg.image.load("fc1.png")
fc2 = pg.image.load("fc2.png")
bus3 = pg.image.load('bus3.png')
bus2 = pg.image.load('bus2.png')
arrow = pg.image.load('arrow.png')
arrow2 = pg.image.load('arrow2.png')
arrow3 = pg.image.load('arrow3.png')
bus = pg.image.load('bus.png')
lobbyS = pg.image.load('lobby.png')
lobbyS2 = pg.image.load('lobby2.png')
car1 = pg.image.load('car3.png')
car2 = pg.image.load('car4.png')
car3 = pg.image.load('car2.png')
Hshield = pg.image.load('shelter.png')
Vshield = pg.image.load('shelter2.png')
block = pg.image.load('block.png')
gd = pg.display.set_mode((DspW,DspH))
stree = pg.image.load('treesmall.png')
tree2 = pg.image.load('tree2.png')
scircle = pg.image.load('circlesmall.png')
basket1 = pg.image.load('basket1.png')
basket2 = pg.image.load('basket2.png')
tree = pg.image.load('tree.png')
shelter = pg.image.load('circle.png')
loop1 = pg.image.load('game1.png')
loop2 = pg.image.load('game2.png')
loop3 = pg.image.load('gameC.png')
loop4 = pg.image.load('gameD.png')
loop5 = pg.image.load('gameE.png')
loop6 = pg.image.load('gameF.png')
loop7 = pg.image.load('gameG.png')
loop8 = pg.image.load('gameH.png')
loop9 = pg.image.load('gameI.png')
loop10 = pg.image.load('gameJ.png')
loop11 = pg.image.load('gameK.png')
loop12 = pg.image.load('gameL.png')
loop13 = pg.image.load('gameM.png')
loop14 = pg.image.load('gameN.png')
loop15 = pg.image.load('gameP.png')
loop16 = pg.image.load('gameO.png')
loop17 = pg.image.load('gameQ.png')
loop18 = pg.image.load('ricco.png')



def msg_to_scrn2(msg,msg2 = ' ',msg3 ='',msg4 = '',msg5 = '',color= black,W=10,H=10,y_disp= 0,x_disp = 0,Font= 'comicsansms',Size=25):
    
    #pg.mixer.Sound.play(popup)
    font = pg.font.SysFont(Font,Size)
    textS = font.render(msg,True,color)
    textrect = textS.get_rect()
    textrect.center = ((DspW/2)+x_disp),((DspH/2)+y_disp)
    textS2 = font.render(msg2,True,color)
    textrect2 = textS.get_rect()
    textrect2.center = ((DspW/2)+x_disp),((DspH/2)+y_disp+40)
    textS3 = font.render(msg3,True,color)
    textrect3 = textS.get_rect()
    textrect3.center = ((DspW/2)+x_disp),((DspH/2)+y_disp+80)
    textS4 = font.render(msg4,True,color)
    textrect4 = textS.get_rect()
    textrect4.center = ((DspW/2)+x_disp),((DspH/2)+y_disp+120)
    textS5 = font.render(msg5,True,color)
    textrect5 = textS.get_rect()
    textrect5.center = ((DspW/2)+x_disp),((DspH/2)+y_disp+160)
    pg.draw.rect(gd,black,(((DspW/2)-5+x_disp),((DspH/2)-5+y_disp),W+10,H+10))
    pg.draw.rect(gd,white,(((DspW/2)+x_disp),((DspH/2)+y_disp),W,H))
    gd.blit(textS,(((DspW/2)+x_disp+10),((DspH/2)+y_disp+10)))
    gd.blit(textS2,(((DspW/2)+x_disp+10),((DspH/2)+y_disp+40)))
    gd.blit(textS3,(((DspW/2)+x_disp+10),((DspH/2)+y_disp+70)))
    gd.blit(textS4,(((DspW/2)+x_disp+10),((DspH/2)+y_disp+100)))
    gd.blit(textS5,(((DspW/2)+x_disp+10),((DspH/2)+y_disp+130)))

def msg_to_scrn(msg,color,y_disp= 0,x_disp = 0,Font= 'Arial',Size=25):
    font = pg.font.SysFont(Font,Size)
    
    textS = font.render(msg,True,color)
    textrect = textS.get_rect()
    textrect.center = ((DspW/2)+x_disp),((DspH/2)+y_disp)
    scrn_txt = font.render(msg,True,color)
    gd.blit(textS,textrect)

def pause(a = "music"):
    pg.mixer.music.pause()
    pg.mixer.Sound.stop(TF)
    pg.mixer.Sound.stop(startS)
    pg.mixer.Sound.play(pauseS)
    pause = True
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    if a=="TF":
                        pg.mixer.Sound.play(TF)
                    if a=="music":
                        pg.mixer.music.play(-1)
                    if a=="startS":
                        pg.mixer.Sound.play(startS)
                    pause = False
                if event.key == pg.K_q:
                    quit()
        gd.fill(black)
        msg_to_scrn('PAUSED',red,-100,Font = 'comicsansms',Size =100 )
        msg_to_scrn('press R to continue and Q to quit',blue,Size = 50)
        pg.display.update()

def text_on_button(msg,color,rectX,rectY,rectW,rectH,Font= 'Arial',Size=25):
    font = pg.font.SysFont(Font,Size)
    textS = font.render(msg,True,color)

    textrect = textS.get_rect()
    textrect.center = (rectX + rectW/2),(rectY + rectH/2)
    gd.blit(textS,textrect)
    
def button(bX,bY,bW,bH,inactive_color,active_color,text,text_acolor,text_incolor,Font='Arial',Size=25,action = None):
    cur = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    
    if bX < cur[0] < bX+bW and bY < cur[1] < bY+bH:
        pg.draw.rect(gd,active_color,[bX-10,bY-10,bW+20,bH+20])
        text_on_button(text,text_acolor,bX,bY,bW,bH,Font,Size+10)
        if click[0] == 1:
            if action== 'quit':
                  quit()
            if action == 'play':
                
                gameloop(863,565,0,0,0,0,0,0,)
                pg.mixer.Sound.stop(startS)
            if action == 'play':
                pass
                
            if action == 'controls':
                controls()
            if action == 'main':
                start()
            
    else:
        pg.draw.rect(gd,inactive_color,[bX,bY,bW,bH])
        text_on_button(text,text_incolor,bX,bY,bW,bH,Font,Size)
def controls():
    gcont = True
    click = pg.mouse.get_pressed()
    while gcont:
        gd.fill(black)
        msg_to_scrn('Instructions',blue,-150,Font = 'Algerian',Size= 100)
        msg_to_scrn('Arrow Keys For Movement Left,Right,Up,Down',red,Font='comicsansms',Size = 35)
        msg_to_scrn( 'C to Crouch ',red,50,Font='comicsansms',Size = 35)
        msg_to_scrn('Protect Yourself behind Buses and Cars',red,100,Font='comicsansms',Size = 35)
        msg_to_scrn('Pause: P                    Continue: SPACE  ',red,150,Font='comicsansms',Size = 35)
        gcont = False 
        pg.display.update()
        clock.tick(15)
        
def start():
    pg.mixer.music.stop()
    pg.mixer.Sound.play(startS)
    intro = True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    Exit = True
                    pg.quit()
                    quit()
        gd.fill(black)
        msg_to_scrn('Escaping From ARYA',blue,-150,Font = 'Algerian',Size= 100)
        msg_to_scrn('It is a Stealth type game',red,Font = 'comicsansms',Size = 35)
        msg_to_scrn('Help RIZ to go outside from college',red,50,Font = 'comicsansms',Size = 35)
        msg_to_scrn('Avoid Faculties, Avoid Wardens',red,100,Font = 'comicsansms',Size = 35)
        msg_to_scrn( 'All The Best',red,150,Font = 'comicsansms',Size = 35)

        button(200,500,130,50,pink,dpink,'Play',blue,sblue, 'comicsansms',35,'play')
        button(460,500,220,50,sblue,dsblue,'Instruction',red,pink, 'comicsansms',35,'controls')
        button(800,500,130,50,yellow,orange,'Quit',green,dgreen, 'comicsansms',35,'quit')
        
        
        #msg_to_scrn('Press S to start',green,100,Size = 40)    
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    game_loop()
                    intro = False
                
        pg.display.update()
      
def game_over(color= red,text='You are spotted, Dont try to go too close to them.',text_color= brown,Size=25,Font='comicsansms',ydisp=0,xdisp=0,go = "no",by = 'f'):
    pg.mixer.music.stop()
    pg.mixer.Sound.stop(TF)
    pg.mixer.Sound.stop(startS)
    if by=="f":
        gd.blit(gpic,(-200,-100))
    go = True
    while go:
        pg.mixer.Sound.play(game_overS)
        go = False
    Font = 'comicsansms'
    Size = 40
    msg_to_scrn("Game Over",red,xdisp,Font="comicsansms",Size= 70)
    #msg_to_scrn(text,black,ydisp+50,xdisp,Font,Size+4)
    msg_to_scrn(text,blue,ydisp+50,xdisp,Font,Size+4)
    
    msg_to_scrn('Press P to play again',red,ydisp+150,xdisp,Font,Size)
    msg_to_scrn('Press Q to quit',red,ydisp+200,xdisp,Font,Size)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q: 
                pg.quit()
                quit()
            if event.key == pg.K_p:
                pg.mixer.Sound.stop(game_overS)
                pg.mixer.music.play(-1)
                gameloop(900,5600,0,0,0,0,0,0)

def won():
    gd.fill(pink)
    msg_to_scrn("Congrates",red,-100,Font="comicsansms",Size= 100)
    msg_to_scrn('You Won',yellow,0,Font='comicsansms',Size = 70)
    msg_to_scrn('You finally make RIZ to escape from college :)',yellow,50,Font ='comicsansms' ,Size = 50)
    msg_to_scrn('Press P to play again',yellow,+150)
    msg_to_scrn('Press Q to quit',yellow,+200)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                pg.quit()
                quit()
            if event.key == pg.K_p:
                pg.mixer.Sound.stop(LC)
                gameloop(500,800,0,0,0,0,0,0)
   
def msg_box(X,Y,msg,W,H,font = 'Arial',size= 15):
    gd.fill(white,rect=[X,Y,W,H])
    x = DspW-X
    y = DspH - Y
    msg_to_scrn(msg,black,y+10,x+10,font,size)

def gameloop18():
    pg.mixer.Sound.stop(startS)
    pg.mixer.music.stop()
    game = True
    j = 0
    i = 0
    meX_chng = 0
    meY_chng = 0
    a = 1
    boy = boyA
    o = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = [j for j in range(650,1000)]
        Yib1= [i for i in range(212,DspH+100)]
        Yib2= [i for i in range(-300,212)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        g = 1
        f= 0
        h = 1
        i = 0
        e = 0
        k = 0
        w = 1
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            gd.blit(loop18,(0,0))
            if e==1:
                o +=1
            if o%10==0:
                fcc = fc1
                boy = pg.transform.rotate(boyA,0)
            if o%20==0:
                boy = pg.transform.rotate(boyB,0)
            if f == 0:
                gd.blit(boy,(Xi[0],270))
            if h == 0:
               gd.blit(bus3,(945,Yib1[-k]))
            
            if a ==1:
                if g!= 0:
                    pg.mixer.Sound.play(busS)
                    gd.blit(bus3,(945,Yib1[-i]))
                    i +=2
                    if i >484:
                        g = 0
                        f = 1
                        h = 0
                        e = 1
                if e ==1:
                    pg.mixer.Sound.stop(busS)
                    pg.mixer.Sound.play(horn)
                    gd.blit(boy,(Xi[j],270))
                    j +=2
                    if j>320:
                        e = 0
                        h = 1
                if j>320:
                    pg.mixer.Sound.stop(horn)
                    gd.blit(bus3,(945,Yib2[-k]))
                    k +=2
                    if k>50 and k<100:
                        pg.mixer.Sound.play(game_won)
                    if Yib2[-k] <-200:
                        pg.mixer.Sound.play(LC)
                        a = 0
                        w = 0
            if w ==0:
                won()
        
            pg.display.update()
def gameloop17(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue,a=0):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    bgr1 = pg.transform.rotate(bg1,270)
    bgr2 = pg.transform.rotate(bg1,270)
    boy = boy1
    angle = 270
    angle1 = 270
    fcc = fc1
    fcr = fcc
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = [j for j in range(434,848)]
        Xib = [j for j in range(434,848)]
        Yi = [i for i in range(40,118)]
        Yib= [i for i in range(40,118)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        g = 1
        i = 0
        e = 1
        h = True
        enter = False
        radius = 7
        while fc:
            
             
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop17,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop17,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            if g!=0 and a==1:
                o +=1
                
            if o%10==0:
                bgr1 = pg.transform.rotate(bg1,angle1)
                bgr2 = pg.transform.rotate(bg2,angle)
            if o%20==0:
                bgr1 = pg.transform.rotate(bg2,angle1)
                bgr2 = pg.transform.rotate(bg1,angle)
            if e== 1:
                gd.blit(bgr1,(Xi[1]-50,Yi[1]-50))
                gd.blit(bgr2,(Xib[-1]-50,Yib[1]-50))
            if g ==0:
                angle1=  270
                angle  = 270
                gd.blit(bgr1,(Xi[202]-80,Yi[-1]-50))
                gd.blit(bgr2,(Xib[202]-20,Yib[-1]-50))
            if a==1:
                
                if e==1:
                    pg.mixer.Sound.stop(startS)
                    pg.mixer.music.play(-1)
                    e = 0
                if Yi[i] <115 or  Yib[i] <115:
                    gd.blit(bgr1,(Xi[1]-50,Yi[i]-50))
                    gd.blit(bgr2,(Xib[-1]-50,Yib[i]-50))
                    
                    i = i+1
                
                    
                if  Yi[i] > 114 and g ==1 or Yib[i]>114 and g == 1:
                    gd.blit(bgr1,(Xi[j]-50,Yi[i]-50))
                    gd.blit(bgr2,(Xib[-j]-50,Yib[i]-50))
                    angle = 180
                    angle1 = 0 
                    j = j+2
                    if  Xi[j]>602:
                        g = 0
                        o = 10
                        
            if meX>339 and meX<830:
                if meY<158:
                    h = False
                    meY = 159
            if h == False and g ==0:
                if enter ==False:
                    msg_to_scrn2('Guards: Go to your class Dont try to go outside of college',
                                                'Me:Yeah Sure -_- ','There must be an open door try the H-hostel one',
                                                'I have to Face Sunil sir now','                         press SPACE to continue',black,420,150,-100,0,Size =15)
                if enter == True:
                    h = True
                    enter = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)
            
            if meX>-50 and meX<50:
                if meY>520:
                    meY = 520
            if meY>410 and meY<540:
                if meX>35 and meX<70:
                    meX = 35
            if meX>50 and meX<910:
                if meY>410 and meY<420:
                    meY = 410
            if meY>410 and meY<DspH+50:
                if meX>900 and meX<911:
                    meX = 911
            if meX>-50 and meX<420:
                if meY<170 and meY>145:
                    meY = 170
            if meY>-50 and meY<170:
                if meX>415 and meX<425:
                    meX = 425
##            m = (170 - 0)/(425-415)
##            if meY == m*meX:
##                meX = 800
                
            if meY<40:
                meY = 40
            if meX>824:
                if meY>-50 and meY<370:
                    meX = 824
                if meY>365 and meY<380:
                    meY = 380
            if meY<159:
                meY = 159
            if meY<160:
                a =1
            ##Function call
            if a ==1:
                if meX<4:
                    meY = rnd.randint(173,399)
                    gameloop16b(meX+DspW-50,meY,-DspW,0,10,0,0,-10)
            if meX<4:
                meY = rnd.randint(173,399)
                gameloop16(meX+DspW-50,meY,-DspW,0,10,0,0,-10)
            if meY>DspH-4:
                meX = rnd.randint(902,1048)
                gameloop13(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if h == False:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop16b(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = 265
        Yi = [i for i in range(0,DspH)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        e = True
        enter = False
        i = 0
        radius = 7
        while fc:
            
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop16,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop16,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            
            if meX<800:
                c = 1
                meX = 100000
                if meX>DspW-10:
                    meX = DspW-10
                if meX<10:
                    meX = 10
                
            gd.blit(fcS,(590,290))
            gd.blit(pg.transform.rotate(fcS,135),(535,263))
            gd.blit(pg.transform.rotate(fcS,215),(535,320))

            if meX==994:
                meX = 1002
            if meX<1000 and meX>995:
                    e = False
                    meX = 992
            if e == False:
                if enter ==False:
                    msg_to_scrn2('Oh god!, From Where these faculties have come',
                                                'I have to find some other way','                         press SPACE to continue','','',
                                                black,400,100,150,-400,Size =15)
                if enter == True:
                    e = True
                    enter = False
            
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meX>DspW-10:
                    meX = DspW-10
    
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)  
            if meY<165:
                 if meX>-50 and meX<1065:
                     meY = 165
            if meY>-50 and meY<165:
                if meX>1040 and meX<1070:
                    meX = 1070
            
            if meX>-50 and meX<150:
                if meY>400 and meY<550:
                    meY = 405
            if meX>905 and meX<DspW+50:
                if meY>400 and meY<550:
                    meY = 405
            if meY<10:
                meY = 10
            if meY>400 and meY<535:
                if meX>130 and meX<160:
                    meX = 160
                if meX>895 and meX<915:
                    meX = 895
            if meX>130 and meX<935:
                if meY>510 and meY<534:
                    meY = 510
            ##"Function calling"

            if meX>DspW-4:
                meY = rnd.randint(173,400)
                gameloop17(meX-DspW+50, meY,DspW,0,-10,0,0,-10,a=1)
            if e == False or c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop16(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            if game == True:
                pg.mixer.Sound.play(startS)
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop16,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop16,(0,0))
            gd.blit(ldka,(meX-25,meY-25))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)   
            if meY<165:
                 if meX>-50 and meX<1065:
                     meY = 165
            if meY>-50 and meY<165:
                if meX>1040 and meX<1070:
                    meX = 1070
            
            if meX>-50 and meX<150:
                if meY>400 and meY<550:
                    meY = 405
            if meX>905 and meX<DspW+50:
                if meY>400 and meY<550:
                    meY = 405
            if meY<10:
                meY = 10
            if meY>400 and meY<535:
                if meX>130 and meX<160:
                    meX = 160
                if meX>895 and meX<915:
                    meX = 895
            if meX>130 and meX<935:
                if meY>510 and meY<534:
                    meY = 510
            ##"Function calling"

            if meX<4:
                gameloop15(meX+DspW-50, meY,-DspW,0,10,0,0,-10)
            if meX>DspW-4:
                meY = rnd.randint(173,400)
                gameloop17(meX-DspW+50, meY,DspW,0,-10,0,0,-10)
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop15(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = 265
        Yi = [i for i in range(0,DspH)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            if game == True:
                pg.mixer.Sound.play(startS)
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop15,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop15,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            gd.blit(lobbyS2,(480,263))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0) 
            if meY<175:
                if meX<DspW+50:
                    meY = 175
            if meY>0:
                if meX<207:
                    meX = 207
            if meY>425:
                if meX>330 and meX<335:
                    meX = 330
            if meY>415:
                if meX>330 and meX<DspW+50:
                    meY = 415
            ##Function calling
            if meY> DspH-4:
                gameloop14(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if meX>DspW-4:
                gameloop16(meX-DspW+50,meY,DspW,0,-10,0,0,-10)
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop14(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    fac = fac1
    direction = "up"
    boy = boy1
    angle1 = 270
    fcc = fc1
    fcr = fcc
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    meX_chng = 0
    meY_chng = 0
    a = 2
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = 265
        Yi = [i for i in range(0,DspH)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        e = True
        enter =  False
        radius = 7
        while fc:
            if game == True:
                pg.mixer.Sound.play(startS)
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop14,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop14,(0,0))
            o +=1
            if o%10==0:
                fcc = fc1
                fcr = pg.transform.rotate(fc1,angle1)
            if o%20==0:
                fcc = fc2
                fcr = pg.transform.rotate(fc2,angle1)
            if a==1:
                gd.blit(fcr,(Xi,Yi[i]))
                if meY<Yi[i]+30 and meY>Yi[i]-30:
                    if meX>460 and meX<480:
                        if meY>367 and meY<510 and croch == True:
                             c = 0
                    else:
                        c = 1
                        meX = -100000
                        if meY<10:
                            meY = 10
                        if meY>DspH-10:
                            meY = DspH-10
                    
                if i == 2:
                    b = 2
                if i>DspH-10:
                    i = -1
                    a = 0
                i +=b
            gd.blit(ldka,(meX-25,meY-25))
            gd.blit(lobbyS,(334,0))
            gd.blit(car1,(350,475))
            gd.blit(car2,(350,425))
            gd.blit(car3,(355,355))
            if meY == 528:
                meY = 538
            if meX>0 and meX<489:
                if meY<536 and meY>530:
                    meY  =526
                    if a!=0:
                        e = False
                        b = 0
            if e== False:
                if enter ==  False:
                    msg_to_scrn2('A faculty is comming here','Find a place to hide','Those cars are looking beautiful',
                                                '            press SPACE to continue','',black,250,150,+50,-400,Size = 15)
                    
                if enter == True:
                    e = True
                    b = 2
                    enter = False
                    
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meX>DspW-10:
                    meX = DspW-10
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)
            if meY<10:
                if meX<210 or meX>481:
                    meY = 10
            if meY>0and meY<DspH+50:
                if meX>465:
                    meX = 465
            if meX>415 and meX<443:
                if meY>330 and meY<340:
                    meY = 340
                if meY<330 and meY>320:
                    meY = 320
            if meX>345 and meX<371:
                if meY>330 and meY<340:
                    meY = 340
                if meY<330 and meY>320:
                    meY = 320
            if meX<207:
                meX = 207
            if meX>345 and meX<459:
                if meY>518 and meY<522:
                    meY = 522
                if meY>479 and meY<490:
                    meY= 479
                if meY>463 and meY<468:
                    meY = 468
                if meY>431 and meY<438:
                    meY = 431
                if meY>408 and meY<416:
                    meY = 416
                if meY>360 and meY<370:
                    meY = 360
            if meX>350 and meX<367:
                if meY>355 and meY<415:
                    meX = 350
                if meY>433 and meY<468:
                    meX = 350
                if meY>480 and meY<525:
                    meX = 350
            if meX>450 and meX<465:
                if meY>355 and meY<415:
                    meX = 465
                if meY>433 and meY<468:
                    meX = 465
                if meY>480 and meY<525:
                    meX = 465
            if a ==2:
                if meY<550 and meY>540:
                    a =1
            ##"Calling function"
            if meX>206 and meX<490:
                if meY<4:
                    meX = rnd.randint(205,330)
                    gameloop15(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
                if meY>DspH-4:
                    gameloop11(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if e == False or c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop13(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue,a=1):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop13,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop13,(0,0))
            gd.blit(ldka,(meX-25,meY-25))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)     
                    
                    
            if meY<10:
                if meX<905 or meX>1045:
                    meY = 10
            if meY >-50  and meY<518:
                if meX>890 and meX<904:
                    meX= 904
                if meX>53 and meX<64:
                    meX = 53
            if meX>1045 and meX<1049:
                if meY>-50 and meY<267:
                    meX = 1045
                if meY>275 and meY<540:
                    meX = 1045
            if meX>1045 and meX<DspW+100:
                if meY>530 and meY<540:
                    meY = 540
                if meY>272 and meY<277:
                    meY = 272
                if meY>258 and meY<263:
                    meY = 263
            if meX>55 and meX<906:
                if meY>505 and meY<515:
                    meY = 515
            if meY>DspH-30:
                if meX>1048 or meX<905:
                    meY = DspH-30
            if meX >DspW-30:
                meX = DspW-30
            ##"Function calling"
            if meY>510:
                if meX<59:
                    gameloop9b(meX-50+DspW-50,meY-DspH+50,-DspW,0,10,0,0,-10)
            if meX>895 and meX<1051:
                if meY>DspH-10:
                    meY = DspH-10
                    #gameloop10(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if meY<4:
                gameloop17(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop12(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        s = 0
        radius = 7
        while fc:
            
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop12,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop12,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            
            gd.blit(block,(71,87))
            gd.blit(Hshield,(148,87))
            gd.blit(Vshield,(71,155))
            gd.blit(tree,(780,160))
            gd.blit(tree,(780,273))
            gd.blit(tree,(780,415))
            gd.blit(tree,(140,185))
            gd.blit(tree,(140,360))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key==pg.K_p:
                        pause()
                        
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0) 
            if meY>148 and meY<DspH+100:
                if meX <822 and meX>810:
                    meX = 822
                if meX>124 and meX<135:
                    meX = 124
            if meX>124 and meX<822:
                if meY>150:
                    meY =150
            if meY>0:
                if meX>917:
                    meX = 917
                if meX<80:
                    meX = 80
            if meX>0:
                if meY>0 and meY<127:
                    meY = 127
            if meY>285 and meY<405:
                if meX>874 and meX<880:
                    meX = 874
                if meX>880 and meX<885:
                    meX = 885
            if meX>874 and meX<929:
                if meY>318 and meY<368:
                    if s == 0:
                        radius = 9
                    else:
                        radius = 7
            if meX<874 or meX>929 or meY<318 or meY>368:
                if s == 0:
                    radius = 7
                else:
                    radius = 5
            ## function calling
            if meX>819 and meX<930:
                if meY>DspH-4:
                    gameloop9b(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if meX>70 and meX<125:
                if meY>DspH-4:
                    gameloop9b(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop11(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        e = True
        enter = False
        s = 0
        radius = 7
        while fc:
            if game == True:
                pg.mixer.Sound.play(startS)
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop11,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop11,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            if meX>0 and meX<489:
                if meY>DspH-12:
                    e = False
            if e== False:
                if enter ==  False:
                    msg_to_scrn2('Last time i found Sunil sir there','So its not better to go there',
                                                '            press SPACE to continue','','',black,250,100,+50,-400,Size = 15)
                    meY  =DspH-16
                if enter == True:
                    e = True
                    enter = False
            gd.blit(stree,(539,500))
            gd.blit(stree,(771,500))
            gd.blit(stree,(1004,505))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)            

            if meX <205:
                meX = 205
            if meY>DspH-10:
                meY = DspH-10
            if meX>497 and meX<DspW+50:
                if meY>515:
                    meY = 515
            if meY>515 and meY<DspH+50:
                if meX>490 and meX<497:
                    meX = 490
            if meX>474 and meX<DspW+50:
                if meY>405 and meY<411:
                    meY = 411
            if meY>-50 and meY<411:
                if meX>470 and meX<475:
                    meX = 470
            ##"calling functions"
            if meX>200 and meX<590:
                if meY<4:
                    gameloop14(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if meY>410 and meY<518:
                if meX>DspW-4:
                    gameloop9(meX-DspW+50,meY-DspH+50,DspW,0,-10,0,0,-10)
            if e == False:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop11b(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        s = 0
        e = True
        enter =  False
        radius = 7
        while fc:
            
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop11,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop11,(0,0))
            
            gd.blit(ldka,(meX-25,meY-25))
            gd.blit(stree,(539,500))
            gd.blit(stree,(771,500))
            gd.blit(stree,(1004,505))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter =  True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)    

            if meX <205:
                meX = 205
            
            if meX>497 and meX<DspW+50:
                if meY>515:
                    meY = 515
            if meY>515 and meY<DspH+50:
                if meX>490 and meX<497:
                    meX = 490
            if meX>474 and meX<DspW+50:
                if meY>405 and meY<411:
                    meY = 411
            if meY>-50 and meY<411:
                if meX>470 and meX<475:
                    meX = 470
            ##"calling functions"
            if meX>200 and meX<590:
                if meY>DspH-4:
                    meX = rnd.randint(215,385)
                    gameloop8b(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
                if meY<4:
                    e = False
                    meY = 6 
                if e == False:
                    if enter ==False:
                        msg_to_scrn2('There is no sense to go there','Guards will not allow me go outside',
                                                    'Lets try the bottom one','                         press SPACE to continue','',
                                                    black,400,150,150,-100,Size =15)
                    if enter == True:
                        e = True
                        enter = False
                        meY = 6
            if meY>410 and meY<518:
                if meX>DspW-4:
                    gameloop9b(meX-DspW+50,meY-DspH+50,DspW,0,-10,0,0,-10)
            if e == False:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop10(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        e = True
        enter = False
        i = 0
        radius = 7
        while fc:
            if game == True:
                pg.mixer.Sound.play(startS)
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop10,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop10,(0,0))
            
            if a==1:
                gd.blit(pg.transform.rotate(guard,270),(370,10))
                if meX>220 and meX<360:
                    c = 1
                    meX = -100000
                    if meX>DspW-10:
                        meX = DspW-10
                    if meX<10:
                        meX = 10
            gd.blit(ldka,(meX-25,meY-50))
            if meX==122:
                    meX = 118
            if meX>119 and meX<122:
                e = False
            if e== False:
                if enter == False:
                    msg_to_scrn2('Wait! Warden is sitting here','Find another way to continue',
                                                '                   press SPACE to continue','','',black,250,100,-200,-150,Size = 15)
                    meX = 124
                
                if  enter == True:
                    e= True
                    enter =  False
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meX>DspW-10:
                    meY = DspW-10
        
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)          
            if meX> 10 and meX<60:
                a = 1
            if meY<40:
                meY = 40
            if meY > 48:
                meY = 48
            if meX >DspW-30:
                meX = DspW-30
            ##"calling function"
            if meY>5 and meY<50:
                if meX<4:
                    meY = rnd.randint(28,57)
                    gameloop9(meX+DspW-50,meY,-DspW,0,10,0,0,-10)
            if meX>895 and meX<1051:
                if meY<4:
                    gameloop13(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if e == False or c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop9(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"    
    j = 0
    i = 0
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        e = True
        enter = False
        i = 0
        radius = 7
        while fc:
            if game== True:
                pg.mixer.Sound.play(startS)
            pg.mixer.Sound.play(startS)
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop9,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            
            
            gd.blit(loop9,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            if meX>110 and meX<350:
                if meY==524:
                    meY = 536
                if meY == 174:
                    meY = 166
                if meY>525 and meY<535:
                    e = False
                    meY = 522
                    
                if meY>169 and meY<174:
                    e = False
                    meY = 178
            if e == False:
                if enter == False:
                    msg_to_scrn2('Beware! Ex is sitting here','Its not good to go from here',
                                                'Find another way to go further','             press SPACE to continue','',
                                                black,300,150,-50,-100,Size = 15)
                    
                if enter == True:
                    e = True
                    enter = False
            if a==1:
                gd.blit(ex,(55,414))
                if meY>250 and meY<500:
                    if meX>60 and meX<360:
                        c = 1
                        meX = -100000
                        if meY<10:
                            meY = 10
                        if meY>DspH-10:
                            meY = DspH-10
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meX>DspW-10:
                    meY = DspW-10
        

            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)
            if meY<10:
                if meX<862 and meX>173 or meX>979 or meX<95:
                    meY = 10
            if meY<10:
                meY = 10
            if meX<30:
                if meY<0 or meY>50:
                    meX = 30
            if meY > DspH-10:
                if meX>270 and meX<980:
                    meY = DspH-10
            if meX >DspW-30:
                if meY<10 or meY>57:
                    meX = DspW-30
            if meY<DspH+50 and meY>52:
                if meX>974 and meX<979:
                    meX = 979
            if meY>50 and meY<60:
                if meX>269 and meX<979:
                    meY = 50
                if meX>1080 and meX<DspW+50:
                    meY = 50
                if meX>-50 and meX<65:
                    meY = 50
            if meX>47 and meX<65:
                if meY>50 and meY<109:
                    meX = 65
                if meY>295 and meY<505:
                    meX = 65
            if meX>58 and meX<147:
                if meY>95 and meY<100:
                    meY = 95
            if meY>95 and meY<171:
                if meX>135 and meX<145:
                    meX = 145
            if meX>135 and meX<170:
                if meY>165 and meY<173:
                    meY = 165
            if meY>165 and meY<280:
                if meX>165 and meX<170:
                    meX= 170
            if meX<170 and meX>110:
                if meY<281 and meY>275:
                    meY = 281
            if meX>120 and meX<125:       
                if meY>235 and meY<340:
                    meX = 125
                if meY>500 and meY<DspH+50:
                    meX = 125
            if meX<125 and meX>10:
                if meY>500 and meY<506:
                    meY = 500
                if meY>329 and meY<339:
                    meY = 339
            if meX<85:
                if meY>385 and meY<450:
                    meX = 85
                if meY>450 and meY<455:
                    meY = 455
                if meY>381 and meY<390:
                    meY = 381
            if meY>300 and meY<537:
                if meX>155 and meX<159:
                    meX = 155
                if meX>284 and meX<290:
                    meX = 290
            if meX>155 and meX<290:
                if meY>534 and meY<540:
                    meY = 540
                if meY>298 and meY<303:
                    meY = 298
            if meY>50 and meY<215:
                if meX>265 and meX<275:
                    meX = 265
            if meX>265 and meX<350:
                if meY>205 and meY<215:
                    meY = 215
            if meY>200 and meY<545:
                if meX>332 and meX<337:
                    meX = 332
            if meX<335 and meX>283:
                if meY>545 and meY<555:
                    meY = 545
            if meY>545:
                if meX>284 and meX<289:
                    meX = 284
            if meY>18:
                if meX<857 and meX>794: 
                    meY = 18
                if meX>442 and meX<779:
                    meY = 18
                if meX>358 and meX<425:
                    meY = 18
            if meY>18 and meY<59:
                if meX>355 and meX<364:
                    meX = 335
                if meX>418 and meX<428:
                    meX = 428
                if meX>440 and meX<450:
                     meX = 440
                if meX>770 and meX<780:
                     meX = 780
                if meX>790 and meX<800:
                     meX = 790
                if meX>855 and meX<865:
                     meX = 856
            if meY>54 and meY<515:
                if meX>1080:
                    meX = 1080
            if meX>1080 and meX<1120:
                if meY>515 and meY<520:
                    meY = 520
                if meY > 553 and meY<559:
                    meY = 553
            if meY>500:
                if meX>1115:
                    meX = 1115
            if meY>555:
                if meX>1085:
                    meX = 1085
            if meY>500 and meY<DspH-10 or meY>100 and meY<110:
                a = 1
            ##"Calling functions"
            if meX>129 and meX<277:
                if meY>DspH-4:
                    gameloop6b(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if meX>980 and meX<1085:
                if meY>DspH-4:
                    gameloop6b(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if meY>0and meY<55:
                if meX>DspW-4:
                    gameloop10(meX-DspW+50,meY,DspW,0,-10,0,0,-10)
            if meY>0 and meY<50:
                if meX<4:
                    meY = rnd.randint(415,515)
                    gameloop11(meX+DspW-50,meY+DspH-50,-DspW,0,10,0,0,-10)
            if meX>840 and meX<990:
                if meY<4:
                    meX = rnd.randint(815,928)
                    gameloop12(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if meX>91 and meX<173:
                if meY<4:
                    meX = rnd.randint(72,120)
                    gameloop12(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if e == False or c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop9b(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    fac = fac1
    direction = "up"
    facr = fac
    boy = boy1
    fcc = fc1
    fcr = fcc
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        o = False
        e = True
        enter = False
        radius = 7
        while fc:
            
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop9,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop9,(0,0))
            gd.blit(fcS,(780,-20))
            gd.blit(pg.transform.rotate(fcS,180),(750,-10))
            if  o == True:
                gd.blit(arrow3,(890,5))

            gd.blit(ldka,(meX-25,meY-25))
            
            if meX==1029:
                meX = 1042
            if meX<1040 and meX>1030:
                if meY>0 and meY<85:
                    e = False
                    meX = 1025
            if e == False:
                if enter ==False:
                    msg_to_scrn2('a couple of faculties are standing here',
                                                'I have to find some other way','                         press SPACE to continue','','',
                                                black,350,100,-200,100,Size =15)
                if enter == True:
                    e = True
                    enter = False
            if meX<820 and meX>370:
                    c = 1
                    meX = -100000
                    if meX>DspW-10:
                        meX = DspW-10
                    if meX<10:
                        meX = 10
                    if meY<10:
                        meY = 10
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meX>DspW-10:
                    meY = DspW-10
        

            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                        o = True
                    if event.key==pg.K_p:
                        pause()
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)
            if meY>DspH-10:
                meY = DspH-10
            
            if meY<10:
                if meX>990 or meX<840 and meX>173 or meX<91:
                    meY = 10
            if meX<30:
                if meY<0 or meY>50:
                    meX = 30
            if meY > DspH-10:
                if meX>270 and meX<980:
                    meY = DspH-10
            if meX >DspW-30:
                if meY<10 or meY>57:
                    meX = DspW-30
            if meY<DspH+50 and meY>52:
                if meX>974 and meX<979:
                    meX = 979
            if meY>50 and meY<60:
                if meX>269 and meX<979:
                    meY = 50
                if meX>1080 and meX<DspW+50:
                    meY = 50
                if meX>-50 and meX<65:
                    meY = 50
            if meX>47 and meX<65:
                if meY>50 and meY<109:
                    meX = 65
                if meY>295 and meY<505:
                    meX = 65
            if meX>58 and meX<147:
                if meY>95 and meY<100:
                    meY = 95
            if meY>95 and meY<171:
                if meX>135 and meX<145:
                    meX = 145
            if meX>135 and meX<170:
                if meY>165 and meY<173:
                    meY = 165
            if meY>165 and meY<280:
                if meX>165 and meX<170:
                    meX= 170
            if meX<170 and meX>110:
                if meY<281 and meY>275:
                    meY = 281
            if meX>120 and meX<125:       
                if meY>235 and meY<340:
                    meX = 125
                if meY>500 and meY<DspH+50:
                    meX = 125
            if meX<125 and meX>10:
                if meY>500 and meY<506:
                    meY = 500
                if meY>329 and meY<339:
                    meY = 339
            if meX<85:
                if meY>385 and meY<450:
                    meX = 85
                if meY>450 and meY<455:
                    meY = 455
                if meY>381 and meY<390:
                    meY = 381
            if meY>300 and meY<537:
                if meX>155 and meX<159:
                    meX = 155
                if meX>284 and meX<290:
                    meX = 290
            if meX>155 and meX<290:
                if meY>534 and meY<540:
                    meY = 540
                if meY>298 and meY<303:
                    meY = 298
            if meY>50 and meY<215:
                if meX>265 and meX<275:
                    meX = 265
            if meX>265 and meX<350:
                if meY>205 and meY<215:
                    meY = 215
            if meY>200 and meY<545:
                if meX>332 and meX<337:
                    meX = 332
            if meX<335 and meX>283:
                if meY>545 and meY<555:
                    meY = 545
            if meY>545:
                if meX>284 and meX<289:
                    meX = 284
            if meY>18:
                if meX<857 and meX>794: 
                    meY = 18
                if meX>442 and meX<779:
                    meY = 18
                if meX>358 and meX<425:
                    meY = 18
            if meY>18 and meY<59:
                if meX>355 and meX<364:
                    meX = 335
                if meX>418 and meX<428:
                    meX = 428
                if meX>440 and meX<450:
                     meX = 440
                if meX>770 and meX<780:
                     meX = 780
                if meX>790 and meX<800:
                     meX = 790
                if meX>855 and meX<865:
                     meX = 856
            if meY>54 and meY<515:
                if meX>1080:
                    meX = 1080
            if meX>1080 and meX<1120:
                if meY>515 and meY<520:
                    meY = 520
                if meY > 553 and meY<559:
                    meY = 553
            if meY>500:
                if meX>1115:
                    meX = 1115
            if meY>555:
                if meX>1085:
                    meX = 1085
            
            ##"Calling functions"
            

            if meY>0and meY<55:
                if meX>DspW-4:
                    gameloop13(meX-DspW+50,meY+DspH-50,DspW,0,-10,0,0,-10)
            if meY>0 and meY<50:
                if meX<4:
                    meY = rnd.randint(415,515)
                    gameloop11b(meX+DspW-50,meY+DspH-50,-DspW,0,10,0,0,-10)
            if meX>840 and meX<990:
                if meY<4:
                    meX = rnd.randint(815,928)
                    gameloop12(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if meX>91 and meX<173:
                if meY<4:
                    meX = rnd.randint(72,120)
                    gameloop12(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if e == False or c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop8(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    angle = 270
    tr = tr1
    tcr = pg.transform.rotate(tr,270)
    pg.mixer.Sound.stop(startS)
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    ex = 300
    ey = 15
    e = True
    enter = False
    speed = 2
    while game:
        
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(100)
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop8,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop8,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            o +=1
            if o%10==0:
                tcr = pg.transform.rotate(tr1,270)
            if o%20==0:
                tcr = pg.transform.rotate(tr2,270)
            if a==1:
                
                pg.mixer.music.stop()
                pg.mixer.Sound.play(TF)
                if ex>meX:
                    ex-= speed
                elif ex<meX:
                    ex += speed
                if ey<meY:
                    ey+= speed
                elif ey>meY:
                     ey -= speed
                gd.blit(tcr,(ex-50,ey-50))
                if ex <meX+25 and ex> meX-25:
                    if ey < meY+25 and ey >meY-25:
                        
                        c = 1
                        meX = 1000
                        ex = 0
                        speed = 0
                        if meY<10:
                            meY = 10
                        if meY>DspH-10:
                            meY = DspH-10
                        
                        
                if meY>DspH-4:
                    gameloop5b(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            gd.blit(tree2,(135,240))
            gd.blit(scircle,(657,170))
            if meX>0:
                if meY<158:
                    e = False
            if e== False:
                if enter ==  False:
                    msg_to_scrn2('He is Sunil Sir','He will try his best to caught You , Run!','If he caught You game will be over',
                                                 'Try to get rid of him','                    press SPACE to continue',
                                                    black,300,200,-150,-50,Size =15)
                    meY = 160
                    speed = 0
                if enter == True:
                    e = True
                    enter = False
                    speed = 2
            if c== 1:
                game_over(red,'Run! Run! Run! Run! ',black,Size=25,Font='Arial',ydisp=0,xdisp=0,go="yes")
                Ychng = 0
                Xchng = 0
                if meY>DspW-10:
                    meY = DspW-10
                if meY<4:
                    meY = 4
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -speed
                        direction = "up"
                        angle = 90
                    if event.key == pg.K_DOWN:
                        meY_chng = speed
                        direction = "down"
                        angle = 270
                    
                    if event.key == pg.K_LEFT:
                        meX_chng = -speed
                        if a!=1:
                            direction = "left"
                        angle = 180
                    if event.key == pg.K_RIGHT :
                        meX_chng = speed
                        if a!=1:
                            direction = "right"
                        angle = 0
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        radius = 5
                        croch = True
                    if event.key ==pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause("TF")
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)           
            if meY<10:
                if meX<215 and meX>391:
                    meY = 10
            if meX <400:
                if meY> 130 and meY<169:
                    a = 1
                    direction = "down"
            if meX<30:
                meX = 30
            if meY > DspH-10:
                if meX>350:
                    meY = DspH-10
            if meX >DspW-30:
                if meY<532:
                    meX = DspW-30
            if meX<DspW+100 and meX>393:
                if meY>522 and meY<530:
                    meY = 530
            if meX<395 and meX>388:
                if meY>308 and meY<525:
                    meX = 388
                if meY>-50 and meY<172:
                    meX = 388
            if meX>388 and meX<742:
                if meY>300 and meY<305:
                    meY = 300
                if meY>97 and meY<170:
                    meY = 170
            if meY> 165 and meY<305:
                if meX>708 and meX<725:
                    meX = 708
            if meX<217 and meX>200:
                if meY<DspH+50 and meY>317:
                     meX = 217
                if meY> -50 and meY<170:
                    meX = 217
                
            if meX>-50 and meX<217:
                if meY>317:
                    meY = 317
                if meY<170:
                    meY = 170
            ##"Calling functions"
            if meY>530 and meY<DspH:
                if meX>DspW-4:
                    gameloop6(meX-DspW+50,meY-DspH+50,DspW,0,-10,0,0,-10)
            if meX>200 and meX<500:
                if meY>DspH-4:
                    meX = 332
                    gameloop5(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
                if meY<4:
                    meX = rnd.randint(230,430)
                    gameloop11(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if e ==  False or c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop8b(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    ex = 300
    ey = 15
    speed = 2
    while game:
        
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        e = True
        enter =  False
        i = 0
        radius = 7
        while fc:
            if game== True:
                pg.mixer.music.stop()
                pg.mixer.Sound.play(startS)
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop8,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop8,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            gd.blit(tcr1,(0,240))
            gd.blit(bus2,(34,180))
            gd.blit(tree2,(135,240))
            gd.blit(scircle,(657,170))
            if meY == 82:
                meY = 68
            if meY>70and meY<80:
                    e = False
                    meY =84 
            if e == False:
                if enter ==False:
                    msg_to_scrn2('Me: Sunil Sir is standing there','i have to be Careful',
                                                'Find your way throughout the gate','                         press SPACE to continue','',
                                                black,350,150,-100,-200,Size =15)
                if enter == True:
                    e = True
                    enter = False
            if meX>0 and meX<170:
                if meY>160 and meY<197 and croch == True:
                    c = 0
                else:
                    c = 1
                    meX = -100000
                    if meX<10:
                        meX = 10
                    if meY<10:
                        meY = 10
                    if meY>DspH-10:
                        meY = DspH-10
            
            if meY>220:
                meY = -100000
                c = 1
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meY>DspW-10:
                    meY = DspW-10
                if meY<4:
                    meY = 4
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                        
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)
            if meX>40 and meX<172:
                if meY>184 and meY<194:
                    meY = 184
                if meY>213 and meY<225:
                    meY  = 225
            if meY>184 and meY<225:
                if meX>166 and meX<175:
                    meX = 175
                if meX>35 and meX<45:
                    meX = 35
            if meY<10:
                if meX<215 and meX>391:
                    meY = 10
            if meX <400:
                if meY> 130 and meY<169:
                    a = 1
            
            if meY > DspH-10:
                if meX>350:
                    meY = DspH-10
            if meX >DspW-30:
                if meY<532:
                    meX = DspW-30
            if meX<DspW+100 and meX>393:
                if meY>522 and meY<530:
                    meY = 530
            if meX<395 and meX>388:
                if meY>308 and meY<525:
                    meX = 388
                if meY>-50 and meY<172:
                    meX = 388
            if meX>388 and meX<742:
                if meY>300 and meY<305:
                    meY = 300
                if meY>97 and meY<170:
                    meY = 170
            if meY> 165 and meY<305:
                if meX>708 and meX<725:
                    meX = 708
            if meX<217 and meX>200:
                if meY<DspH+50 and meY>317:
                     meX = 217
                if meY> -50 and meY<170:
                    meX = 217
            
            if meX>-50 and meX<217:
                if meY>317:
                    meY = 317
                if meY<170:
                    meY = 170
            ##"Calling functions"
            if meX<4:
                gd.fill(white)
                time.sleep(2)
                gameloop18( )
            if meY>530 and meY<DspH:
                if meX>DspW-4:
                    meX = DspW-4
            if meX>200 and meX<500:
                if meY>DspH-4:
                    meY = DspH-4
                if meY<4:
                    meX = rnd.randint(230,430)
                    gameloop11b(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if e == False or c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop7(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    tr = tr1
    tcr = pg.transform.rotate(tr,270)
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    ex = 0
    ey = 0
    speed = 2
    while game:
        pg.mixer.music.stop()
        fc = True
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop7,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop7,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            o +=1
            if o%10==0:
                tcr = pg.transform.rotate(tr1,270)
            if o%20==0:
                tcr = pg.transform.rotate(tr2,270)
            if a==1:
                pg.mixer.Sound.play(TF)
                if ex>meX:
                    ex-= speed
                elif ex<meX:
                    ex += speed
                if ey<meY:
                    ey+= speed
                elif ey>meY:
                     ey -= speed
                gd.blit(tcr,(ex-50,ey-50))
                if ex <meX+2 and ex> meX-2:
                    if ey < meY+2 and ey >meY-2:
                        
                        c = 1
                        meX = -100000
                        if meX<10:
                            meX = 10
                        if meY>DspH-10:
                            meY = DspH-10
            if c== 1:
                game_over(red,'Sooooooo Slow!',black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meY>DspW-10:
                    meY = DspW-10
                if meY<4:
                    meY = 4
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -speed
                        direction = "up"
                        angle = 90
                    if event.key == pg.K_DOWN:
                        meY_chng = speed
                        direction = "down"
                        angle = 270
                    
                    if event.key == pg.K_LEFT:
                        meX_chng = -speed
                        if a!=1:
                            direction = "left"
                        angle = 180
                    if event.key == pg.K_RIGHT :
                        meX_chng = speed
                        if a!=1:
                            direction = "right"
                        angle = 0
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        speed = 1
                        croch = True
                    if event.key ==pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause("TF")
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        speed = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)        
            if meY<10:
                if meX>239:
                    meY = 10
            if meX<10:
                if meY<10 or meY>300:
                    meX = 10
            if meY > DspH-10:
                if meX<95 and meX>355:
                    meY = DspH-10
            if meX >DspW-30:
                meX = DspW-30
            if meX>315 and meX<1070:
                if meY>490 and meY< 500:
                    meY = 500
            if meY>450 and meY<500:
                if meX>315 and meX<320:
                    meX = 315
                if meX>1060 and meX<1070:
                    meX = 1070
            if meX>1065 and meX<DspW+50:
                if meY>470 and meY<490:
                    meY = 490
            if meX>265 and meX<3330:
                if meY>460 and meY<470:
                    meY = 470
            if meY>-50 and meY<490:
                if meX>264 and meX<270:
                    meX = 264

            if meX>10 and meY>10:
                a = 1
                direction = "down"
            ##"function calling"
            if meX>0 and meX<335:
                if meY>DspH-4:
                    gameloop4(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            if meY<10:
                if meX>4 and meY<250:
                    meY = 10
                    #gameloop9(meX+DspW-100,meY+DspH-50,0,-DspH,0,10,-10,0)
            
            if c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop6(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    pg.mixer.Sound.play(TF)
    
    
    game = True
    j = 0
    i = 0
    angle = 270
    tr = tr1
    tcr = pg.transform.rotate(tr,0)
    pg.mixer.Sound.stop(startS)
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    o = 0
    u = 0
    speed = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "right"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    ex = 0
    ey = 0
    speed = 2
    while game:
        
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            pg.mixer.music.stop()
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop6,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop6,(0,0))
            gd.blit(arrow,(1050,112))
            gd.blit(ldka,(meX-25,meY-25))
            
            o +=1
            if o%10==0:
                tcr = pg.transform.rotate(tr1,0)
            if o%20==0:
                tcr = pg.transform.rotate(tr2,0)
            if a==1:
                pg.mixer.Sound.play(startS)
                pg.mixer.Sound.play(TF)
                if ex>meX:
                    ex-= speed
                elif ex<meX:
                    ex += speed
                if ey<meY:
                    ey+= speed
                elif ey>meY:
                     ey -= speed
                gd.blit(tcr,(ex-50,ey-50))
                if ex <meX+2 and ex> meX-2:
                    if ey < meY+2 and ey >meY-2:
                        
                        c = 1
                        meX = -100000
                        if meX>DspW-10:
                            meX = 10
                        if meX<10:
                            meX = 10
                       
                if meY>DspH-4:
                    gameloop5b(meX,meY-DspH+50,0,DspH,0,-10,-10,0)
            gd.blit(tree2,(849,90))
            gd.blit(basket1,(322,94))
            gd.blit(basket2,(325,470))
            if c== 1:
                game_over(red,'Have i Done something Wrong with you! :(',black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meY>DspW-10:
                    meY = DspW-10
                if meY<4:
                    meY = 4
             
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -speed
                        if a!=1:
                            direction = "up"
                        angle = 90
                    if event.key == pg.K_DOWN:
                        meY_chng = speed
                        if a!=1:
                            direction = "down"
                        angle = 270
                    if event.key == pg.K_LEFT:
                        meX_chng = -speed
                        direction = "left"
                        angle = 180
                    if event.key == pg.K_RIGHT :
                        meX_chng = speed
                        direction = "right"
                        angle = 0
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        speed = 1
                        croch = True
                    if event.key ==pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause("TF")
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        speed = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)           
            if meY<10:
                if meX>0 :
                    meY = 10
            if meY > DspH-10:
                meY = DspH-10
            if meX >DspW-10:
                if meY>276:
                    meX = DspW-10
            if meY<DspH+100 and meY>165:
                if meX>922 and meX<932:
                    meX = 932
            if meX>500 and meX<932:
                if meY>164 and meY<168:
                    meY = 164
            if meY>130 and meY<196:
                if meX >75 and meX<79:
                    meX = 75
                if meX>79 and meX<82:
                    meX = 82
            if meY<DspH+100 and meY>130:
                if meX>505 and meX<509:
                    meX = 509
                
                if meX>500 and meX<504:
                    meX = 500
            if meX>335 and meX<348:
                if meY>215 and meY<218:
                    meY = 215
                if meY<215 and meY>218:
                    meY = 218
            if meX<80 and meX> -100:
                if meY<184 and meY>175:
                    meY = 175
                if meY>184 and meY<188:
                    meY = 188
                if meY>335 and meY<339:
                    meY = 335
                if meY>340 and meY<345:
                    meY = 345
                if meY > 490 and meY<495:
                    meY = 490
                if meY>495 and meY< 500:
                    meY = 500
                if meY>175 and meY<512:
                    if meX<10:
                        meX = 10
            if meY>-100 and meY<35:
                if meX<535 and meX>525:
                    meX = 525
                if meX>615 and meX<626:
                    meX = 626
                if meX>815 and meX<825:
                    meX = 815
                if meX>903 and meX<913:
                    meX = 913
            if meY>29 and meY<39:
                if meX>525 and meX<626:
                    meY = 39
                if meX>815 and meX<910:
                    meY = 39
            if meX>78:
                if meY>0 and meY<185:
                    a = 1
                    direction = "right"
            ##"calling functions"
            
            if meY>50 and meY<276:
                if meX>DspW-4:
                    gameloop7(meX-DspW+50,meY,DspW,0,-10,0,0,-10)
            
            if meX>-50 and meX<75:
                if meY>164 and meY<168:
                    meY = 164
            if c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop6b(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    pg.mixer.music.stop()
    pg.mixer.Sound.stop(TF)
    i = 0
    boy1 = boyA
    boy2 = boyB
    angle = 270
    boy = boy1
    tcc = tr1
    tcr = tcc
    o = 0
    u = 0
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    spd = 2
    meX_chng = 0
    meY_chng = 0
    a = 0
    d = 0
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = [i for i  in range(0,470)]
        Yi = [i for i in range(20,970)]
        
        clock.tick(10)
        b = 2
        c = 0
        i = 2
        e = True
        enter = False
        f = 2
        j=0
        k=0
        r = 0
        d = 2
        g = 2
        radius = 7
        while fc:
            if game== True:
                pg.mixer.Sound.play(startS)
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop6,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop6,(0,0))
            o +=1
            if o%10==0:
                fcc = fc1
                tcr = pg.transform.rotate(tr1,angle)
            if o%20==0:
                fcc = fc2
                tcr = pg.transform.rotate(tr2,angle)
            if a==1 and g!=0:
                
                if  f!=0:
                    i = i+b
                    gd.blit(tcr,(Xi[-1],Yi[-i]))
                    angle = 90
                    if meY > Yi[-i]-10 and meY<Yi[-i]+10 or meX >Xi[-1]-10 and meX < Xi[-1]+10:
                        if meX <20 and meY>320 and meY<343 and croch == True:
                            c = 0
                        else:
                            c = 1
                if  i>945:
                    f=0
                    j += b
                    if j>460:
                        g = 0
                        Xi[j]  += 600
                    angle = 180   
                    gd.blit(tcr,(Xi[-j],Yi[5]))
                    if  meX > Xi[-j]-10 and meX< Xi[-j]+10:
                        if meX <20 and meY>320 and meY<343 and croch == True:
                            c = 0
                        else:
                            c = 1
                            meX = -100000
                            if meX>DspW-10:
                                meX = 10
                            if meX<10:
                                meX = 10
                            if meY<10:
                                meY = 10
                            if meY>DspH-10:
                                meY = DspH-10
            if f == 0 and g == 0:
                 gd.blit(arrow3,(200,10))
                 gd.blit(arrow3,(1000,10))
            pg.draw.circle(gd,black,(20,340),15)
            gd.blit(ldka,(meX-25,meY-25))
            gd.blit(tree2,(849,90))
            gd.blit(basket1,(322,94))
            gd.blit(basket2,(325,470))
            ##
            if meY>DspH-60 and g !=0:
                e = False
            if e == False:
                if enter == False:
                    msg_to_scrn2('He is comming behind you','go to the dark spot near stairs to hide',
                                                 'hide until he run away from the screen','                     press SPACE to continue',
                                                 '',black,300,150,0,0,Size = 15)
                    meY = DspH-63
                if enter == True:
                    e = True
                    enter = False
            ##
            if c== 1:
                game_over(red,'Hide till he run away from Screen',black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meY>DspW-10:
                    meY = DspW-10
                if meY<4:
                    meY = 4
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause("startS")
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)       
            if meY<10:
                if meX<200 and meX>-50 or meX>300 and meX<825:
                    meY = 10
            if meY > DspH-10:
                meY = DspH-10
            if meX >DspW-10:
                if meY>276:
                    meX = DspW-10
            if meY<DspH+100 and meY>165:
                if meX>922 and meX<932:
                    meX = 932
            if meX>500 and meX<932:
                if meY>164 and meY<168:
                    meY = 164
            if meY>130 and meY<196:
                if meX >75 and meX<79:
                    meX = 75
                if meX>79 and meX<82:
                    meX = 82
            if meY<DspH+100 and meY>130:
                if meX>505 and meX<509:
                    meX = 509
                
                if meX>500 and meX<504:
                    meX = 500
            if meX>DspW-10:
                meX = DspW-10
            if meX>335 and meX<348:
                if meY>215 and meY<218:
                    meY = 215
                if meY<215 and meY>218:
                    meY = 218
            if meX<80 and meX> -100:
                if meY<184 and meY>175:
                    meY = 175
                if meY>184 and meY<188:
                    meY = 188
                if meY>335 and meY<339:
                    meY = 335
                if meY>340 and meY<345:
                    meY = 345
                if meY > 490 and meY<495:
                    meY = 490
                if meY>495 and meY< 500:
                    meY = 500
                if meY>175 and meY<512:
                    if meX<10:
                        meX = 10
            if meX<10:
                meX = 10
            if meY>-100 and meY<35:
                if meX<535 and meX>525:
                    meX = 525
                if meX>615 and meX<626:
                    meX = 626
                if meX>815 and meX<825:
                    meX = 815
                if meX>903 and meX<913:
                    meX = 913
            if meY>29 and meY<39:
                if meX>525 and meX<626:
                    meY = 39
                if meX>815 and meX<910:
                    meY = 39
            if meX<509 and  meX>0:
                if meY>DspH-100 and meY<DspH-80:
                    a = 1
            ##"calling functions"
            if meY>50 and meY<276:
                if meX>DspW-4:
                    gameloop7(meX-DspW+50,meY,DspW,0,-10,0,0,-10)
            if meX>911 and meX<1130:
                if meY<4:
                    meX = rnd.randint(980,1080)
                    gameloop9(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if meX>200 and meX<300:
                if meY<4:
                    gameloop9(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if meY>50 and meY<163:
                if meX<4:
                    gameloop5(meX+DspW-50,meY,-DspW,0,10,0,0,-10)
            if meY<50 and meY>8:
                if meX<4:
                    gameloop8(meX+DspW-50,meY+DspW-50,-DspW,0,10,0,0,-10)
            if meY>535 and meY<580:
                if meX<4:
                    gameloop5(meX+DspW-50,meY,-DspW,0,10,0,0,-10)
            
            if meX>-50 and meX<75:
                if meY>164 and meY<168:
                    meY = 164
            if e== False or c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()

def gameloop5(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    boy1 = boyA
    boy2 = boyB
    fac = fac1
    direction = "up"
    facr = fac
    boy = boy1
    angle = 180
    angle1 = 270
    fcc = fc1
    fcr = fcc
    o = 0
    u = 0
    j = 0
    i = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    j = 0
    i = 0
    meX_chng = 0
    meY_chng = 0
    a = 0
    d = 0
    croch = False
    ayu = True
    e= True
    h = True
    enter = False
    while game:
        
        fc = True
        Xi = [i for i  in range(360,1000)]
        Yi = [i for i in range(85,600)]
        Xib = 1095
        Yi2 = [i for i in range(0,185)]
        clock.tick(0)
        b = 2
        c = 0
        i = 2
        f = 2
        j=0
        k=0
        r = 0
        d = 2
        g = 2
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop5,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop5,(0,0))
            o +=1
            if o%10==0:
                fcc = fc1
                fcr = pg.transform.rotate(fc1,angle1)
                facr = pg.transform.rotate(fac1,angle)
            if o%20==0:
                fcc = fc2
                fcr = pg.transform.rotate(fc2,angle1)
                facr = pg.transform.rotate(fac2,angle)

            if a==1 and g!=0:
                if  f!=0:
                    i = i+b
                    angle = 180
                    gd.blit(facr,(Xi[-i],Yi[1]))
                    if meY == Yi[1]:
                        c = 1
                if  i>630:
                    f=0
                    angle = 270
                    j += b
                    if j>510:
                        g = 0
                        Yi[j]  += 600
                    gd.blit(facr,(Xi[5],Yi[j]))
                    if j>2 :
                        if meY < Yi[j]+80:
                            if meX>960 and meY>552 and croch == True:
                                c = 0
                            
                            else:
                                c =1
            if a==1:
                gd.blit(fcr,(Xib,Yi2[k]-25))
                if meX > (Xib - 200):
                    if meY <Yi2[k]+60 and meY>Yi2[k]-60:
                        c = 1
                        meX = -100000
                        if meY<10:
                            meY = 10
                        if meY>DspH-10:
                            meY = DspH-10
                if k== 0:
                    angle1 = 270
                    d = 2
                if k==180:
                    angle1 = 90
                    d = -2
                k +=d
                

            gd.blit(ldka,(meX-25,meY-25))
            gd.blit(bus,(-230,-175))
            ##
            if meX>0 :
                if meY<410 and meY>404:
                    if j>510:
                        e = True
                    else:
                        e = False
                        b = 0
            if e == False:
                if enter ==  False:
                    msg_to_scrn2('A Faculty is comming here. Go and find a place to hide.',
                                                'Those big boxes at right corner are looking good to hide',
                                                'Dont forget to use "C"','                          press SPACE to continue','',
                                                black,400,120,-150,-50,Size = 15)
                    meY = 412
                if enter ==  True:
                    e= True
                    enter = False
                    b = 2
            if meX>660:
                if meY>0 and meY<140:
                    h = False
                
            if h == False:
                if enter ==  False:
                    msg_to_scrn2('me: i dont want to let him caught me','Find some other way to go',
                                                    '                           press SPACE to continue','','',black,300,100,-200,50,Size = 15)
                    meX = 654
                if enter == True:
                    h = True
                    enter = False
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meX>DspW-10:
                    meX = DspW-10
                if meY>DspH-10:
                    meY = DspH-10
                if meY< 4:
                    meY = 4
            if meX>483 and meX<535:
                if meY>310 and meY<412:
                    radius = 9
            if meX<483 or meX>535 or meY<310 or meY>412:
                if r == 1:
                    radius = 5
                else:
                    radius = 7
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                        
                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)            
            if meX>535 and meX<1095:
                if meY>555 and meY<560:
                    meY= 560
                if meY >135 and meY<140:
                    meY = 135
            if meY >140 and meY < 560:
                if meX>1090 and meX< 1095:
                    meX = 1095
                if meX > 530 and meX< 540:
                    meX = 530
            if meX > 1090 and meX < DspW:
                if meY> 485 and meY<490:
                    meY = 490
                if meY >335 and meY<342:
                    meY = 335
            if meY>555 and meY<575:
                if meX>852 and meX<857:
                    meX = 852
                if meX<966 and meX>962:
                    meX = 966
            if meX>852 and meX<966:
                if meY>570 and meY<575:
                    meY = 575
            if meY>135 and meY<495:
                if meX>470 and meX<485:
                    meX = 470
                if meX>496 and meX<500:
                    meX = 500
            if meX>20 and meX<215:
                if meY>435 and meY<440:
                    meY = 440
            if meX>485:
                if meY<10:
                    meY = 10
            if meY <440 and meY> -100:
                if meX > 212 and meX<218:
                    meX = 218
            if meY<10:
                if meX>1080:
                    meY = 10
            if meX<201 and meX>0:
                if meY>528 and meY<533:
                    meY = 528
            if meY >528:
                if meX>195 and meX< 201:
                    meX = 201
            if meY > DspH-10:
                if meX>445:
                    meY = DspH-10
            if meX >DspW-10:
                if meY>181:
                    meX = DspW-10
            if meX<30:
                meX = 30
           
            if meX>0:
                if meY<413 and meY>400 or meY>0 and meY<139:
                    a = 1
            
            ##"calling functions"
            if meX>200 and meX<525:
                if meY>DspH-4:
                    meX = rnd.randint(250,400)
                    gameloop2(meX,meY-DspH+50,0,800,0,-10,-10,0)
                if meY<4:
                    meX = rnd.randint(220,356)
                    gameloop8(meX,meY+DspH-50,0,-800,0,10,-10,0)
            if meY>10 and meY<180:
                if meX>DspW-4:
                    gameloop6(meX-DspW+50,meY,DspW,0,-10,0,0,-10)
            if e ==False or h == False or c ==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop5b(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    j = 0
    i = 0
    angle = 270
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    tr = tr1
    tcr = pg.transform.rotate(tr,270)
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    d = 0
    croch = False
    ayu = True
    
    while game:
        
        fc = True
        b = 2
        c = 0
        i = 2
        f = 2
        j=0
        k=0
        d = 2
        ex = 200
        ey = -40
        speed = 2
        g = 2
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop5,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop5,(0,0))
            gd.blit(arrow,(590,50))
            gd.blit(ldka,(meX-25,meY-25))
            o +=1
            if o%10==0:
                tcr = pg.transform.rotate(tr1,0)
            if o%20==0:
                tcr = pg.transform.rotate(tr2,0)
            
            pg.mixer.Sound.play(TF)
            if a==1:
                if ex>meX:
                    ex-= speed
                elif ex<meX:
                    ex += speed
                if ey<meY:
                    ey+= speed
                elif ey>meY:
                     ey -= speed
                gd.blit(tcr,(ex-50,ey-50))
                gd.blit(tcr,(ex-50,ey-50))
                if ex <meX+2 and ex> meX-2:
                    if ey < meY+2 and ey >meY-2:
                        c = 1
                        meX = 100000
                        if meX>DspW-10:
                            meX = DspW-10
                        if meY<10:
                            meY =10
                    
            gd.blit(bus,(-230,-175))
            if c== 1:
                game_over(red,'Noooooo! He Caught me',black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meX>DspW-10:
                    meX = DspW-10
                if meY>DspH-10:
                    meY = DspH-10
                if meY< 4:
                    meY = 4
            if meX>483 and meX<535:
                if meY>310 and meY<412:
                    radius = 9
            if meX<483 or meX>535 or meY<310 or meY>412:
                if d == 1:
                    radius = 5
                else:
                    radius = 7
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -speed
                        if a!=1:
                            direction = "up"
                        angle = 90
                    if event.key == pg.K_DOWN:
                        meY_chng = speed
                        if a!=1:
                            direction = "down"
                        angle = 270
                    if event.key == pg.K_LEFT:
                        meX_chng = -speed
                        direction = "left"
                        angle = 180
                    if event.key == pg.K_RIGHT :
                        meX_chng = speed
                        direction = "right"
                        angle = 0
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        speed = 1
                        croch = True
                    if event.key ==pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause("TF")
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        speed = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)
            if meX>535 and meX<1095:
                if meY>555 and meY<560:
                    meY= 560
                if meY >135 and meY<140:
                    meY = 135
            if meY >140 and meY < 560:
                if meX>1090 and meX< 1095:
                    meX = 1095
                if meX > 530 and meX< 540:
                    meX = 530
            if meX > 1090 and meX < DspW:
                if meY> 485 and meY<490:
                    meY = 490
                if meY >335 and meY<342:
                    meY = 335
            if meY>555 and meY<575:
                if meX>852 and meX<857:
                    meX = 852
                if meX<966 and meX>962:
                    meX = 966
            if meX>852 and meX<966:
                if meY>570 and meY<575:
                    meY = 575
            if meY>135 and meY<495:
                if meX>470 and meX<485:
                    meX = 470
                if meX>496 and meX<500:
                    meX = 500
            if meX>20 and meX<215:
                if meY>435 and meY<440:
                    meY = 440
            if meX>485:
                if meY<10:
                    meY = 10
            if meY <440 and meY> -100:
                if meX > 212 and meX<218:
                    meX = 218
            if meY<10:
                if meX>1080:
                    meY = 10
            if meX<201 and meX>0:
                if meY>528 and meY<533:
                    meY = 528
            if meY >528:
                if meX>195 and meX< 201:
                    meX = 201
            if meY > DspH-10:
                if meX>445:
                    meY = DspH-10
            if meX >DspW-10:
                if meY>181:
                    meX = DspW-10
            if meX<30:
                meX = 30
           
            if meX>0:
                if meY>0 and meY<150 :
                    a = 1
                    direction = "right"
            ##"calling functions"
            if meX>200 and meX<525:
                if meY>DspH-4:
                    meX = rnd.randint(250,400)
                    gameloop2(meX,meY-DspH+50,0,800,0,-10,-10,0)
                if meY<4:
                    meX = rnd.randint(220,356)
                    gameloop8(meX,meY+DspH-50,0,-800,0,10,-10,0)
            if meY>10 and meY<180:
                if meX>DspW-4:
                    gameloop6(meX-DspW+50,meY,DspW,0,-10,0,0,-10)
            if c == 1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop4(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    pg.mixer.music.stop()
    
    j = 0
    tr = tr1
    tcr = pg.transform.rotate(tr,270)
    i = 0
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    ex = 300
    ey = 0
    speed = 2
    while game:
        
        
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop4,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop4,(0,0))
            gd.blit(arrow2,(10,200))
            gd.blit(ldka,(meX-25,meY-25))
            o +=1
            if o%10==0:
                tcr = pg.transform.rotate(tr1,180)
            if o%20==0:
                tcr = pg.transform.rotate(tr2,180)
            
            if a==1:
                pg.mixer.Sound.play(TF)
                if ex>meX:
                    ex-= speed
                elif ex<meX:
                    ex += speed
                if ey<meY:
                    ey+= speed
                elif ey>meY:
                     ey -= speed
                gd.blit(tcr,(ex-50,ey-50))
                if ex <meX+2 and ex> meX-2:
                    if ey < meY+2 and ey >meY-2:
                        
                        c = 1
                        meX = 100000
                        if meX <10:
                            meX = 10
                        if meY<10:
                            meY = 10
            if c== 1:
                game_over(red,'He Caught me ! -_-',black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                if meY>DspW-10:
                    meY = DspW-10
                if meY<4:
                    meY = 4

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -speed
                        if a!=1:
                           direction = "up"
                        angle = 90
                    if event.key == pg.K_DOWN:
                        meY_chng = speed
                        if a!=1:
                            direction = "down"
                        angle = 270
                    if event.key == pg.K_LEFT:
                        meX_chng = -speed
                        direction = "left"
                        angle = 180
                    if event.key == pg.K_RIGHT :
                        meX_chng = speed
                        direction = "right"
                        angle = 0
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key ==pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause("TF")
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        speed = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0) 
            if meX>-30 and meX<655:
                if meY>463 and meY<470:
                    meY = 465
            if meY>470 and meY<DspH+30:
                if meX>630 and meX<635:
                    meX = 635
            if meX>-30 and meX<655:
                if meY>475 and meY<488:
                    meY = 488
            if meY>485 and meY<DspH+30:
                if meX>614 and meX<625:
                    meX = 614
            if meX>-30 and meX<445:
                if meY>DspH-10:
                    meY = DspH-10
            if meY>150 and meY<255:
                if meX>238 and meX<242:
                    meX = 238
                if meX>672 and meX<676:
                    meX = 676
            if meX>240 and meX<655:
                if meY>252 and meY<256:
                    meY = 256
                if meY >148 and meY<152:
                    meY = 148
            if meX>255 and meX<DspW+50:
                if meY<10:
                    meY = 10
            if meX> DspW-50:
                meX = DspW-50
            if meX>10 and meY>10:
                a = 1
                direction = "left"
            ##"Function calling"
            if meY>488:
                if meX<4:
                    gameloop3(meX+DspW-50,meY,-DspW,0,10,0,0,-10)
            if meX>431 and meX<493:
                if meY>DspH-4:
                    gameloop(meX,meY+DspH-50,0,DspH,0,-10,-10,0)
            if meX>95 and meX<255:
                if meY<4:
                    gameloop7(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if meY>50 and meY<475:
                if meX<4:
                    gameloop3(meX+DspW-50,meY,-DspW,0,10,0,0,-10)
            if c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop3(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    
    pg.mixer.music.stop()
    j = 0
    i = 0
    angle = 270
    tr = tr1
    tcr = pg.transform.rotate(tr,270)
    boy1 = boyA
    boy2 = boyB
    boy = boy1
    o = 0
    u = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    direction = "up"
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    ex = DspW-10
    ey = 80
    speed = 2
    while game:
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop3,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop3,(0,0))
            gd.blit(ldka,(meX-25,meY-25))
            o +=1
            if o%10==0:
                tcr = pg.transform.rotate(tr1,180)
            if o%20==0:
                tcr = pg.transform.rotate(tr2,180)
            gd.blit(arrow3,(300,10))
            if a==1:
                pg.mixer.Sound.play(TF)
                if ex>meX:
                    ex-= speed
                elif ex<meX:
                    ex += speed
                if ey<meY:
                    ey+= speed
                elif ey>meY:
                     ey -= speed
                gd.blit(tcr,(ex-50,ey-50))
            gd.blit(tree,(210,381))
            gd.blit(tree,(360,387))
            gd.blit(tree,(540,389))
            gd.blit(tree,(685,389))
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meY>DspW-10:
                    meY = DspW-10
                if meY<4:
                    meY = 4

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -speed
                        if a!=1:
                            direction = "up"
                        angle = 90
                    if event.key == pg.K_DOWN:
                        meY_chng = speed
                        if a!=1:
                            direction = "down"
                        angle = 270
                    if event.key == pg.K_LEFT:
                        meX_chng = -speed
                        direction = "left"
                        angle = 180
                    if event.key == pg.K_RIGHT :
                        meX_chng = speed
                        direction = "right"
                        angle = 0
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        speed = 1
                        croch = True
                    if event.key ==pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause("TF")
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        speed = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)
            
            if meX>-10 and meX<40:
                if meY>435 and meY<439:
                    meY = 439
            if meY<438 and meY>255:
                if meX>37 and meX<40:
                    meX = 40
            if meX >10 and meX<60:
                if meY>250 and meY<260:
                    meY = 260
            if meY<260 and meY>147:
                if meX> 47 and meX<53:
                    meX = 53
            if meX<53 and meX > 10:
                if meY > 145 and meY< 149:
                    meY = 145
            if meY < 155 and meY >62:
                if meX > 35 and meX < 39:
                    meX =39
            if meX <37 and meX>-10:
                if meY>62 and meY<67:
                    meY = 62
            if meX>75 and meX < DspW+50:
                if meY<480 and meY>477:
                    meY = 480
            if meX>75 and meX < DspW+50:
                if meY<474 and meY>465:
                    meY = 465
            if meY < 480 and meY>65:
                if meX >72 and meX<76:
                    meX=72
            if meX>455 and meX<DspW+50:
                if meY<10:
                    meY = 10
            if meY > DspH-10:
                meY = DspH-10
            if meY>430 and meY<481:
                if meX<10:
                    meX = 10
            if meX>-50 and meX<191:
                 if meY<10:
                     meY = 10
            if meX<DspW-50:
                a= 1
                direction = "left"
            ## 'function calling'
            if meY>482 and meY<595:
                if meX<4:
                    gameloop2(meX+DspW-50,meY,-DspW,0,10,0,0,-10)
                if meX>DspW-4:
                    gameloop4(meX-DspW+50,meY,DspW,0,-10,0,0,-10)
            if meX>191 and meX<475:
                if meY<4:
                    gameloop6b(meX,meY+DspH-50,0,-DspH,0,10,-10,0)
            if meY>4 and meY<350:
                if meX>DspW-4:
                    gameloop4(meX-DspW+50,meY,DspW,0,-10,0,0,-10)
            if ex <meX+2 and ex> meX-2:
                    if ey < meY+2 and ey >meY-2:
                        c=1
                        meX = 1000
                        ex = 0
                        if meX>DspH-10:
                            meX = 10
                        if meY<10:
                            meY = 10
            if c==1:
                #pg.mixer.Sound.stop(game_overS)
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
  
def gameloop2(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    game = True
    boy1 = boyA
    boy2 = boyB
    angle = 270
    boy = boy1
    fcc = fc1
    fcr = fcc
    o = 0
    u = 0
    j = 0
    i = 0
    spd = 2
    ldka = pg.transform.rotate(boy,90)
    meX_chng = 0
    meY_chng = 0
    a = 0
    e= True
    direction = "up"
    enter = False
    croch = False
    ayu = True
    while game:
        
        fc = True
        Xi = 1035
        Yi = [i for i in range(335,480)]
        clock.tick(0)
        Yr = 400
        b = 2
        c = 0
        i = 0
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop2,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop2,(0,0))
            o +=1
            if o%10==0:
                fcc = fc1
                fcr = pg.transform.rotate(fc1,angle)
            if o%20==0:
                fcc = fc2
                fcr = pg.transform.rotate(fc2,angle)
            if a==1:
                gd.blit(fcr,(Xi-25,Yi[i]-25))
                
                if meX>Xi-70:
                    c = 1
                    meX = -100000
                    
                if i == 2:
                    angle = 270
                    b = 2
                if i==142:
                    angle = 90
                    b = -2
                i +=b
            gd.blit(ldka,(meX-25,meY-25))
            gd.blit(shelter,(335,87))
            gd.blit(bus,(-230,-175))
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                Ychng = 0
                Xchng = 0
                if meX>DspW-10:
                    meX = DspW-10
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        meY_chng = -2
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = 2
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -2
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = 2
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_SPACE:
                        enter = True
                    if event.key==pg.K_p:
                        pause()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
                        
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)           
            if meX == 638:
                meX = 630
            if meX>632 and meX<636:
                e = False
                meX = 640
            if e == False:
                if enter == False:
                    msg_to_scrn2('me: i dont want to let him caught me','Find some other way to go',
                                                    '                           press SPACE to continue','','',black,300,100,-100,50,Size = 15)
                
                if enter == True:
                    e = True
                    enter = False
            ##
            if meX<196:
                meX = 196
            if meX >428 and meX< DspW+50:
                if meY >480and meY<490:
                    meY = 480
            if meY >483 and meY<DspH+50:
                if meX > 430 and meX <435:
                    meX = 430
            if meX > 428 and meX<964:
                if meY >405 and meY<410:
                    meY = 410
            if meY>331 and meY<415:
                if meX>963 and meX<967:
                    meX = 967
            if meX > 965 and meX<1035:
                if meY>330 and meY<334:
                     meY = 334
            
            if meX>1030 and meX<1035:
                if meY<335 and meY>200:
                     meX = 1035
                if meY>65 and meY<120:
                     meX = 1035
            if meY <200 and meY>120:
                if meX>1045 and meX<1048:
                    meX = 1048
            if meX >1030 and meX<1047:
                if meY >195 and meY<200:
                    meY = 200
            if meX >1030 and meX<1047:
                if meY >125 and meY<129:
                    meY = 125
            if meX<1031 and meX>960:
                if meY>60 and meY<65:
                    meY = 60
            if meY<80 and meY> -50:
                if meX>960 and meX<965:
                    meX = 965
            if meY> -50 and meY<410:
                if meX>425 and meX<431:
                    meX = 425
           ## "Calling Functions"

            if meX>200 and meX<414:
                if meY<4:
                    gameloop5(meX,meY+DspH-50,0,-600,0,10,-10,0)
            if meX>DspW-4 and meX:
                gameloop3(meX-DspW+50,meY,800,0,-10,0,0,-10)
            if meY>DspH-4:
                if meX>203 and meX<418:
                    meX = rnd.randint(190,300)
                    gameloop(meX,meY-DspH+50,0,600,0,-10,-10,0)
            if meX>440 and meY<460:
                if meY>405and meY<490:
                    a = 1
            if e== False or  c==1:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10== 0:
                    boy = boy2
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
def gameloop(meX,meY,X,Y,Xchng,Ychng,Xvalue,Yvalue):
    pg.mixer.Sound.stop(startS)
    fcc= fc1
    boy1 = boyA
    boy2 = boyB
    angle = 270
    fcr = pg.transform.rotate(fcc,270)
    boy = boy1
    u = 0
    spd = 2
    game = True
    direction = "up"
    ldka = pg.transform.rotate(boy,90)
    j = 0
    i = 0
    meX_chng = 0
    meY_chng = 0
    a = 0
    croch = False
    ayu = True
    enter = False
    e = True
    f = True
    g = True
    o=0
    croch = False
    while game:
        pg.mixer.music.play(-1)
        fc = True
        Xi = 200
        Yi = [i for i in range(0,400)]
        clock.tick(0)
        Yr = 400
        b = 2
        
        c = 0
        i = 0
        radius = 7
        while fc:
            pg.display.update()
            gd.fill(white)
            while ayu:
                gd.blit(loop1,(X,Y))
                pg.display.update()
                Y += Ychng
                X += Xchng
                if  Y ==Yvalue:
                    ayu = False
                if X==Xvalue:
                    ayu = False
            gd.blit(loop1,(0,-200))
            
            if a==1:
                o +=1
                if o%10==0:
                    fcc = fc1
                    fcr = pg.transform.rotate(fc1,angle)
                if o%20==0:
                    fcc = fc2
                    fcr = pg.transform.rotate(fc2,angle)
                gd.blit(fcr,(Xi-15,Yi[i]-25))
                if meX<Xi+100 :
                    if meY <Yi[i]+60 and meY>Yi[i]-60:
                        if meX>265:
                            if meY>207 and meY<311 and croch == True:
                                c = 0
                            else:
                                c = 1
                        else:
                            c = 1
                            meX = 100000
               
                    
                if i == 0:
                    angle = 270
                    b = 2
                if i==380:
                    angle = 90
                    b = -2
            
                i +=b
                
            gd.blit(ldka,(meX-25,meY-25))
            gd.blit(bus,(220,175))   
            gd.blit(guard,(915,530))
            
            if c== 1:
                game_over(red,text_color=black,Size=25,Font='Arial',ydisp=0,xdisp=0)
                meX_chng = 0
                meY_chng = 0
                if meY<10:
                    meY = 10
                
            if meX>224 and meX<258:
                if meY>290 and meY<317:
                    meY = 317
                if meY>175 and meY<184:
                    meY = 175
            if meY>175 and meY<317:
                if meX>250  and meY<265:
                    meX = 275
                if meX>224 and meX<235:
                    meX = 224
            
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        boy1 = sboy1
                        boy2 = sboy2
                        meX_chng = 0
                        meY_chng = 0
                        spd = 1
                        croch = True
                    if event.key == pg.K_UP:
                        meY_chng = -spd
                        meX_chng = 0
                        direction = "up"
                    if event.key == pg.K_DOWN:
                        meY_chng = spd
                        meX_chng = 0
                        direction = "down"
                    if event.key == pg.K_LEFT:
                        meX_chng = -spd
                        meY_chng= 0
                        direction = "left"
                    if event.key == pg.K_RIGHT :
                        meX_chng = spd
                        meY_chng = 0
                        direction = "right"
                    if event.key == pg.K_q:
                        game = False
                    if event.key==pg.K_p:
                        pause()
                    if event.key == pg.K_r:
                        pg.mixer.music.play()
                    if event.key == pg.K_2:
                        gameloop2(400,300,0,0,0,0,0,0,)
                        
                    if event.key == pg.K_p:
                        pause()
##                    if event.key == pg.K_8:
##                        gameloop8(400,300,0,0,0,0,0,0,)
##                    if event.key == pg.K_h:
##                        gameloop16(400,300,0,0,0,0,0,0,)
##                    if event.key == pg.K_b:
##                        gameloop6b(400,300,0,0,0,0,0,0,)
##                    if event.key == pg.K_9:
##                        gameloop9b(1120,10,0,0,0,0,0,0,)
##                    if event.key == pg.K_z:
##                        gameloop10(1120,500,0,0,0,0,0,0,)
##                    if event.key == pg.K_x:
##                        gameloop11b(1120,500,0,0,0,0,0,0,)
##                    if event.key == pg.K_v:
##                        gameloop11(1120,500,0,0,0,0,0,0,)
##                    if event.key == pg.K_n:
##                        gameloop12(1120,500,0,0,0,0,0,0,)
##                    if event.key == pg.K_m:
##                        gameloop13(1120,500,0,0,0,0,0,0,)
##                    if event.key == pg.K_l:
##                        gameloop14(1120,500,0,0,0,0,0,0,)
##                    if event.key == pg.K_j:
##                        gameloop16b(1120,500,0,0,0,0,0,0,)
##                    if event.key == pg.K_f:
##                        gameloop8b(250,0,0,0,0,0,0,0,)
                    if event.key == pg.K_SPACE:
                        enter = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        meY_chng = 0
                        #direction == 
                    if event.key == pg.K_DOWN:
                        meY_chng = 0
                    if event.key == pg.K_LEFT:
                        meX_chng = 0 
                    if event.key == pg.K_RIGHT:
                        meX_chng = 0
                    if event.key == pg.K_c:
                        boy1 = boyA
                        boy2 = boyB
                        meX_chng = 0
                        meY_chng = 0
                        croch = False
                        spd = 2
            if direction =="up":
                ldka = pg.transform.rotate(boy,90)
            if direction =="left":
                ldka = pg.transform.rotate(boy,180)
            if direction =="down":
                ldka = pg.transform.rotate(boy,270)
            if direction =="right":
                ldka = pg.transform.rotate(boy,0)            
            ##messeges
            if meX>900 and meY>520:
                e = False
            if e ==False:
                if enter == False:
                    msg_to_scrn2('Watchman: Hey you, where are you going','me: Nowhere',
                                                  'watchman: You are not allowed to go outside',
                                                  'me: I knew that', '                                  press SPACE to continue',
                                                    black,320,170,0,150,Size =15)
                if enter ==True:
                    e = True
                    meX = 898
                    enter = False
                    
            if  meX<370 and meX>360:
                meX = 356
                f =False
            if  meX==358:
                meX = 372
            if f== False:
                
                msg_to_scrn2('A warden is comming Here',"Make sure he won't see you",
                                            'Use C to crouch','You can also use bus for purpose',
                                                '                           press SPACE to continue',black,320,170,-100,0,Size =15)
                if enter == True:
                    f = True
                    g = True
                    enter = False
            if meX>880 and meX<966:
                 if meY<420:
                     g = False
                     meY = 422

            if g == False:
                if enter == False:
                     msg_to_scrn2('Dude i dont want to go from here','Its girls Hostel on right side',
                                                      'Boys are prohabited in this area', 'go to some other way',
                                                        '                        press SPACE to continue',black,320,170,-100,100,Size =15)
                if enter == True:
                    g = True
                    meY = 425
                    enter = False
                #enter =  False
            ##########
            if meX>188 and meX<278:
                if meY<5:
                    gameloop2(meX,meY+DspH-50,0, -600,0,10,-10,0)
            if meX>DspW-10:
                meX = DspW-11
            if meX <179:
                meX = 180
            if meX>728 and meX<DspW+100:
                if meY>215 and meY<415:
                    meY = 415
                if meY>32 and meY<50:
                    meY = 32
            if meY>-50 and meY<82:
                if meX>955:
                    meX = 955       
            
            if meY>470:
                if meX> 754 and meX<757:
                    meX = 757
                elif meX >170 and meX< 754:
                    meY = 469
            if meY>59 and meY<600:
                if meX >950 and  meX <957:
                    meX = 950
            if meX>276 and meX<883:
                if meY<415 and meY>411:
                    meY = 415
            if meY <415 and meY>66:
                if meX >276 and meX<279:
                    meX = 276
            if meX <329 and meX>280:
                if meY>64 and meY<67:
                    meY = 64
            if meY >-10 and meY <65:
                if meX >310 and meX <315:
                    meX = 310
            if meX > 330 and meX <678:
                if meY >40 and meY<43:
                    meY = 40
            if meY >-10 and meY < 70:
                if meX>688 and meX < 691:
                    meX = 691
            if meX >673 and meX<743:
                if meY>64 and meY<67:
                    meY = 64
            if meY>36 and meY<74:
                if meX>723 and meX<725:
                    meX = 723
            if meY<4:
                meY = 4
            if meX >705 and meX<845:
                if meY >65 and meY<67:
                    meY = 64
            if meY >66 and meY<418:
                if meX>727 and meX <731:
                    meX = 731
            if meX>955 and meX<1160:
                if meY >60 and meY< 63:
                    meY = 59
            if meY >35 and meY<415:
                if meX >885 and meX<887:
                    meX = 887
            if meY>DspH-5:
                meY = DspH-10
            if meX<375:
                if meY<480 and meY>414:
                    a = 1
            if g== False:
                meX_chng = 0
                meY_chng = 0
            if f == False:
                meX_chng = 0
                meY_chng = 0
            if e==False:
                meX_chng = 0
                meY_chng = 0
            if meY_chng!=0 or meX_chng!=0:
                u +=1
                if u%20 ==0 :
                    boy = boy1
                elif  u%10 == 0:
                    boy = boy2
            
            meX += meX_chng
            meY += meY_chng
            pg.display.update()
            clock.tick(100)
start()  























          


