#!/usr/bin/env python

import pygame
from pygame.locals import *
from random import randint
from server import *
from time import *

class Virus(object):

    def __init__(self, team):
        self.team = team
        self.spread_chance = 9

        self.is_colour()
        self.is_type()

    def is_type(self):
        pass

    def is_colour(self):
        if self.team == 1:
            self.colour = (255,0,0)
    
    def spread(self, server):
        chance_list = []
        total = server.red_viruses[self.type]
        while total >0 and server.off_state == False:
            chance = randint(0,99)
            chance_list.append(chance)
            total -= 1
        for num in chance_list:
            for comp in server.connected_list:
                if num <= self.spread_chance:
                    comp.add_virus(self)

class XVirus(Virus):

    def is_type(self):
        self.type = 'x'
