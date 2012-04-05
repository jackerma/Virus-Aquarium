#!/usr/bin/env python

import pygame
from pygame.locals import *

class Server(Rect):

    def __init__ (self, screen, (x,y)):
        self.width = 160
        self.height = 120
        self.x = x
        self.y = y
        self.screen = screen
        self.rect = Rect((x,y), (self.width, self.height))
        self.scrn_colour = (255,255,255)
        self.cnct_range = 150
        self.connected_list = [] 
        
    
    def draw_rect(self):
        scrn_thick = 4
        comp_screen =  pygame.Rect((self.x+scrn_thick, self.y+scrn_thick), (self.width-scrn_thick*2,self.height-scrn_thick*2))
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        pygame.draw.rect(self.screen, self.scrn_colour, comp_screen)
    
    def draw_circle(self):
        pygame.draw.circle(self.screen, (0,0,255), self.rect.center, self.cnct_range, 1)

    def draw_lines(self):
        for comp in self.connected_list:
            pygame.draw.aaline(self.screen, (255,0,0), self.rect.center, comp.rect.center, 5)

        
    def onoff (self):
        pass
    
    def wipe (self):
        pass
    
    def player1app (self, virus):
        pass
    
    def player2app (self, virus):
        pass
    
    def count (self):
        pass

