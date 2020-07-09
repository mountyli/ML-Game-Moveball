#!/usr/bin/env python
#based on https://eyehere.net/2011/python-pygame-novice-professional-2/

import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

#picture resource
Ball_Red_Surface=pygame.image.load("ballred_s.png")
Ball_Green_Surface=pygame.image.load("ballgreen_s.png")
Ball_Blue_Surface=pygame.image.load("ballblue_s.png")
Ball_Purple_Surface=pygame.image.load("ballpurple_s.png")
Ball=[Ball_Red_Surface,Ball_Green_Surface,Ball_Blue_Surface,Ball_Purple_Surface]
Ball_width=Ball[0].get_width()
Ball_height=Ball[0].get_height()

arrow_up=pygame.image.load("arrow_up.png")
arrow_down=pygame.image.load("arrow_down.png")
arrow_left=pygame.image.load("arrow_left.png")
arrow_right=pygame.image.load("arrow_right.png")
global arrow_side
arrow_side=arrow_up.get_width()

#Font
font=pygame.font.SysFont("arial",19)

#initialize the window
global edgeX, edgeY,scr_iniX, scr_iniY, ballarea_iniX, ballarea_iniY,window_width, window_height
edgeX=50+50 #blank area 
edgeY=100+50+50 #blank or text area
scr_iniX=int(edgeX/2)
scr_iniY=edgeY-edgeX
ballarea_iniX=scr_iniX+arrow_side
ballarea_iniY=scr_iniY+arrow_side
window_width=4*Ball_width+2*arrow_side+edgeX
window_height=4*Ball_height+2*arrow_side+edgeY

screen=pygame.display.set_mode((window_width,window_height),0,32)
global move_step
move_step=0
scrach_surface=pygame.surface.Surface((80,20))
scrach_surface.fill((0,0,0))

screen.blit(font.render("Welcome to MOVE BALL GAME",True,(255,0,255)),(30,10))
screen.blit(font.render("Press Button N: new game start; Button M: Puzzle game start",True,(255,0,255)),(10,30))
#screen.blit(font.render("Press Button M: Puzzle game start",True,(255,0,255)),(10,30))
screen.blit(font.render("Now you already move STEP  ",True,(255,0,255)),(10,50))
global step_location
step_location=(320,50)
screen.blit(font.render("0", True,(255,0,255)),step_location)

#draw arrows
for p in range(4):
    screen.blit(arrow_up,(p*Ball_width+ballarea_iniX+15,scr_iniY))
    pygame.display.update()
    screen.blit(arrow_down,(p*Ball_width+ballarea_iniX+15,ballarea_iniY+4*Ball_height))
    screen.blit(arrow_left,(scr_iniX,p*Ball_width+ballarea_iniY+15))
    pygame.display.update()
    screen.blit(arrow_right,(ballarea_iniX+4*Ball_height,p*Ball_width+ballarea_iniY+15))
pygame.display.update()

#draw balls
for y_temp in range(4):
    for x_temp in range(4):
        screen.blit(Ball[y_temp],(ballarea_iniX+x_temp*Ball_width,y_temp*Ball_height+ballarea_iniY))
