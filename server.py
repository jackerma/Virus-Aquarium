#!/usr/bin/env python

import pygame
from pygame.locals import *
from virus import *
from random import randint

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
#        self.blue_viruses = {'x':0}
        self.virus_max = 25
        self.off_state = False


    def draw_rect(self):
        scrn_thick = 4
        comp_screen =  pygame.Rect((self.x+scrn_thick, self.y+scrn_thick), (self.width-scrn_thick*2,self.height-scrn_thick*2))
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        self.scrn_change()
        pygame.draw.rect(self.screen, self.scrn_colour, comp_screen)
        self.draw_text(comp_screen)
    
    def draw_circle(self):
#        pygame.draw.circle(self.screen, (0,0,255), self.rect.center, self.cnct_range, 1)
        pass

    def draw_lines(self):
        for comp in self.connected_list:
            pygame.draw.aaline(self.screen, (255,0,0), self.rect.center, comp.rect.center, 5)

    def scrn_change(self):
        if self.off_state == False:
            if sum(self.red_viruses.values()) > 0:
                self.scrn_colour = (255,175,175)
#            elif sum(self.blue_viruses.values()) > 0:
#                self.scrn_colour = (175,175,255)
            else:
                self.scrn_colour = (255,255,255)

    def draw_text(self, comp_screen):
        if sum(self.red_viruses.values()) > 0:
            text = smallfont.render("Xvirus = " + str(sum(self.red_viruses.values())), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = comp_screen.topleft
            self.screen.blit(text,loc)
            



    def add_virus(self, virus):
        if virus.team == 1 and self.red_viruses['x']< self.virus_max and self.off_state == False:
            self.red_viruses[virus.type] += 1

#        elif virus.team == 21 and self.blue_viruses['x']< self.virus_max and self.off_state == False:
#            self.blue_viruses[virus.type] += 1
        
    def onoff (self):
        off_chance = randint(0,999)
        if off_chance <= 1 and self.off_state == False:
            self.off_state = True
            self.scrn_colour = (100,100,100)
        if off_chance >= 989 and self.off_state == True:
            self.off_state = False
            self.scrn_change()

    
    def wipe (self):
        if self.red_viruses['x'] >= 25 and randint(0,9) >5:
            self.red_viruses['x'] = 0
    
    def player1app (self, virus):
        pass
    
    def player2app (self, virus):
        pass
    
    def count (self, score):
#        if self.off_state == False:
#            virus_count = self.red_viruses['x']

#            return virus_count
        pass

class Home_server(Server):

    def draw_rect(self):
        scrn_thick = 7
        comp_screen =  pygame.Rect((self.x+scrn_thick, self.y+scrn_thick), (self.width-scrn_thick*2,self.height-scrn_thick*2))
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        self.scrn_change()
        pygame.draw.rect(self.screen, self.scrn_colour, comp_screen)
        self.draw_text(comp_screen)
    
    def onoff(self):
        pass

    def wipe(self):
        pass
        
    def team(self):
        pass
        
