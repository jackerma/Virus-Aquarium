#!/usr/bin/env python

import pygame
from pygame import Surface
from pygame.locals import *
from virus import *
from random import randint
import time
from resources import load_image
from pygame.sprite import Sprite, Group

pygame.font.init()
smallfont = pygame.font.Font(None, 20)
scorefont = pygame.font.Font(None, 45)
bigfont = pygame.font.Font(None, 250)
midfont = pygame.font.Font(None, 80)


class Server(Rect):

    def __init__ (self, screen, (x,y)):
        scrn_thick = 6
        self.width = 160
        self.height = 120
        self.x = x
        self.y = y
        self.vx = self.x
        self.vy = self.y
        self.screen = screen
        self.rect = Rect((x,y), (self.width, self.height))
        self.scrn_colour = (255,255,255)
        self.cnct_range = 150
        self.connected_list = [] 

        self.red_viruses = {'x':0, 'y':0, 'w':0, 'b':0} 
        self.blue_viruses = {'x':0, 'y':0, 'w':0, 'b':0}  
        self.red_viruses_old = {'x':0, 'y':0, 'w':0, 'b':0}
        self.blue_viruses_old = {'x':0, 'y':0, 'w':0, 'b':0}


        self.virus_max = 30
                 
        self.off_state = False
        self.lose = False

        self.bounds = self.screen.get_rect()
        self.comp_screen =  pygame.Rect((self.x+scrn_thick, self.y+scrn_thick), (self.width-scrn_thick*2,self.height-scrn_thick*2))
        self.score_blue = 0.0
        self.score_red = 0.0

        self.xplolist_outer = [(self.vx+ 55,self.vy+ 2), (self.vx+ 60,self.vy+ 10), (self.vx+ 65,self.vy+ 2), (self.vx+ 70,self.vy+ 11), (self.vx+ 75,self.vy+ 15), (self.vx+ 75,self.vy+ 25), (self.vx+ 70,self.vy+ 20), (self.vx+65,self.vy+ 22), (self.vx+ 55,self.vy+ 19), (self.vx+ 50,self.vy+ 13)]
        self.xplolist_inner = [(self.vx+60, self.vy+5), (self.vx+ 62,self.y+ 7), (self.vx+ 65,self.vy+ 5), (self.vx+ 67,self.vy+ 8), (self.vx+ 70,self.vy+ 10), (self.vx+ 70,self.vy+ 20), (self.vx+ 67,self.vy+ 15), (self.vx+ 65,self.vy+ 18), (self.vx+ 62,self.vy+ 14), (self.vx+ 61,self.vy+ 8)]

        self.screen_img = load_image("mac1")

    def score_check(self):
        self.score_red = float((self.red_viruses['x']))/10
        self.score_blue = float((self.blue_viruses['x']))/10

        return self.score_red, self.score_blue

    def draw_rect(self):
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        self.scrn_change()
        pygame.draw.rect(self.screen, self.scrn_colour, self.comp_screen)
        self.screen.blit(self.screen_img, (self.x+4,self.y+4))
    
    def draw_circle(self):
