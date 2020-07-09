# -*- coding: utf-8 -*-
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

font1=pygame.font.SysFont("calibri",40)
text_surface=font1.render("hihi i am here",True,(0,0,140))


x=0
y=int((480-text_surface.get_height())/2)

font = pygame.font.SysFont("arial", 16)
font_height=font.get_linesize()
event_text= []

pygame.display.set_caption('hello,World, Lesson 4, Font Font!')
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
    screen.blit(background,(0,0))
        
    x-=1
    if x<-text_surface.get_width():
        x=640-text_surface.get_width()
        
    screen.blit(text_surface,(x,y))

    pygame.display.update()


