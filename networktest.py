#!/usr/bin/env python

import networkx as nx
import pygame
from random import randint
Rect_width= 160
Rect_height= 120
scrn_thick = 4
x, y = 0,0
#Globals
width, height = 1300,700

networkSize = 10
radius = 80

comps = sorted(set((randint(radius,width-radius),randint(radius,height-radius)) for i in range(networkSize)))


#Screen Setup Stuff
background_colour = (255,255,255)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Tutorial 2')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    for pos in comps:
        server = pygame.Rect(pos, (Rect_width,Rect_height))
        (x, y) = pos
        comp_screen =  pygame.Rect((x+scrn_thick, y+scrn_thick), (Rect_width-scrn_thick*2,Rect_height-scrn_thick*2))
        pygame.draw.rect(screen, (0,0,0), server)
        pygame.draw.rect(screen, (255,255,255), comp_screen)
    
    pygame.display.flip()
