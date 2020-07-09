#!/usr/bin/env python
# https://eyehere.net/2011/python-pygame-novice-professional-2/
background_image_filename='Haigercabin.jpg'
# either you configure variant path, or add the path into filename 'C:/Users/mounty.li/Desktop/Github/ML-Game-Moveball/backgroundsample.jpg'
# mouse_image_filename='pic_mouse.png'
#'C:/Users/mounty.li/Desktop/Github/ML-Game-Moveball/fugu.png'

import pygame

from pygame.locals import *
#导入常用函数和常量
from sys import exit

pygame.init()
#初始化
SCREEN_SIZE=(640,480)
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
#create a window
background=pygame.image.load(background_image_filename).convert()

x,y=0,0
move_x,move_y=0,0

font = pygame.font.SysFont("arial", 16)
font_height=font.get_linesize()
event_text= []

pygame.display.set_caption('hello,World, Lesson 2!')
#title

#background = pygame.image.load(background_image_filename).convert()
#mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#load and convert image

#main loop
while True:
    for event in pygame.event.get():
        print(event.type)

        if event.type==QUIT:
            exit()
        if event.type==KEYDOWN:
            print('Keydown')
            if event.key==K_LEFT:
                move_x=-1
            elif event.key==K_RIGHT:
                move_x=1
            elif event.key==K_UP:
                move_y=-1
            elif event.key==K_DOWN:
                move_y=1
            print(move_x, move_y)
        elif event.type==KEYUP:
            print('keyup')
            move_x=0
            move_y=0

    x+=move_x
    y+=move_y
    print(x,y,move_x,move_y)

    screen.fill((0,0,0))
    screen.blit(background,(x,y))

    pygame.display.update()


