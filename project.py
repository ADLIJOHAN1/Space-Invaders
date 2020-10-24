#importing modules
import pygame as p
import math as m
import random as r


#intializing pygame
p.init()

#game window
screen=p.display.set_mode((1200,1000))

#title and icon
p.display.set_caption("SPACE INVADERS")
icon=p.image.load("space-game.png")
p.display.set_icon(icon)

#background
bg=p.image.load("space.jpg")
def background():
    screen.blit(bg,(0,0))

#player
hero=p.image.load("spaceship.png")
p_xcoord=550
p_ycoord=800
p_xchange=0
def player(x,y):
    screen.blit(hero,(x,y))

#score
score = 0
text = p.font.Font("FreeSansBold.ttf",32)
txt_xcoord = 10
txt_ycoord = 10
def scoreshow(x,y):
    screen_score = text.render("SCORE : "+str(score),True,(255,255,255))
    screen.blit(screen_score,(x,y))

#Game over text
game_over=p.font.Font("FreeSansBold.ttf",64)
def gameover():
    game_text=game_over.render("GAME OVER !",True,(255,255,255))
    screen.blit(game_text,(455,450))

#enemy
villain=[]
v_xcoord=[]
v_ycoord=[]
v_xchange=[]
v_ychange=[]
enemycount=4
for i in range(enemycount):
    villain.append(p.image.load("invaders.png"))
    v_xcoord.append(r.randint(0,1200))
    v_ycoord.append(r.randint(100,300))
    v_xchange.append(4)
    v_ychange.append(60)
def enemy(x,y,i):
    screen.blit(villain[i],(x,y))

#bullet
bullet=p.image.load("jing.fm-blast-clipart-1178204.png")
bulletx=2000
bullety=2000
bulletx_change=0
bullety_change=20
bullet_state='ready' 

def fireBullet(x,y):
   global bullet_state
   bullet_state='fire'
   screen.blit(bullet,(x+58,y+40))

#collision
def iscollision(bulletx,bullety,v_xcoord,v_ycoord):
    distance=m.sqrt(m.pow(bulletx-v_xcoord,2)+(m.pow(bullety-v_ycoord,2)))
    if distance < 30:
        return True
    else :
        return False
        


#gameloop
run=True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run==False

    #players movement 
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                p_xchange = -4
            if event.key == p.K_RIGHT:
                p_xchange = 4
            if event.key==p.K_SPACE:
              if bullet_state=='ready':
                  bullety=p_ycoord 
                  bulletx=p_xcoord
                  fireBullet(bulletx,bullety)
            
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT or event.key == p.K_RIGHT:
                p_xchange = 0
    p_xcoord += p_xchange         

    
    background()
    
    #adding borders to ensure spaceship stays inside window
    if p_xcoord <=0:
        p_xcoord = 0
    elif p_xcoord >= 1072:
        p_xcoord = 1072
        
    #enemy movement
    for i in range(enemycount):

        #Game over display
        if v_ycoord[i] > 680:
            for j in range(enemycount):
                v_ycoord[j] = 1200
            gameover()
            break
        
        v_xcoord[i] += v_xchange[i]
    
        if v_xcoord[i] <=0:
            v_xchange[i] = 4
            v_ycoord[i] += v_ychange[i] 
        elif v_xcoord [i]>= 1072:
            v_xchange[i] = -4
            v_ycoord[i] += v_ychange[i]
        enemy(v_xcoord[i],v_ycoord[i],i)

        #collision effects
        collision=iscollision(bulletx,bullety,v_xcoord[i],v_ycoord[i])
        if collision == True:
            bullety=540
            bullet_state="ready"
            v_xcoord[i]=r.randint(0,1072)
            v_ycoord[i]=r.randint(100,300)
            score +=10
            
            

    #bullet movement
    if bullety<=0:
       bullety=540
       bullet_state='ready'
    if bullet_state == 'fire':        
       fireBullet(bulletx,bullety)
       bullety-=bullety_change

    
    scoreshow(txt_xcoord,txt_ycoord)
    player(p_xcoord,p_ycoord)
    p.display.update()

quit()
