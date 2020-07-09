#!/usr/bin/env python
#https://eyehere.net/2011/python-pygame-novice-professional-2/

import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

#picture resource
Ball_Red_Surface=pygame.image.load("ballred.png")
Ball_Green_Surface=pygame.image.load("ballgreen.png")
Ball_Blue_Surface=pygame.image.load("ballblue.png")
Ball_Purple_Surface=pygame.image.load("ballpurple.png")
Ball=[Ball_Red_Surface,Ball_Green_Surface,Ball_Blue_Surface,Ball_Purple_Surface]
Ball_width=Ball[0].get_width()
Ball_height=Ball[0].get_height()
arrow_up=pygame.image.load("arrow_up.png")
arrow_down=pygame.image.load("arrow_down.png")
arrow_left=pygame.image.load("arrow_left.png")
arrow_right=pygame.image.load("arrow_right.png")

font=pygame.font.SysFont("arial",19)

#initialize the window
screen=pygame.display.set_mode((700,700),0,32)
inerX=50
inerY=50
global move_step
move_step=0
scrach_surface=pygame.surface.Surface((80,20))
scrach_surface.fill((0,0,0))

screen.blit(font.render("PressN:new",True,(255,0,255)),(5,10))
screen.blit(font.render("PressM:Pazl",True,(255,0,255)),(5,30))
screen.blit(font.render("STEP",True,(255,0,255)),(650,10))
screen.blit(font.render("0", True,(255,0,255)),(650,32))

for p in range(4):
    screen.blit(arrow_up,(p*Ball_width+inerX+50,0))
    pygame.display.update()
    screen.blit(arrow_down,(p*Ball_width+inerX+50,650))
    screen.blit(arrow_left,(0,p*Ball_width+inerY+50))
    pygame.display.update()
    screen.blit(arrow_right,(650,p*Ball_width+inerY+50))
pygame.display.update()

for y_temp in range(4):
    for x_temp in range(4):
        screen.blit(Ball[y_temp],(x_temp*Ball_width+inerX,y_temp*Ball_height+inerY))
pygame.display.update()



