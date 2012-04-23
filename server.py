#!/usr/bin/env python

import pygame
from pygame.locals import *
from virus import *
from random import randint
import time


pygame.font.init()
smallfont = pygame.font.Font(None, 20)
scorefont = pygame.font.Font(None, 50)
bigfont = pygame.font.Font(None, 250)

class Server(Rect):

    def __init__ (self, screen, (x,y)):
        scrn_thick = 4
        self.width = 160
        self.height = 120
        self.x = x
        self.y = y
        self.screen = screen
        self.rect = Rect((x,y), (self.width, self.height))
        self.scrn_colour = (255,255,255)
        self.cnct_range = 150
        self.connected_list = [] 

        self.red_viruses = {'x':0, 'y':0, 'w':0, 'b':0} 
        self.blue_viruses = {'x':0, 'y':0, 'w':0, 'b':0}  
        self.virus_max = 30
                 
        self.off_state = False
        self.lose = False

        self.bounds = self.screen.get_rect()
        self.comp_screen =  pygame.Rect((self.x+scrn_thick, self.y+scrn_thick), (self.width-scrn_thick*2,self.height-scrn_thick*2))
        self.score_blue = 0
        self.score_red = 0
        self.spread_occ_red = 0
        self.spread_occ_blue = 0
        
    def score_check(self):
        self.score_red = self.red_viruses['x']
        self.score_blue = self.blue_viruses['x']

        return self.score_red, self.score_blue

    def draw_rect(self):
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        self.scrn_change()
        pygame.draw.rect(self.screen, self.scrn_colour, self.comp_screen)

    
    def draw_circle(self):
#        pygame.draw.circle(self.screen, (0,0,255), self.rect.center, self.cnct_range, 1)
        pass
        


    def draw_lines(self):
        for comp in self.connected_list:
            pygame.draw.aaline(self.screen, (255,0,0), self.rect.center, comp.rect.center, 5)

    def scrn_change(self):
        if self.off_state == False:
            if sum(self.red_viruses.values()) > sum(self.blue_viruses.values()):
                self.scrn_colour = (255,175,175)
            elif sum(self.blue_viruses.values()) > sum(self.red_viruses.values()):
                self.scrn_colour = (175,175,255)
            else:
                self.scrn_colour = (255,255,255)


    def draw_text(self):

        ##Red Virus numbers
        if self.red_viruses['x'] > 0:
            text = smallfont.render("Xvirus = " + str(self.red_viruses['x']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = self.comp_screen.topleft
            self.screen.blit(text,loc)

        if self.red_viruses['y'] > 0:
            x,y = self.comp_screen.topleft
            text = smallfont.render("Yvirus = " + str(self.red_viruses['y']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = (x, y + loc.height)
            self.screen.blit(text,loc)

        if self.red_viruses['w'] > 0:
            x,y = self.comp_screen.topleft
            text = smallfont.render("Wall = " + str(self.red_viruses['w']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = (x, y + loc.height*2)
            self.screen.blit(text,loc)

        if self.red_viruses['b'] > 0:
            x,y = self.comp_screen.topleft
            text = smallfont.render("Bomb = " + str(self.red_viruses['b']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = (x, y + loc.height *3)
            self.screen.blit(text,loc)

        ##Blue Virus numbers    
        if self.blue_viruses['x'] > 0:
            text = smallfont.render("Xvirus = " + str(self.blue_viruses['x']), True, (0,0,255))
            loc = text.get_rect()
            loc.topright = self.comp_screen.topright
            self.screen.blit(text,loc)
        
        if self.blue_viruses['y'] > 0:
            x, y = self.comp_screen.topright
            text = smallfont.render("Yvirus = " + str(self.blue_viruses['y']), True, (0,0,255))
            loc = text.get_rect()
            loc.topright = (x, y+loc.height)
            self.screen.blit(text,loc)

        if self.blue_viruses['w'] > 0:
            x,y = self.comp_screen.topright
            text = smallfont.render("Wall = " + str(self.blue_viruses['w']), True, (0,0,255))
            loc = text.get_rect()
            loc.topright = (x, y + loc.height*2)
            self.screen.blit(text,loc)

        if self.blue_viruses['b'] > 0:
            x,y = self.comp_screen.topright
            text = smallfont.render("Bomb = " + str(self.blue_viruses['b']), True, (0,0,255))
            loc = text.get_rect()
            loc.topright = (x, y + loc.height*3)
            self.screen.blit(text,loc)


    def add_virus(self, virus):


        if virus.team == 1 and self.red_viruses[virus.type] < virus.max and self.off_state == False: 
            self.red_viruses[virus.type] += 1

        if virus.team == 2 and self.blue_viruses[virus.type] < virus.max and self.off_state == False:
            self.blue_viruses[virus.type] += 1


        
    def onoff (self):
        off_chance = randint(0,999)
        if off_chance <= 1 and self.off_state == False:
            self.off_state = True
            self.scrn_colour = (100,100,100)
        if off_chance >= 989 and self.off_state == True:
            self.off_state = False
            self.scrn_change()

    
    def wipe (self):
        if sum(self.red_viruses.values()) >= self.virus_max and sum(self.blue_viruses.values()) >= self.virus_max and randint(0,99) < 5:

            self.red_viruses = {'x':0, 'y':0, 'w':0, 'b':0} 
            self.blue_viruses = {'x':0, 'y':0, 'w':0, 'b':0}

    
    def player1app (self, virus):
        pass
    
    def player2app (self, virus):
        pass
    
    def count (self, score):
        pass



class Home_server(Server):

    def draw_rect(self):
        scrn_thick = 7
        comp_screen =  pygame.Rect((self.x+scrn_thick, self.y+scrn_thick), (self.width-scrn_thick*2,self.height-scrn_thick*2))
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        self.scrn_change()
        pygame.draw.rect(self.screen, self.scrn_colour, self.comp_screen)
    
    def onoff(self):
        pass

    def wipe(self):
        pass
        
    def is_team(self, num):
        self.team = num
        
    def scrn_change(self):
        if self.off_state == False:
            if self.team == 1:
                if sum(self.red_viruses.values()) > sum(self.blue_viruses.values()):
                    self.scrn_colour = (255,175,175)

                elif sum(self.blue_viruses.values()) > sum(self.red_viruses.values()):
                    self.scrn_colour = (175,175,255)
                    time.sleep(.2)
                    self.lose = True
                    text = bigfont.render("Blue Wins!", True, (0,0,255))
                    loc = text.get_rect()
                    loc.center = self.bounds.center
                    self.screen.blit(text,loc)



                else:
                    self.scrn_colour = (255,255,255)

            if self.team == 2:
                if sum(self.red_viruses.values()) > sum(self.blue_viruses.values()):
                    self.scrn_colour = (255,175,175)
                    time.sleep(.2)
                    self.lose = True
                    text = bigfont.render("Red Wins!", True, (255,0,0))
                    loc = text.get_rect()
                    loc.center = self.bounds.center
                    self.screen.blit(text,loc)



                elif sum(self.blue_viruses.values()) > sum(self.red_viruses.values()):
                    self.scrn_colour = (175,175,255)

                else:
                    self.scrn_colour = (255,255,255)

    def onoff (self):
        off_chance = randint(0,999)
        if off_chance >= 9 and self.off_state == True:
            self.off_state = False
            self.scrn_change()
