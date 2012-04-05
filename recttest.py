#!usr/bin/env python

import pygame
from pygame.locals import *
from server import Server

done = False
width = 1300
height = 700
screen = pygame.display.set_mode((width, height))
background_colour = (150,150,150)

#Servers 
comp1 = Server(screen, (150, 250))
comp2 = Server(screen, (500, 400))
comp3 = Server(screen, (410, 200))
comp4 = Server(screen, (700, 500))
comp5 = Server(screen, (800, 300))
comp6 = Server(screen, (900, 100))
comp7 = Server(screen, (250, 500))
comp8 = Server(screen, (1000, 520))
comps = [comp1,comp2, comp3, comp4, comp5, comp6, comp7, comp8]

while not done:

    screen.fill(background_colour)

    for com1 in comps:
        for com2 in comps:
                x1, y1 = com1.rect.center
                x2, y2 = com2.rect.center
                if (x2-x1)**2 + (y2-y1)**2 <= (2*com1.cnct_range)**2 and com2 not in com1.connected_list and com1 != com2:
                    com1.connected_list.append(com2)
    
    for comp in comps:
      #  comp.draw_circle()
        comp.draw_lines()
        
    for comp in comps:
        comp.draw_rect()
    
    pygame.display.flip()




#Quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN and event.key== K_ESCAPE:
            done = True