#        pygame.draw.circle(self.screen, (0,0,255), self.rect.center, self.cnct_range, 1)
        pass
        


    def draw_lines(self):
        for comp in self.connected_list:
            pygame.draw.aaline(self.screen, (255,0,0), self.rect.center, comp.rect.center, 5)

    def scrn_change(self):
        if self.off_state == True:
            self.screen_img.fill((100,100,100))
        elif self.off_state == False:
            if sum(self.red_viruses.values()) > sum(self.blue_viruses.values()):
                self.scrn_colour = (255,0,0)
                self.screen_img = load_image("macred")
            elif sum(self.blue_viruses.values()) > sum(self.red_viruses.values()):
                self.screen_img = load_image("macblue")
                self.scrn_colour = (0,0,255)
            else:
                self.scrn_colour = (255,255,255)
                self.screen_img = load_image("mac1")

    def draw_text(self):

        ##Red Virus numbers
        if self.red_viruses['x'] < self.red_viruses_old['x']:
            (self.vx, self.vy) = (self.x, self.y)
            self.xplolist_outer = [(self.vx+ 55,self.vy+ 2), (self.vx+ 60,self.vy+ 10), (self.vx+ 65,self.vy+ 2), (self.vx+ 70,self.vy+ 11), (self.vx+ 75,self.vy+ 15), (self.vx+ 75,self.vy+ 25), (self.vx+ 70,self.vy+ 20), (self.vx+65,self.vy+ 22), (self.vx+ 55,self.vy+ 19), (self.vx+ 50,self.vy+ 13)]
            self.xplolist_inner = [(self.vx+60, self.vy+5), (self.vx+ 62,self.y+ 7), (self.vx+ 65,self.vy+ 5), (self.vx+ 67,self.vy+ 8), (self.vx+ 70,self.vy+ 10), (self.vx+ 70,self.vy+ 20), (self.vx+ 67,self.vy+ 15), (self.vx+ 65,self.vy+ 18), (self.vx+ 62,self.vy+ 14), (self.vx+ 61,self.vy+ 8)]
            pygame.draw.polygon(self.screen, (200,0,0), self.xplolist_outer)
            pygame.draw.polygon(self.screen, (200,200,0), self.xplolist_inner)
            time.sleep(.1)
            self.scrn_change()

            self.red_viruses_old['x'] = self.red_viruses['x']
            text = smallfont.render("Xvirus = " + str(self.red_viruses['x']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = self.comp_screen.topleft
            self.screen.blit(text,loc)

        if self.red_viruses['x'] > 0:
            self.red_viruses_old['x'] = self.red_viruses['x']
            text = smallfont.render("Xvirus = " + str(self.red_viruses['x']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = self.comp_screen.topleft
            self.screen.blit(text,loc)


        if self.red_viruses['y'] < self.red_viruses_old['y']:
            (self.vx, self.vy) = (self.x, self.y+ 10)
            self.xplolist_outer = [(self.vx+ 55,self.vy+ 2), (self.vx+ 60,self.vy+ 10), (self.vx+ 65,self.vy+ 2), (self.vx+ 70,self.vy+ 11), (self.vx+ 75,self.vy+ 15), (self.vx+ 75,self.vy+ 25), (self.vx+ 70,self.vy+ 20), (self.vx+65,self.vy+ 22), (self.vx+ 55,self.vy+ 19), (self.vx+ 50,self.vy+ 13)]
            self.xplolist_inner = [(self.vx+60, self.vy+5), (self.vx+ 62,self.y+ 7), (self.vx+ 65,self.vy+ 5), (self.vx+ 67,self.vy+ 8), (self.vx+ 70,self.vy+ 10), (self.vx+ 70,self.vy+ 20), (self.vx+ 67,self.vy+ 15), (self.vx+ 65,self.vy+ 18), (self.vx+ 62,self.vy+ 14), (self.vx+ 61,self.vy+ 8)]
            pygame.draw.polygon(self.screen, (200,0,0), self.xplolist_outer)
            pygame.draw.polygon(self.screen, (200,200,0), self.xplolist_inner)
            time.sleep(.1)
            self.scrn_change()

            self.red_viruses_old['y'] = self.red_viruses['y']
            x,y = self.comp_screen.topleft
            text = smallfont.render("Yvirus = " + str(self.red_viruses['y']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = (x, y + loc.height)
            self.screen.blit(text,loc)

        if self.red_viruses['y'] > 0:
            self.red_viruses_old['y'] = self.red_viruses['y']
            x,y = self.comp_screen.topleft
            text = smallfont.render("Yvirus = " + str(self.red_viruses['y']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = (x, y + loc.height)
            self.screen.blit(text,loc)

        if self.red_viruses['w'] < self.red_viruses_old['w']:
            (self.vx, self.vy) = (self.x, self.y+25)
            self.xplolist_outer = [(self.vx+ 55,self.vy+ 2), (self.vx+ 60,self.vy+ 10), (self.vx+ 65,self.vy+ 2), (self.vx+ 70,self.vy+ 11), (self.vx+ 75,self.vy+ 15), (self.vx+ 75,self.vy+ 25), (self.vx+ 70,self.vy+ 20), (self.vx+65,self.vy+ 22), (self.vx+ 55,self.vy+ 19), (self.vx+ 50,self.vy+ 13)]
            self.xplolist_inner = [(self.vx+60, self.vy+5), (self.vx+ 62,self.y+ 7), (self.vx+ 65,self.vy+ 5), (self.vx+ 67,self.vy+ 8), (self.vx+ 70,self.vy+ 10), (self.vx+ 70,self.vy+ 20), (self.vx+ 67,self.vy+ 15), (self.vx+ 65,self.vy+ 18), (self.vx+ 62,self.vy+ 14), (self.vx+ 61,self.vy+ 8)]
            pygame.draw.polygon(self.screen, (200,0,0), self.xplolist_outer)
            pygame.draw.polygon(self.screen, (200,200,0), self.xplolist_inner)
            time.sleep(.1)
            self.scrn_change()

            self.red_viruses_old['w'] = self.red_viruses['w']

            x,y = self.comp_screen.topleft
            text = smallfont.render("Wall = " + str(self.red_viruses['w']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = (x, y + loc.height*2)
            self.screen.blit(text,loc)

        if self.red_viruses['w'] > 0:
            self.red_viruses_old['w'] = self.red_viruses['w']
            x,y = self.comp_screen.topleft
            text = smallfont.render("Wall = " + str(self.red_viruses['w']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = (x, y + loc.height*2)
            self.screen.blit(text,loc)

        if self.red_viruses['b'] > 0:
            self.red_viruses_old['b'] = self.red_viruses['b']
            x,y = self.comp_screen.topleft
            text = smallfont.render("Bomb = " + str(self.red_viruses['b']), True, (255,0,0))
            loc = text.get_rect()
            loc.topleft = (x, y + loc.height *3)
            self.screen.blit(text,loc)



        ##Blue Virus numbers  
        if self.blue_viruses['x'] < self.blue_viruses_old['x']:
            (self.vx, self.vy) = (self.x+80, self.y)
            self.xplolist_outer = [(self.vx+ 55,self.vy+ 2), (self.vx+ 60,self.vy+ 10), (self.vx+ 65,self.vy+ 2), (self.vx+ 70,self.vy+ 11), (self.vx+ 75,self.vy+ 15), (self.vx+ 75,self.vy+ 25), (self.vx+ 70,self.vy+ 20), (self.vx+65,self.vy+ 22), (self.vx+ 55,self.vy+ 19), (self.vx+ 50,self.vy+ 13)]
            self.xplolist_inner = [(self.vx+60, self.vy+5), (self.vx+ 62,self.y+ 7), (self.vx+ 65,self.vy+ 5), (self.vx+ 67,self.vy+ 8), (self.vx+ 70,self.vy+ 10), (self.vx+ 70,self.vy+ 20), (self.vx+ 67,self.vy+ 15), (self.vx+ 65,self.vy+ 18), (self.vx+ 62,self.vy+ 14), (self.vx+ 61,self.vy+ 8)]
           
            self.blue_viruses_old['x'] = self.blue_viruses['x']
            pygame.draw.polygon(self.screen, (200,0,0), self.xplolist_outer)
            pygame.draw.polygon(self.screen, (200,200,0), self.xplolist_inner)
            time.sleep(.1)
            self.scrn_change()


            if self.blue_viruses['x'] > 0:
                self.blue_viruses_old['x'] = self.blue_viruses['x']
                text = smallfont.render("Xvirus = " + str(self.blue_viruses['x']), True, (0,0,255))
                loc = text.get_rect()
                loc.topright = self.comp_screen.topright
                self.screen.blit(text,loc)
  
        if self.blue_viruses['x'] > 0:
            self.blue_viruses_old['x'] = self.blue_viruses['x']
            text = smallfont.render("Xvirus = " + str(self.blue_viruses['x']), True, (0,0,255))
            loc = text.get_rect()
            loc.topright = self.comp_screen.topright
            self.screen.blit(text,loc)

        if self.blue_viruses['y'] < self.blue_viruses_old['y']:
            (self.vx, self.vy) = (self.x+80, self.y+ 10)
            self.xplolist_outer = [(self.vx+ 55,self.vy+ 2), (self.vx+ 60,self.vy+ 10), (self.vx+ 65,self.vy+ 2), (self.vx+ 70,self.vy+ 11), (self.vx+ 75,self.vy+ 15), (self.vx+ 75,self.vy+ 25), (self.vx+ 70,self.vy+ 20), (self.vx+65,self.vy+ 22), (self.vx+ 55,self.vy+ 19), (self.vx+ 50,self.vy+ 13)]
            self.xplolist_inner = [(self.vx+60, self.vy+5), (self.vx+ 62,self.y+ 7), (self.vx+ 65,self.vy+ 5), (self.vx+ 67,self.vy+ 8), (self.vx+ 70,self.vy+ 10), (self.vx+ 70,self.vy+ 20), (self.vx+ 67,self.vy+ 15), (self.vx+ 65,self.vy+ 18), (self.vx+ 62,self.vy+ 14), (self.vx+ 61,self.vy+ 8)]

            self.blue_viruses_old['y'] = self.blue_viruses['y']
            pygame.draw.polygon(self.screen, (200,0,0), self.xplolist_outer)
            pygame.draw.polygon(self.screen, (200,200,0), self.xplolist_inner)
            time.sleep(.1)
            self.scrn_change()

            if self.blue_viruses['y'] > 0:
                x, y = self.comp_screen.topright
                text = smallfont.render("Yvirus = " + str(self.blue_viruses['y']), True, (0,0,255))
                loc = text.get_rect()
                loc.topright = (x, y+loc.height)
                self.screen.blit(text,loc)

        if self.blue_viruses['y'] > 0:
            self.blue_viruses_old['y'] = self.blue_viruses['y']
            x, y = self.comp_screen.topright
            text = smallfont.render("Yvirus = " + str(self.blue_viruses['y']), True, (0,0,255))
            loc = text.get_rect()
            loc.topright = (x, y+loc.height)
            self.screen.blit(text,loc)

        if self.blue_viruses['w'] < self.blue_viruses_old['w']:
            (self.vx, self.vy) = (self.x+80, self.y+ 25)
            self.xplolist_outer = [(self.vx+ 55,self.vy+ 2), (self.vx+ 60,self.vy+ 10), (self.vx+ 65,self.vy+ 2), (self.vx+ 70,self.vy+ 11), (self.vx+ 75,self.vy+ 15), (self.vx+ 75,self.vy+ 25), (self.vx+ 70,self.vy+ 20), (self.vx+65,self.vy+ 22), (self.vx+ 55,self.vy+ 19), (self.vx+ 50,self.vy+ 13)]
            self.xplolist_inner = [(self.vx+60, self.vy+5), (self.vx+ 62,self.y+ 7), (self.vx+ 65,self.vy+ 5), (self.vx+ 67,self.vy+ 8), (self.vx+ 70,self.vy+ 10), (self.vx+ 70,self.vy+ 20), (self.vx+ 67,self.vy+ 15), (self.vx+ 65,self.vy+ 18), (self.vx+ 62,self.vy+ 14), (self.vx+ 61,self.vy+ 8)]

            self.blue_viruses_old['w'] = self.blue_viruses['w']
            pygame.draw.polygon(self.screen, (200,0,0), self.xplolist_outer)
            pygame.draw.polygon(self.screen, (200,200,0), self.xplolist_inner)
            time.sleep(.1)
            self.scrn_change()

            if self.blue_viruses['w'] > 0:
                x, y = self.comp_screen.topright
                text = smallfont.render("Wall = " + str(self.blue_viruses['w']), True, (0,0,255))
                loc = text.get_rect()
                loc.topright = (x, y+loc.height*2)
                self.screen.blit(text,loc)

        if self.blue_viruses['w'] > 0:
            self.blue_viruses_old['w'] = self.blue_viruses['w']
            x, y = self.comp_screen.topright
            text = smallfont.render("Wall = " + str(self.blue_viruses['w']), True, (0,0,255))
            loc = text.get_rect()
            loc.topright = (x, y+loc.height*2)
            self.screen.blit(text,loc)



        if self.blue_viruses['b'] > 0:
            self.blue_viruses_old['b'] = self.blue_viruses['b']
            x,y = self.comp_screen.topright
            text = smallfont.render("Bomb = " + str(self.blue_viruses['b']), True, (0,0,255))
            loc = text.get_rect()
            loc.topright = (x, y + loc.height *3)
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
            self.scrn_change()
        if off_chance >= 989 and self.off_state == True:
            self.off_state = False
            self.scrn_change()

    
    def wipe (self):
        #if randint(0,999) < 4:

         #   self.red_viruses = {'x':0, 'y':0, 'w':0, 'b':0} 
          #  self.blue_viruses = {'x':0, 'y':0, 'w':0, 'b':0}
        pass

    def count (self, score):
        pass

    def draw_limits(self):
        pass


class Home_server(Server):


    def draw_rect(self):
        scrn_thick = 8
        comp_screen =  pygame.Rect((self.x+scrn_thick, self.y+scrn_thick), (self.width-scrn_thick*2,self.height-scrn_thick*2))
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        self.scrn_change()
        pygame.draw.rect(self.screen, self.scrn_colour, self.comp_screen)
        self.screen.blit(self.screen_img, (self.x+(scrn_thick/2),self.y+(scrn_thick/2)))


    def onoff(self):
        pass

    def wipe(self):
        pass
        
    def is_team(self, num):
        self.team = num
        if self.team == 1:
            self.color = (255,0,0)
        elif self.team == 2:
            self.color = (0,0,255)
        
    def scrn_change(self):
        if self.off_state == False:
            if self.team == 1:
                if sum(self.red_viruses.values()) > sum(self.blue_viruses.values()):
                    self.scrn_colour = (255,0,0)
                    self.screen_img = load_image("macred")

                elif sum(self.blue_viruses.values()) > sum(self.red_viruses.values()):
                    self.scrn_colour = (0,0,255)
                    self.screen_img = load_image("macblue")
                    self.lose = True
                    text = bigfont.render("Blue Wins!", True, (0,0,255))
                    loc = text.get_rect()
                    loc.center = self.bounds.center
                    self.screen.blit(text,loc)

                    text = midfont.render("Press 'esc' to return to menu", True, (0,0,255))
                    loc = text.get_rect()
                    (x, y)= self.bounds.center
                    loc.center = (x, y + 100)
                    self.screen.blit(text,loc)


                else:
                    self.scrn_colour = (255,255,255)
                    self.screen_img = load_image("mac1")

            if self.team == 2:
                if sum(self.red_viruses.values()) > sum(self.blue_viruses.values()):
                    self.scrn_colour = (255,0,0)
                    self.screen_img = load_image("macred")
                    self.lose = True
                    text = bigfont.render("Red Wins!", True, (255,0,0))
                    loc = text.get_rect()
                    loc.center = self.bounds.center
                    self.screen.blit(text,loc)

                    text = midfont.render("Press 'esc' to return to menu", True, (255,0,0))
                    loc = text.get_rect()
                    (x, y)= self.bounds.center
                    loc.center = (x, y + 100)
                    self.screen.blit(text,loc)

                elif sum(self.blue_viruses.values()) > sum(self.red_viruses.values()):
                    self.scrn_colour = (0,0,255)
                    self.screen_img = load_image("macblue")
                else:
                    self.scrn_colour = (255,255,255)
                    self.screen_img = load_image("mac1")

    def onoff (self):
        off_chance = randint(0,999)
        if off_chance >= 9 and self.off_state == True:
            self.off_state = False
            self.scrn_change()

    def draw_limits(self):
        if self.team == 1: 
            p,q = self.comp_screen.bottomleft
            j,k = self.comp_screen.center
            limit = smallfont.render("Total: " + str(sum(self.red_viruses.values())) + " / " + str(self.virus_max), True, (255,0,0))
            lim_rect = limit.get_rect()
            lim_rect.center = j, q - 5
            self.screen.blit(limit,lim_rect)
        if self.team == 2: 
            p,q = self.comp_screen.bottomleft
            j,k = self.comp_screen.center
            limit = smallfont.render("Total: " + str(sum(self.blue_viruses.values())) + " / " + str(self.virus_max), True, (0,0,255))
            lim_rect = limit.get_rect()
            lim_rect.center = j, q - 5
            self.screen.blit(limit,lim_rect)


    def blue_lose(self):
        self.lose = True
        text = bigfont.render("Blue Wins!", True, (0,0,255))
        loc = text.get_rect()
        loc.center = self.bounds.center
        self.screen.blit(text,loc)

        text = midfont.render("Press 'esc' to return to menu", True, (0,0,255))
        loc = text.get_rect()
        (x, y)= self.bounds.center
        loc.center = (x, y + 100)
        self.screen.blit(text,loc)


    def red_lose(self):
        self.lose = True
        text = bigfont.render("Red Wins!", True, (255,0,0))
        loc = text.get_rect()
        loc.center = self.bounds.center
        self.screen.blit(text,loc)

        text = midfont.render("Press 'esc' to return to menu", True, (255,0,0))
        loc = text.get_rect()
        (x, y)= self.bounds.center
        loc.center = (x, y + 100)
        self.screen.blit(text,loc)

                      
