#!/usr/bin/env python

import pygame
from pygame.locals import *
from random import randint
from server import *
from time import *

target_dict ={}

class Virus(object):

    def __init__(self, team):
        self.team = team
        self.target_dict = target_dict
        self.has_spread_chance()
        self.is_colour()
        self.is_type()

    def is_type(self):
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
                red_chance = randint(0,99)
                red_chance_list.append(red_chance)
                total_red -= 1
            for num in red_chance_list:
                for comp in server.connected_list:
                    if num <= self.spread_chance:
                        comp.add_virus(self)
        
        if self.team == 2:
            blue_chance_list = []
            total_blue = server.blue_viruses[self.type]
            while total_blue > 0 and server.off_state == False:
                blue_chance = randint(0,99)
                blue_chance_list.append(blue_chance)
                total_blue -= 1
            for num in blue_chance_list:
                for comp in server.connected_list:
                    if num <= self.spread_chance:
                        comp.add_virus(self)

class XVirus(Virus):

    def is_type(self):
        self.type = 'x'

    def has_spread_chance(self):
        self.spread_chance = 9


class YVirus(Virus):          ##All New Below

    
    def is_type(self):
        self.type = 'y'
        
    def has_spread_chance(self):
        self.spread_chance = 5

    def target(self, server, target_dict):
        i = randint(0,9)
        j = randint(0,1)
        if self.team == 1 and server.red_viruses['y'] > 0:
            hit_chance = 1
            if hit_chance <= i:
                if j == 1:
                    target_dict['x_blue']+= server.red_viruses['y']
                elif j == 0:
                    target_dict['y_blue']+= server.red_viruses['y']

        if self.team == 2 and server.blue_viruses['y'] > 0:
            hit_chance =  1
            if hit_chance <= i:
                if j == 1:
                    target_dict['x_red']+= server.blue_viruses['y']
                elif j == 0:
                    target_dict['y_red']+= server.blue_viruses['y']

