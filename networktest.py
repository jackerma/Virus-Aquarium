#!/usr/bin/env python

import networkx as nx
import pygame
from random import randint

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
        server = pygame.Rect(pos, (20,20))
        pygame.draw.rect(screen, (0,0,0), server)
    
    pygame.display.flip()
