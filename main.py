#!usr/bin/env python

import pygame
from pygame.locals import *
from server import *
from virus import *
import time
from maps import *

#Choosing Map
print ""
print "Initializing: Virus Aquarium"
print "________________________________________________________"
print "1. Linear"
print "2. X-R0ads"
print "3. Bridge"
print "_________________________________________________________"
network_map = raw_input("Select map number: ")


if network_map == str(1) or network_map == str(2) or network_map == str(3):
    print "Loading..."
    time.sleep(.6)
else:
    print "Randomizing..."
    time.sleep(1)

#Globals
done = False
width = 1300
height = 700
screen = pygame.display.set_mode((width, height))
background_colour = (150,150,150)
score_red = 200
score_blue = 200
virus_count_red = 0
virus_count_blue = 0
bomb_count_red = 0
bomb_count_blue = 0
target_dict = {'x_red':0, 'y_red':0, 'w_red':0, 'b_red':0, 'x_blue':0, 'y_blue':0, 'w_blue':0, 'b_blue':0}
score_red_t = 0
score_blue_t = 0
score_dec_b = 0
score_dec_r = 0



#Map init
gamemap = Map(screen, network_map)

Player1 = gamemap.Player1
Player2 = gamemap.Player2
comps = gamemap.comps

#Virus
red_xvirus = XVirus(1, Player1)
blue_xvirus = XVirus(2, Player2)
red_yvirus = YVirus(1, Player1)
blue_yvirus = YVirus(2, Player2)
red_wvirus =  Wall_Virus(1, Player1)
blue_wvirus =  Wall_Virus(2, Player2)
red_bvirus =  Bomb_Virus(1, Player1)
blue_bvirus = Bomb_Virus(2, Player2)


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


    pygame.draw.rect(screen, background_colour, pygame.Rect((350,0), (200,50)))
    text = scorefont.render("Score = " + str(score_red), True, (255,0,0))
    loc = text.get_rect()
    loc.topleft = (300,0)
    screen.blit(text,loc)

    pygame.draw.rect(screen, background_colour, pygame.Rect((800,0), (200,50)))
    text = scorefont.render("Score = " + str(score_blue), True, (0,0,255))
    loc = text.get_rect()
    loc.topleft = (750,0)
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
                if score_red >= red_xvirus.cost and sum(Player1.red_viruses.values()) < Player1.virus_max:
                    Player1.red_viruses['x'] +=1
                    score_red -= red_xvirus.cost
#Subtracting XVirus red
            if event.type == KEYDOWN and event.key == K_s:
                if Player1.red_viruses['x'] > 0:
                    Player1.red_viruses['x'] -=1


#Adding YVirus red
            if event.type == KEYDOWN and event.key == K_e:
                if score_red >= red_yvirus.cost and sum(Player1.red_viruses.values()) < Player1.virus_max:
                    Player1.red_viruses['y'] += 1
                    score_red -= red_yvirus.cost
#Subtracting YVirus red
            if event.type == KEYDOWN and event.key == K_d:
                if Player1.red_viruses['y'] > 0:
                    Player1.red_viruses['y'] -=1


#Adding Wall_Virus red
            if event.type == KEYDOWN and event.key == K_q:
                if score_red >= red_wvirus.cost and sum(Player1.red_viruses.values()) < Player1.virus_max:
                    Player1.red_viruses['w'] += 1
                    score_red -= red_wvirus.cost
#Subtracting Wall_Virus red
            if event.type == KEYDOWN and event.key == K_a:
                if red_viruses['w'] > 0:
                    Player1.red_viruses['w'] -=1


#Adding Bomb_Virus red
            if event.type == KEYDOWN and event.key == K_r:
                if score_red >= red_bvirus.cost and bomb_count_red == 0 and sum(Player1.red_viruses.values()) < Player1.virus_max:
                    Player1.add_virus(red_bvirus)
                    score_red -= red_bvirus.cost

                else:
                    for comp in comps:
                        if comp.red_viruses['b'] == 1 and comp.off_state == False:
                            comp.off_state = True
                            comp.scrn_colour = (100,100,100)
                            comp.blue_viruses = {'x':0, 'y':0, 'w':0, 'b':0} 
                            comp.red_viruses ['b'] = 0


#Adding XVirus blue
        if not Player2.lose:
            if event.type == KEYDOWN and event.key == K_u:
                if score_blue >= blue_xvirus.cost and sum(Player2.blue_viruses.values()) < Player2.virus_max:
                    Player2.blue_viruses['x'] +=1
                    score_blue -= blue_xvirus.cost
