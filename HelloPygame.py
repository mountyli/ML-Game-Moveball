#!/usr/bin/env python
# https://blog.csdn.net/lu_123456/article/details/8457217?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-4
background_image_filename='Haigercabin.jpg'
# either you configure variant path, or add the path into filename 'C:/Users/mounty.li/Desktop/Github/ML-Game-Moveball/backgroundsample.jpg'
mouse_image_filename='pic_mouse.png'
#'C:/Users/mounty.li/Desktop/Github/ML-Game-Moveball/fugu.png'

import pygame

from pygame.locals import *
#导入常用函数和常量
from sys import exit

pygame.init()
#初始化

screen=pygame.display.set_mode((500,390),0,32)
#create a window
pygame.display.set_caption('hello,World!')
#title

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#load and convert image

#main loop
while True:
    for event in pygame.event.get():
        if event.type== QUIT:
            exit()


    screen.blit(background,(0,0))
        #draw bkgd

    x,y=pygame.mouse.get_pos()

    x-= mouse_cursor.get_width()/2
    y-= mouse_cursor.get_width()/2

    screen.blit(mouse_cursor,(x,y))

    pygame.display.update()


