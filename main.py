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
Player1.is_team(1)
Player2 = Home_server(screen, (1130, 270))
Player2.is_team(2)
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
red_wvirus =  Wall_Virus(1, Player1)
blue_wvirus =  Wall_Virus(2, Player2)
red_bvirus =  Bomb_Virus(1)
blue_bvirus = Bomb_Virus(2)


red_virus_list = [red_xvirus, red_yvirus, red_wvirus, red_bvirus]       
blue_virus_list = [blue_xvirus, blue_yvirus, blue_wvirus, blue_bvirus]    


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
    

    
    Player1.scrn_change()
    Player2.scrn_change()

    for comp in comps:
        comp.draw_text()
    pygame.display.flip()


##Keys
    for event in pygame.event.get():

#Adding XVirus red
        if not Player1.lose:
            if event.type == KEYDOWN and event.key == K_w:
                if score_red >= 10 and (Player1.red_viruses['x']) <red_xvirus.max:
                    Player1.add_virus(red_xvirus)
                    score_red -= 10

#Adding YVirus red
            if event.type == KEYDOWN and event.key == K_e:
                if score_red >= 10 and (Player1.red_viruses['y']) <red_yvirus.max:
                    Player1.add_virus(red_yvirus)
                    score_red -= 10

#Adding Wall_Virus red
            if event.type == KEYDOWN and event.key == K_q:
                if score_red >= 10 and (Player1.red_viruses['w']) < 10:
                    Player1.add_virus(red_wvirus)
                    score_red -= 10

#Adding Bomb_Virus red
            if event.type == KEYDOWN and event.key == K_r:
                if score_red >= 10 and (Player1.red_viruses['b']) < red_bvirus.max:
                    Player1.add_virus(red_bvirus)
                    score_red -= 10

#Adding XVirus blue
        if not Player2.lose:
            if event.type == KEYDOWN and event.key == K_u:
                if score_blue >= 10 and (Player2.blue_viruses['x']) < blue_xvirus.max:
                    Player2.add_virus(blue_xvirus)
                    score_blue -= 10

#Adding YVirus blue
            if event.type == KEYDOWN and event.key == K_i:
                if score_blue >= 10 and (Player2.blue_viruses['y']) < blue_yvirus.max:
                    Player2.add_virus(blue_yvirus)
                    score_blue -= 10

#Adding Wall_Virus blue
            if event.type == KEYDOWN and event.key == K_y:
                if score_blue >= 10 and (Player2.blue_viruses['w']) < 10:
                    Player2.add_virus(blue_wvirus)
                    score_blue -= 10

#Adding Bomb_Virus blue
            if event.type == KEYDOWN and event.key == K_o:
                if score_blue >= 10 and (Player2.blue_viruses['b']) < blue_bvirus.max:
                    Player2.add_virus(blue_bvirus)
                    score_blue -= 10


#Quitting
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN and event.key== K_ESCAPE:
            done = True

#Update

    for comp in comps:
        target_dict= {'x_red':0, 'y_red':0, 'x_blue':0, 'y_blue':0} 
        comp.wipe()
        comp.onoff()

        for virus in red_virus_list:
            virus.spread(comp)
            if virus.type == 'y':
                virus.target(comp, target_dict)
                
        for virus in blue_virus_list:
            virus.spread(comp)
            if virus.type == 'y':
                virus.target(comp, target_dict)
                
        
        #Killing the target list 

        comp.red_viruses['x'] -= target_dict['x_red']
        if comp.red_viruses['x'] < 0:        #So minimum = 0
            comp.red_viruses['x'] = 0
            
        comp.red_viruses['y'] -= target_dict['y_red']
        if comp.red_viruses['y'] < 0:
            comp.red_viruses['y'] = 0


        comp.blue_viruses['x'] -= target_dict['x_blue']
        if comp.blue_viruses['x'] < 0:
            comp.blue_viruses['x'] = 0

        comp.blue_viruses['y'] -= target_dict['y_blue']
        if comp.blue_viruses['y'] < 0:
            comp.blue_viruses['y'] = 0

    for comp in comps:
        
        if comp.off_state == False:
            virus_count_red = comp.red_viruses['x']/10
        score_red += virus_count_red

        if comp.off_state == False:
            virus_count_blue = comp.blue_viruses['x']/10
        score_blue += virus_count_blue


        



    time.sleep(.2)

