#!/usr/bin/env python

import pygame
from pygame.locals import *
from virus import *

pygame.font.init()
smallfont = pygame.font.Font(None, 20)

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
        self.red_viruses = {'x':0}
        
    def draw_rect(self):
        scrn_thick = 4
        comp_screen =  pygame.Rect((self.x+scrn_thick, self.y+scrn_thick), (self.width-scrn_thick*2,self.height-scrn_thick*2))
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        self.scrn_change()
        pygame.draw.rect(self.screen, self.scrn_colour, comp_screen)
    
    def draw_circle(self):
        pygame.draw.circle(self.screen, (0,0,255), self.rect.center, self.cnct_range, 1)

    def draw_lines(self):
        for comp in self.connected_list:
            pygame.draw.aaline(self.screen, (255,0,0), self.rect.center, comp.rect.center, 5)

    def scrn_change(self):
        if sum(self.red_viruses.values()) > 0:
            self.scrn_colour = (255,0,0)
            text = smallfont.render(str(sum(self.red_viruses.values())), True, (0,0,0))
            loc = text.get_rect()
            loc.center = self.rect.center
            self.screen.blit(text,loc)

    def add_virus(self, virus):
        if virus.team == 1:
            self.red_viruses[virus.type] += 1
        
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

class Home_server(Server):

    def team(self):
        pass
        