Pos_ball=[[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]

def Change_column_up(n):
    global move_step,Pos_ball
    Temp_Ball=Pos_ball[0][n]
    Pos_ball[0][n]=Pos_ball[1][n]
    Pos_ball[1][n]=Pos_ball[2][n]
    Pos_ball[2][n]=Pos_ball[3][n]
    Pos_ball[3][n]=Temp_Ball
    for i in range(4):
        screen.blit(Ball[Pos_ball[i][n]],(n*150+inerX,i*150+inerY))
        pygame.display.update()
    for y in range(4):
        for x in range(4):
            print(str(Pos_ball[y][x]))
    return True

def Change_column_down(n):
    global move_step,Pos_ball
    x=Pos_ball[3][n]
    Pos_ball[3][n]=Pos_ball[2][n]
    Pos_ball[2][n]=Pos_ball[1][n]
    Pos_ball[1][n]=Pos_ball[0][n]
    Pos_ball[0][n]=x
    for i in range(4):
        screen.blit(Ball[Pos_ball[i][n]],(n*150+inerX,i*150+inerY))
    pygame.display.update()
    return True

def Change_line_left(n):
    global move_step,Pos_ball
    x=Pos_ball[n][0]
    Pos_ball[n][0]=Pos_ball[n][1]
    Pos_ball[n][1]=Pos_ball[n][2]
    Pos_ball[n][2]=Pos_ball[n][3]
    Pos_ball[n][3]=x
    for i in range(4):
        screen.blit(Ball[Pos_ball[n][i]],(i*150+inerX,n*150+inerY))
    for y in range(4):
        for x in range(4):
            print(str(Pos_ball[y][x]))
    pygame.display.update()
    return True

def Change_line_right(n):
    global move_step,Pos_ball
    x=Pos_ball[n][3]
    Pos_ball[n][3]=Pos_ball[n][2]
    Pos_ball[n][2]=Pos_ball[n][1]
    Pos_ball[n][1]=Pos_ball[n][0]
    Pos_ball[n][0]=x
    for i in range(4):
        screen.blit(Ball[Pos_ball[n][i]],(i*150+inerX,n*150+inerY))
    pygame.display.update()
    return True




while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            exit()

        if event.type==KEYDOWN:
            if event.key==K_n:
                #new start
                for x_cyc in range(4):
                    for y_cyc in range(4):
                        screen.blit(Ball[y_cyc],(x_cyc*Ball_width+inerX,y_cyc*Ball_height+inerY))
                pygame.display.update()
                Pos_ball=[[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
                move_step=0
                screen.blit(scrach_surface,(650,30))
                screen.blit(font.render(str(move_step), True,(255,0,255)),(650,30))
                pygame.display.update()
                
            if event.key==K_m:
                #new choas
                for stir_step in range(20):
                    a1=random.randint(0,3)
                    a2=random.randint(0,3)
                    a3=random.randint(0,3)
                    a4=random.randint(0,3)
                    temp_p=Pos_ball[a1][a2]
                    temp_q=Pos_ball[a3][a4]
                    Pos_ball[a1][a2]=temp_q
                    Pos_ball[a3][a4]=temp_p
                for y in range(4):
                    for x in range(4):
                        screen.blit(Ball[Pos_ball[y][x]],(x*Ball_width+inerX,y*Ball_height+inerY))
                        print(str(Pos_ball[y][x])) #debug 
                pygame.display.update()
                move_step=0
                screen.blit(scrach_surface,(650,30))
                screen.blit(font.render(str(move_step), True,(255,0,255)),(650,30))
                pygame.display.update()

        x,y=pygame.mouse.get_pos()
        moveline=0
        movecolumn=0
        if pygame.mouse.get_pressed()[0]:
            if x<inerX:
                for i in range(4):
                    for j in range(4):
                        print(Pos_ball[i][j])
                if y>inerY and y<600+inerY:
                    if y<150+inerY and y>inerY:
                        moveline=0
                        for i in range(4):
                            for j in range(4):
                                print(Pos_ball[i][j])
                    elif y>150+inerY and y<300+inerY:
                        moveline=1
                    elif y>300+inerY and y<450+inerY:
                        moveline=2
                    elif y>450+inerY:
                        moveline=3
                    Change_line_left(moveline)
                    move_step+=1
                    screen.blit(scrach_surface,(650,30))
                    screen.blit(font.render(str(move_step), True,(255,0,255)),(650,30))
                    pygame.display.update()
            elif x>600+inerX:
                if y>inerY and y<600+inerY:
                    if y<150+inerY and y>inerY:
                        moveline=0
                    elif y>150+inerY and y<300+inerY:
                        moveline=1
                    elif y>300+inerY and y<450+inerY:
                        moveline=2
                    elif y>450+inerY:
                        moveline=3
                    Change_line_right(moveline)
                    move_step+=1
                    screen.blit(scrach_surface,(650,30))
                    screen.blit(font.render(str(move_step), True,(255,0,255)),(650,30))
                    pygame.display.update()
            else :
                if y<inerY or y>600+inerX:
                    if x>inerX and x<150+inerX:
                        moveline=0
                    elif x>150+inerX and x<300+inerX:
                        moveline=1
                    elif x>300+inerX and x<450+inerX:
                        moveline=2
                    elif x>450+inerX:
                        moveline=3
                    if y<inerY:
                        Change_column_up(moveline)
                    elif y>inerY+600:
                        Change_column_down(moveline)
                    move_step+=1
                    screen.blit(scrach_surface,(650,30))
                    screen.blit(font.render(str(move_step), True,(255,0,255)),(650,30))
                    pygame.display.update()
        

'''
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y>component*80 and y<(component+1)*80:
                color[component]=int((x/639.)*255.)

        pygame.display.set_caption("Pygame color test-"+str(tuple(color)))

    for component in range(3):
        pos=(int((color[component]/255.)*639),component*80+40)
        pygame.draw.circle(screen,(255,255,255),pos,20)

    pygame.draw.rect(screen,tuple(color),(0,240,640,240))
    

    pygame.display.update()
'''