#Subtracting XVirus blue
            if event.type == KEYDOWN and event.key == K_j:
                if Player2.blue_viruses['x'] > 0:
                    Player2.blue_viruses['x'] -=1


#Adding YVirus blue
            if event.type == KEYDOWN and event.key == K_i:
                if score_blue >= blue_yvirus.cost and sum(Player2.blue_viruses.values()) < Player2.virus_max:
                    Player2.blue_viruses['y'] +=1
                    score_blue -= blue_yvirus.cost
#Subtracting YVirus blue
            if event.type == KEYDOWN and event.key == K_k:
                if Player2.blue_viruses['y'] > 0:
                    Player2.blue_viruses['y'] -=1


#Adding Wall_Virus blue
            if event.type == KEYDOWN and event.key == K_y:
                if score_blue >= blue_wvirus.cost and sum(Player2.blue_viruses.values()) < Player2.virus_max:
                    Player2.blue_viruses['w'] +=1
                    score_blue -= blue_wvirus.cost
#Subtracting Wall_Virus blue
            if event.type == KEYDOWN and event.key == K_h:
                if Player2.blue_viruses['w'] > 0:
                    Player2.blue_viruses['w'] -=1

#Adding Bomb_Virus blue
            if event.type == KEYDOWN and event.key == K_o:
                if score_blue >= blue_bvirus.cost and bomb_count_blue == 0 and sum(Player2.blue_viruses.values()) < Player2.virus_max:
                    Player2.add_virus(blue_bvirus)
                    score_blue -= blue_bvirus.cost
                else:
                    for comp in comps:
                        if comp.blue_viruses['b'] == 1 and comp.off_state == False:
                            comp.off_state = True
                            comp.scrn_colour = (100,100,100)
                            comp.red_viruses = {'x':0, 'y':0, 'w':0, 'b':0} 
                            comp.blue_viruses['b'] = 0



#Quitting
        if event.type == pygame.QUIT:
            done = True
        elif event.type == KEYDOWN and event.key== K_ESCAPE:
            done = True

#Update

    for comp in comps:
        target_dict = {'x_red':0, 'y_red':0, 'w_red':0, 'b_red':0, 'x_blue':0, 'y_blue':0, 'w_blue':0, 'b_blue':0}
        comp.wipe()
        comp.onoff()

        if comp.blue_viruses['w'] == 0 and not Player1.lose:
            for virus in red_virus_list:
                virus.spread(comp)
        for virus in red_virus_list:
            if virus.type == 'y' and not Player1.lose:
                virus.target(comp, target_dict)

        if comp.red_viruses['w'] == 0 and not Player2.lose:
            for virus in blue_virus_list:
                virus.spread(comp)
        for virus in blue_virus_list:
            if virus.type == 'y' and not Player2.lose:
                virus.target(comp, target_dict)
                
#Killing the target list 
        
        if comp.off_state == False:
            comp.red_viruses['x'] -= target_dict['x_red']
            if comp.red_viruses['x'] < 0:        #So minimum = 0
                comp.red_viruses['x'] = 0
            
            comp.red_viruses['y'] -= target_dict['y_red']
            if comp.red_viruses['y'] < 0:
                comp.red_viruses['y'] = 0

            comp.red_viruses['w'] -= target_dict['w_red']
            if comp.red_viruses['w'] < 0:        
                comp.red_viruses['w'] = 0
            
            comp.red_viruses['b'] -= target_dict['b_red']
            if comp.red_viruses['b'] < 0:
                comp.red_viruses['b'] = 0


            comp.blue_viruses['x'] -= target_dict['x_blue']
            if comp.blue_viruses['x'] < 0:
                comp.blue_viruses['x'] = 0

            comp.blue_viruses['y'] -= target_dict['y_blue']
            if comp.blue_viruses['y'] < 0:
                comp.blue_viruses['y'] = 0

            comp.blue_viruses['w'] -= target_dict['w_blue']
            if comp.blue_viruses['w'] < 0:
                comp.blue_viruses['w'] = 0

            comp.blue_viruses['b'] -= target_dict['b_blue']
            if comp.blue_viruses['b'] < 0:
                comp.blue_viruses['b'] = 0

    bred = 0
    bblue = 0
    for comp in comps:
        bred += comp.red_viruses['b']
        bblue += comp.blue_viruses['b']
    bomb_count_red = bred
    bomb_count_blue = bblue


    for virus in red_virus_list:
        virus.check_home()
    for virus in blue_virus_list:
        virus.check_home()

                




    for comp in comps:
        if comp.off_state == False:

            part_score_red, part_score_blue = comp.score_check()
            
            score_red += part_score_red 
            score_blue += part_score_blue 


    time.sleep(.2)

