#!/usr/bin/env python

import pygame
from pygame.locals import *
from random import randint
from server import *
from time import *
from resource import load_sfx

target_dict ={}
last_comp_red = 0
last_comp_blue = 0


class Virus(object):

    def __init__(self, team, home):
        self.team = team
        self.home = home
        self.target_dict = target_dict
        self.has_spread_chance()
        self.is_colour()
        self.is_type()
        self.costs()
        self.check_home()

    def check_home(self):
        if self.team == 1:
            self.home_number = self.home.red_viruses[self.type]
        if self.team == 2:
            self.home_number = self.home.blue_viruses[self.type]
        self.max = self.home_number
        
    def costs(self):
        pass


    def is_type(self):
        pass

    def has_max(self):
        pass
    
    def target(self, server, target_dict):
        pass
    
    def has_spread_chance(self):
        pass

    def is_colour(self):
        if self.team == 1:
            self.colour = (255,0,0)
        if self.team == 2:
            self.colour = (0,0,255)
    
    def spread(self, server):
        if self.team == 1:
            red_chance_list = []
            total_red = server.red_viruses[self.type]
            while total_red >0 and server.off_state == False:
                red_chance = randint(0,900)
                red_chance_list.append(red_chance)
                total_red -= 1
            for num in red_chance_list:
                for comp in server.connected_list:
                    if num <= self.spread_chance:
                        if comp != self.home:  
                            comp.add_virus(self)
        
        if self.team == 2:
            blue_chance_list = []
            total_blue = server.blue_viruses[self.type]
            while total_blue > 0 and server.off_state == False:
                blue_chance = randint(0,900)
                blue_chance_list.append(blue_chance)
                total_blue -= 1
            for num in blue_chance_list:
                for comp in server.connected_list:
                    if num <= self.spread_chance:
                        if comp != self.home:  
                            comp.add_virus(self)

class XVirus(Virus):

    def is_type(self):
        self.type = 'x'

    def has_max(self):
        self.max = 50

    def has_spread_chance(self):
        self.spread_chance = 14

    def costs(self):
        self.cost = 50


class YVirus(Virus):

    def is_type(self):
        self.type = 'y'

    def has_max(self):
        self.max = 30
        
    def has_spread_chance(self):
        self.spread_chance = 9

    def costs(self):
        self.cost = 150

    def target(self, server, target_dict):
        i = randint(0,499)
        j = randint(0,4)
        if self.team == 1 and server.red_viruses['y'] > 0:
            hit_chance = 1
            if hit_chance <= i:
                if j < 2:
                    if server.blue_viruses['y'] > 0:
                        target_dict['y_blue']+= server.red_viruses['y']
                    elif server.blue_viruses['x'] > 0:
                        target_dict['x_blue'] += (server.red_viruses['y']-1)
                    elif server.blue_viruses['w'] > 0:
                        target_dict['w_blue'] += 1

                elif j == 2:
                    target_dict['x_blue']+= server.red_viruses['y']
                    target_dict['w_blue']+= 1

                elif j > 2:
                    if server.blue_viruses['x'] > 0:
                        target_dict['x_blue']+= server.red_viruses['y']
                    elif server.blue_viruses['y'] > 0:
                        target_dict['y_blue'] += (server.red_viruses['y']-1)
                    elif server.blue_viruses['w'] > 0:
                        target_dict['w_blue'] += 1


        if self.team == 2 and server.blue_viruses['y'] > 0:
            hit_chance =  1
            if hit_chance <= i:
                if j < 2:
                    if server.red_viruses['y'] > 0:
                        target_dict['y_red']+= server.blue_viruses['y']
                    elif server.red_viruses['x'] > 0:
                        target_dict['x_red'] += server.blue_viruses['y']
                elif j == 2:
                    target_dict['x_red']+= server.blue_viruses['y']
                    target_dict['w_red']+= 1

                elif j > 2:
                    if server.red_viruses['x'] > 0:
                        target_dict['x_red']+= server.blue_viruses['y']
                    elif server.red_viruses['y'] > 0:
                        target_dict['y_red'] += server.blue_viruses['y']
 


class Wall_Virus(Virus):

    def is_type(self):
        self.type = 'w'
    
    def has_max(self):
        self.max = 50
    
    def costs(self):
        self.cost = 500
            
    def has_spread_chance(self):
        self.spread_chance = 6


class Bomb_Virus(Virus):

    def __init__(self, team, home):
        self.team = team
        self.home = home
        self.target_dict = target_dict
        self.has_spread_chance()
        self.is_colour()
        self.is_type()
        self.max = 1
        self.costs()

        self.z_red = 0
        self.z_blue = 0

    def check_home(self):
        pass

    def check_home(self):
        pass

    def is_type(self):
        self.type = 'b'
    
    def costs(self):
        self.cost = 1000

    def has_spread_chance(self):
        self.spread_chance = 10

    def spread(self, server):
        global last_comp_red
        global last_comp_blue
        sfx_move = load_sfx("bombmove")


        if self.team == 1:
            red_chance_list = []

            total_red = server.red_viruses[self.type]
            while total_red >0 and server.off_state == False:

                red_chance = randint(0,99)
                red_chance_list.append(red_chance)
                total_red -= 1
            i = randint(0,99)
            for num in red_chance_list:
                for comp in server.connected_list:
                    if num <= self.spread_chance and server.red_viruses[self.type] != 0:

                        if i < (float(server.connected_list.index(comp)+1)/float(len(server.connected_list)))*100 and i > (float((server.connected_list.index(comp)))/float(len(server.connected_list)))*100 and comp.off_state == False and comp.red_viruses[self.type] < self.max :
                            if self.z_red != 0:
                                if comp != last_comp_red:
                                    last_comp_red = server   
                                    server.red_viruses[self.type] = 0
                                    comp.add_virus(self)
                                    self.z_red =+1
                                   # sfx_move.stop()
                                   # sfx_move.play()

                            else:
                                last_comp_red = server   
                                server.red_viruses[self.type] = 0
                                comp.add_virus(self)
                                self.z_red =+1




###########

        if self.team == 2:
            blue_chance_list = []

            total_blue = server.blue_viruses[self.type]
            while total_blue > 0 and server.off_state == False:

                blue_chance = randint(0,99)
                blue_chance_list.append(blue_chance)
                total_blue -= 10
            i = randint(0,99)
            for num in blue_chance_list:
                for comp in server.connected_list:
                    if num <= self.spread_chance and server.blue_viruses[self.type] != 0:
                         
                         if i < (float(server.connected_list.index(comp)+1)/float(len(server.connected_list)))*100 and i > (float((server.connected_list.index(comp)))/float(len(server.connected_list)))*100 and comp.off_state == False and comp.blue_viruses[self.type] < self.max:

                                 if self.z_blue != 0:
                                     if comp != last_comp_blue:
                                         last_comp_blue = server   
                                         server.blue_viruses[self.type] = 0
                                         comp.add_virus(self)
                                         self.z_blue =+1
                                      #   sfx_move.stop()
                                       #  sfx_move.play()

                                 else:
                                     last_comp_blue = server 
                                     server.blue_viruses[self.type] = 0  
                                     comp.add_virus(self)
                                     self.z_blue =+1


