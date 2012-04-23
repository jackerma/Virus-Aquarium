#!/usr/bin/env python

#Maps

import pygame
from pygame.locals import *
from server import *
from virus import *
import time

class Map(object):

    def __init__(self, scrn, num):
        self.screen = scrn
        self.num = num
        self.drawmap()


    def drawmap(self):
        screen = self.screen
         
    #Line
        if self.num == '1':
            self.Player1 = Home_server(screen, (50,350))
            self.Player1.is_team(1)
            self.Player2 = Home_server(screen, (1100, 350))
            self.Player2.is_team(2)
            comp1 = Server(screen, (300, 350))
            comp2 = Server(screen, (575, 350))
            comp3 = Server(screen, (850, 350))
            self.comps = [self.Player1, self.Player2, comp1,comp2, comp3]
      
    #X-R0ads
        elif self.num == '2':
            self.Player1 = Home_server(self.screen, (20,20))
            self.Player1.is_team(1)
            self.Player2 = Home_server(self.screen, (1120, 550))
            self.Player2.is_team(2)
            comp1 = Server(screen, (100, 305))
            comp2 = Server(screen, (550, 325))
            comp3 = Server(screen, (350, 160))
            comp4 = Server(screen, (750, 160))
            comp5 = Server(screen, (750, 470))
            comp6 = Server(screen, (1000, 305))
            comp7 = Server(screen, (350, 470))
            self.comps = [self.Player1, self.Player2, comp1,comp2, comp3, comp4, comp5, comp6, comp7]
    #Bridge
        elif self.num == '3':
            self.Player1 = Home_server(self.screen, (20,20))
            self.Player1.is_team(1)
            self.Player2 = Home_server(self.screen, (1120,20))
            self.Player2.is_team(2)
            comp1 = Server(screen, (100, 305))
            comp2 = Server(screen, (390, 325))
            comp3 = Server(screen, (290, 120))
            comp4 = Server(screen, (580, 500))
            comp5 = Server(screen, (750, 325))
            comp6 = Server(screen, (850, 120))
            comp7 = Server(screen, (1040, 305))
            comp8 = Server(screen, (150, 505))
            comp9 = Server(screen, (990, 505))
            self.comps = [self.Player1, self.Player2, comp1,comp2, comp3, comp4, comp5, comp6, comp7, comp8, comp9]
            
        else:
            self.num = str(randint(1,2))
            self.drawmap()
