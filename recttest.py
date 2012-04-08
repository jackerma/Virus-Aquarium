#!usr/bin/env python

import pygame
from pygame.locals import *
from server import *
from virus import *
import time

done = False
width = 1300
height = 700
screen = pygame.display.set_mode((width, height))
background_colour = (150,150,150)
score = 100
virus_count = 0

#Servers 
Player1 = Home_server(screen, (20,20))
Player2 = Home_server(screen, (1130, 270))
comp1 = Server(screen, (150, 250))
comp2 = Server(screen, (500, 400))
comp3 = Server(screen, (410, 200))
comp4 = Server(screen, (700, 500))
comp5 = Server(screen, (800, 300))
comp6 = Server(screen, (900, 100))
comp7 = Server(screen, (250, 500))
comp8 = Server(screen, (1000, 520))
comps = [Player1, Player2, comp1,comp2, comp3, comp4, comp5, comp6, comp7, comp8]

comp8.off_state = True

#Virus
red_xvirus = XVirus(1)

while not done:

    screen.fill(background_colour)

#Connects computers
    for com1 in comps:
        for com2 in comps:
                x1, y1 = com1.rect.center
                x2, y2 = com2.rect.center
                if (x2-x1)**2 + (y2-y1)**2 <= (2*com1.cnct_range)**2 and com2 not in com1.connected_list and com1 != com2:
                    com1.connected_list.append(com2)
    
#Drawing
    for comp in comps:
        comp.draw_circle()
        comp.draw_lines()
        
    for comp in comps:
        comp.draw_rect()

    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((600,0), (200,50)))
    text = smallfont.render("Score = " + str(score), True, (255,0,0))
    loc = text.get_rect()
    loc.topleft = (600,0)
    screen.blit(text,loc)

    pygame.display.flip()


##Keys
    for event in pygame.event.get():

#Adding Virus red
        if event.type == KEYDOWN and event.key == K_w:
            if score >= 10 and (Player1.red_viruses['x'])+1 < 25:
                Player1.add_virus(red_xvirus)
                score -= 10

#Adding Virus blue
#        if event.type == KEYDOWN and event.key == K_w:
#            if score >= 10 and (Player1.blue_viruses['x'])+1 < 25:
#                Player1.add_virus(blue_xvirus)
#                score -= 10

#Spreading Virus
        if event.type == KEYDOWN and event.key == K_s:
            for comp in comps:
                red_xvirus.spread(comp)



#Quitting
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN and event.key== K_ESCAPE:
            done = True

#Update

    for comp in comps:
        comp.wipe()
        comp.onoff()
        red_xvirus.spread(comp)

#        comp.count(score)
        if comp.off_state == False:
            virus_count = comp.red_viruses['x']/10
        score += virus_count




    time.sleep(.2)
