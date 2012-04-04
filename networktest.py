#!/usr/bin/env python

import pygame
from random import randint
Rect_width= 160
Rect_height= 120
scrn_thick = 4
x, y = 0,0
#Globals
width, height = 1300,700

networkSize = 10
radius = 150

comps = sorted(set((randint(radius,width-radius),randint(radius,height-radius)) for i in range(networkSize)))


#Screen Setup Stuff
background_colour = (255,255,255)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Virus Aquarium')


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(background_colour)

    for pos in comps:
        #Draw Circle
        pygame.draw.circle(screen, (255,255,255), (x+Rect_width/2, y+Rect_height/2), radius, 1)
        
        
    for pos in comps:
        #Draw Lines
        colliding_circles = []
        for i in range(len(comps)-1):
            for j in range(i+1,len(comps)):
                x1,y1 = comps[i]
                x2,y2 = comps[j]
                if x2-x1>2*radius:
                    break #can't collide anymore.
                if (x2-x1)**2 + (y2-y1)**2 <= (2*radius)**2:
                    x1 = x1 + Rect_width/2
                    y1 = y1 + Rect_height/2
                    x2 = x2 + Rect_width/2
                    y2 = y2 + Rect_height/2
                    colliding_circles.append(((x1,y1),(x2,y2)))
        for point_pair in colliding_circles:
            point1,point2 = point_pair
            pygame.draw.aaline(screen, (255,0,0), point1, point2, 5)
        

    for pos in comps:
        #Drawing Computers
        server = pygame.Rect(pos, (Rect_width,Rect_height))
        (x, y) = pos
        comp_screen =  pygame.Rect((x+scrn_thick, y+scrn_thick), (Rect_width-scrn_thick*2,Rect_height-scrn_thick*2))
        pygame.draw.rect(screen, (0,0,0), server)
        pygame.draw.rect(screen, (255,255,255), comp_screen)
        
    
    pygame.display.flip()
    
