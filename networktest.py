#!/usr/bin/env python

import pygame
from pygame.locals import *
from random import randint
import time

Rect_width= 160
Rect_height= 120
scrn_thick = 10
x, y = 0,0
rects = []
comp_screens = []

width, height = 1300,700
i=0
j=0
networkSize = 10
radius = 80

comps = sorted(set((randint(0,width-Rect_width),randint(0,height-Rect_height)) for i in range(networkSize)))



#Screen Setup Stuff
background_colour = (200,200,200)
screen = pygame.display.set_mode((width, height))

#setup game objects

for pos in comps:

    rects.append(pygame.Rect(pos, (Rect_width,Rect_height)))


#gets screen bounds
bounds = screen.get_rect()

pygame.display.set_caption('Tutorial 2')


done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN and event.key== K_ESCAPE:
            done = True


#collision

    while j<100:
        j+=1
        for rect in rects:
            i +=1
            rects.remove(rect)
            if rect.collidelist(rects)!=-1:
                pos = (randint(0,width-Rect_width),randint(0,height-Rect_height))
                rect = pygame.Rect(pos, (Rect_width,Rect_height))
            rects.insert(i,rect)
 
   
   


#            rect = rect.move(randint(radius,width-radius),randint(radius,height-radius))


            
#draw method
    screen.fill(background_colour)


    for server in rects:
        
        comp_screen =  pygame.Rect((0,0), (Rect_width-scrn_thick,Rect_height-scrn_thick))
        comp_screen.center = server.center
        comp_screens.append(comp_screen)

        pygame.draw.rect(screen, (0,0,0), server)

    for comp_screen in comp_screens:
        pygame.draw.rect(screen, (255,255,255), comp_screen)




    
    pygame.display.flip()
