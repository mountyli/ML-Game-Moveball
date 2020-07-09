#!/usr/bin/env python
# https://eyehere.net/2011/python-pygame-novice-professional-2/
# background_image_filename='Haigercabin.jpg'
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
    event=pygame.event.wait()
    event_text.append(str(event))
	
    event_text=event_text[-int(SCREEN_SIZE[1]/font_height):]
	
    if event.type== QUIT:
        exit()
				
    screen.fill((0,0,0))
	
    y=SCREEN_SIZE[1]-font_height
	
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(255,255,255)),(0,y))
        y-=font_height

    pygame.display.update()


