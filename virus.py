#!/usr/bin/env python

import pygame
from pygame.locals import *
from random import randint
from server import *

class Virus(object):

    def __init__(self, team):
        self.team = team

        self.is_colour()
        self.is_type()

    def is_type(self):
        pass

    def is_colour(self):
        if self.team == 1:
            self.colour = (255,0,0)


class XVirus(Virus):

    def is_type(self):
        self.type = 'x'
