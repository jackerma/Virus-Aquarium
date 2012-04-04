#!/usr/bin/env python


from server import Server
import pygame
from pygame.locals import *
from random import randint
import time



#Globals

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
radius = 150

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
pygame.display.set_caption('Virus Aquarium')


done = False
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
 
   

    #Drawing Circles
    screen.fill(background_colour)
    for rect in rects:
        pygame.draw.circle(screen, background_colour, rect.center, radius, 1)
        
    #Drawing Lines    
    for rect in rects:
        colliding_circles = []
        rect_radius = radius
        for i in range(len(rects)-1):
            for j in range(i+1,len(rects)):
                rect1 = rects[i]
                rect2 = rects[j]
                x1, y1 = rect1.center
                x2, y2 = rect2.center
                if (x2-x1)**2 + (y2-y1)**2 <= (2*rect_radius)**2:
                    colliding_circles.append(((x1,y1),(x2,y2)))

        for point_pair in colliding_circles:
            point1,point2 = point_pair
            pygame.draw.aaline(screen, (255,0,0), point1, point2, 5)
        
        
        


#screen placement
    for server in rects:
        
        comp_screen =  pygame.Rect((0,0), (Rect_width-scrn_thick,Rect_height-scrn_thick))
        comp_screen.center = server.center
        comp_screens.append(comp_screen)





#draw method
    for server in rects:
        pygame.draw.rect(screen, (0,0,0), server)

    for comp_screen in comp_screens:
        pygame.draw.rect(screen, (255,255,255), comp_screen)
    
#    Player1 = Server()
 #   Player1.draw(screen,(200,200))
    
        
    
    pygame.display.flip()
    