pygame.display.update()
Pos_ball=[[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]

def Change_column_up(n): #n: the column/line which need move
    global move_step,Pos_ball
    Temp_Ball=Pos_ball[0][n]
    Pos_ball[0][n]=Pos_ball[1][n]
    Pos_ball[1][n]=Pos_ball[2][n]
    Pos_ball[2][n]=Pos_ball[3][n]
    Pos_ball[3][n]=Temp_Ball
    for i in range(4):
        screen.blit(Ball[Pos_ball[i][n]],(n*Ball_width+ballarea_iniX,i*Ball_height+ballarea_iniY))
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
        screen.blit(Ball[Pos_ball[i][n]],(n*Ball_width+ballarea_iniX,i*Ball_height+ballarea_iniY))
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
        screen.blit(Ball[Pos_ball[n][i]],(i*Ball_width+ballarea_iniX,n*Ball_height+ballarea_iniY))
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
        screen.blit(Ball[Pos_ball[n][i]],(i*Ball_width+ballarea_iniX,n*Ball_height+ballarea_iniY))
    pygame.display.update()
    return True



#main loop
while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            exit()

        if event.type==KEYDOWN:
            if event.key==K_n:
                #new start

                
                for x_cyc in range(4):
                    for y_cyc in range(4):
                        screen.blit(Ball[y_cyc],(x_cyc*Ball_width+ballarea_iniX,y_cyc*Ball_height+ballarea_iniY))
                    pygame.display.update()
                Pos_ball=[[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
                move_step=0
                screen.blit(scrach_surface,step_location)
                screen.blit(font.render(str(move_step), True,(255,0,255)),step_location)
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
                        screen.blit(Ball[Pos_ball[y][x]],(x*Ball_width+ballarea_iniX,y*Ball_height+ballarea_iniY))
                        print(str(Pos_ball[y][x])) #debug 
                pygame.display.update()
                move_step=0
                screen.blit(scrach_surface,step_location)
                screen.blit(font.render(str(move_step), True,(255,0,255)),step_location)
                pygame.display.update()

        x,y=pygame.mouse.get_pos()
        moveline=0
        movecolumn=0
        if pygame.mouse.get_pressed()[0]:
            if x<ballarea_iniX and x>scr_iniX:
                for i in range(4):
                    for j in range(4):
                        print(Pos_ball[i][j])
                if y>ballarea_iniY and y<4*Ball_width+ballarea_iniY:
                    if y<Ball_width+ballarea_iniY and y>ballarea_iniY:
                        moveline=0
                        for i in range(4):
                            for j in range(4):
                                print(Pos_ball[i][j])
                    elif y>ballarea_iniY and y<2*Ball_width+ballarea_iniY:
                        moveline=1
                    elif y>2*Ball_width+ballarea_iniY and y<3*Ball_width+ballarea_iniY:
                        moveline=2
                    elif y>3*Ball_width+ballarea_iniY and y<4*Ball_width+ballarea_iniY:
                        moveline=3
                    Change_line_left(moveline)
                    move_step+=1
                    screen.blit(scrach_surface,step_location)
                    screen.blit(font.render(str(move_step), True,(255,0,255)),step_location)
                    pygame.display.update()
            elif x>ballarea_iniX+4*Ball_width and x<ballarea_iniX+4*Ball_width+arrow_side:
                if y>ballarea_iniY and y<4*Ball_width+ballarea_iniY:
                    if y<Ball_width+ballarea_iniY and y>ballarea_iniY:
                        moveline=0
                        for i in range(4):
                            for j in range(4):
                                print(Pos_ball[i][j])
                    elif y>ballarea_iniY and y<2*Ball_width+ballarea_iniY:
                        moveline=1
                    elif y>2*Ball_width+ballarea_iniY and y<3*Ball_width+ballarea_iniY:
                        moveline=2
                    elif y>3*Ball_width+ballarea_iniY and y<4*Ball_width+ballarea_iniY:
                        moveline=3
                    Change_line_right(moveline)
                    move_step+=1
                    screen.blit(scrach_surface,step_location)
                    screen.blit(font.render(str(move_step), True,(255,0,255)),step_location)
                    pygame.display.update()
            elif x>ballarea_iniX and x<ballarea_iniX+4*Ball_width :
                if (y<ballarea_iniY and y>scr_iniY)or (y>ballarea_iniY+4*Ball_width and y<ballarea_iniY+4*Ball_width+arrow_side):
                    if x<ballarea_iniX+Ball_width:
                        moveline=0
                    elif x>ballarea_iniX+Ball_width and x<ballarea_iniX+2*Ball_width:
                        moveline=1
                    elif x>ballarea_iniX+2*Ball_width and x<ballarea_iniX+3*Ball_width:
                        moveline=2
                    elif x>ballarea_iniX+3*Ball_width:
                        moveline=3
                    if y<ballarea_iniY:
                        Change_column_up(moveline)
                    elif y>ballarea_iniY+3*Ball_width:
                        Change_column_down(moveline)
                    move_step+=1
                    screen.blit(scrach_surface,step_location)
                    screen.blit(font.render(str(move_step), True,(255,0,255)),step_location)
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
