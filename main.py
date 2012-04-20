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
score_red = 100
score_blue = 100
virus_count_red = 0
virus_count_blue = 0
target_dict= {'x_red':0, 'y_red':0, 'x_blue':0, "yblue":0}

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


#Virus
red_xvirus = XVirus(1)
blue_xvirus = XVirus(2)
red_yvirus = YVirus(1)
blue_yvirus = YVirus(2)


red_virus_list = [red_xvirus, red_yvirus]
blue_virus_list = [blue_xvirus, blue_yvirus]


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

    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((350,0), (200,50)))
    text = smallfont.render("Score = " + str(score_red), True, (255,0,0))
    loc = text.get_rect()
    loc.topleft = (350,0)
    screen.blit(text,loc)

    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((800,0), (200,50)))
    text = smallfont.render("Score = " + str(score_blue), True, (0,0,255))
    loc = text.get_rect()
    loc.topleft = (800,0)
    screen.blit(text,loc)

    pygame.display.flip()


##Keys
    for event in pygame.event.get():

#Adding Virus red
        if event.type == KEYDOWN and event.key == K_w:
            if score_red >= 10 and (Player1.red_viruses['x'])+1 < 25:
                Player1.add_virus(red_xvirus)
                score_red -= 10

#Adding Virus blue
        if event.type == KEYDOWN and event.key == K_u:
            if score_blue >= 10 and (Player2.blue_viruses['x'])+1 < 25:
                Player2.add_virus(blue_xvirus)
                score_blue -= 10

#Adding Virus red
        if event.type == KEYDOWN and event.key == K_e:
            if score_red >= 10 and (Player1.red_viruses['y'])+1 < 25:
                Player1.add_virus(red_yvirus)
                score_red -= 10

#Adding Virus blue
        if event.type == KEYDOWN and event.key == K_i:
            if score_blue >= 10 and (Player2.blue_viruses['y'])+1 < 25:
                Player2.add_virus(blue_yvirus)
                score_blue -= 10


#Quitting
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN and event.key== K_ESCAPE:
            done = True

#Update

    for comp in comps:
        comp.wipe()
        comp.onoff()
        for virus in red_virus_list:
            virus.spread(comp)
            
        for virus in blue_virus_list:
            virus.spread(comp)


        if comp.off_state == False:
            virus_count_red = comp.red_viruses['x']/10
        score_red += virus_count_red

        if comp.off_state == False:
            virus_count_blue = comp.blue_viruses['x']/10
        score_blue += virus_count_blue




    time.sleep(.2)
