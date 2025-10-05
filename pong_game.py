import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('my game')
def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont('freesans',32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
y=200
y1=200
x=300
x1=550
y2=300
x2=0
down=False
up=False
down1=False
up1=False
speedx=1
speedy=1
player1=0
player2=0
gameover=False
while True:
        screen.fill((0,0,0))
        pygame.time.delay(5)
        pygame.draw.rect(screen,blue,(x2,y,50,125))
        pygame.draw.rect(screen,blue,(x1,y1,50,125))
        pygame.draw.circle(screen,green,(x,y2),20)
        x=x+speedx
        y2=y2+speedy
        if down==True:
            y=y+2
        if up==True:
            y=y-2
        if down1==True:
            y1=y1+2
        if up1==True:
            y1=y1-2
        if y<0:
            y=0
        if y>475:
            y=475
        if y1<0:
            y1=0
        if y1>475:
            y1=475
        if (x==x1 and y1<=y2<=y1+125):
            speedx=-speedx
        if (x==x2+50 and y<=y2<=y+125):
            speedx=-speedx
        if y2-20<=0 or y2+20>=600:
            speedy=-speedy
        if x>=600:
            player1=player1+1
            x=300
            y2=300
        if x<=0:
            player2=player2+1
            x=300
            y2=300
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    down=True
                    up=False
                if event.key==pygame.K_UP:
                    down=False
                    up=True
                if event.key==pygame.K_s:
                    down1=True
                    up1=False
                if event.key==pygame.K_w:
                    down1=False
                    up1=True
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            show_text('player 1:'+str(player1),0,0,red)
            show_text('player 2:'+str(player2),455,0,red)
            if player1==5:
                gameover=True
            elif player2==5:
                gameover=True
            if gameover==True:
                screen.fill((0,0,0))
                show_text('GAME OVER',200,200,red)
                if player1==5:
                    show_text('Player 1 Won',200,300,red)
                    time.sleep(3)
                else:
                    show_text('Player 2 Won',200,300,red)
                    time.sleep(3)
        pygame.display.update()
red=(255,0,0)
blue=(0,0,255)
