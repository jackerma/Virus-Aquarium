#!usr/bin/env python

import os

import pygame
from resource import load_image, play_song, load_sfx
from pygame.locals import *
from server import *
from virus import *
import time
from maps import *

class Menu(object):

    def __init__(self, screen):
        self.screen = screen
        self.bounds = self.screen.get_rect()
        self.title_font = pygame.font.Font(None, 170)
        self.menu_font = pygame.font.Font(None, 70)
        self.maps_font = pygame.font.Font(None, 50)
        self.background_colour = (0, 0, 0)
        self.menu_off = False
        self.main = True
        self.maps = False
        self.map = None
        self.controls = False
        self.rules = False
        play_song("Chopin")

        self.items = ["Play", "Controls","Rules"]
        self.rects = []
        while self.menu_off == False:
            self.update()
        pygame.mixer.music.stop()

    def update(self):
        self.draw()
        self.inputs()

    def draw(self):
        if self.main == True:
            self.screen.fill(self.background_colour)
            title = self.title_font.render("VIRUS AQUARIUM", True, (0, 255, 0))
            centerx, centery = self.bounds.center
            loc = title.get_rect()
            loc.center = (centerx, centery - 200)
            self.screen.blit(title, loc)
            self.items = ["Play", "Controls", "Rules"]
            self.rects = []
            
            for item in self.items:
                option = self.menu_font.render(item, True, (0, 255, 0))
                x, y = self.bounds.center
                loc = option.get_rect()
                loc.center = (x, (y+100) + loc.height*2*self.items.index(item))
                self.buttonize(loc)
                self.screen.blit(option, loc)
                if loc not in self.rects:
                    self.rects.append(loc)

        elif self.maps == True:
            self.screen.fill(self.background_colour)
            title = self.title_font.render("Select Map", True, (0, 255, 0))
            centerx, centery = self.bounds.center
            loc = title.get_rect()
            loc.center = (centerx, centery - 200)
            self.draw_back()
            self.screen.blit(title, loc) 
            self.rects =[]
            self.items = ["1.Linear", "2.X-R0ADS", "3.Bridge", "4.Centipede"]
            
            for item in self.items:
                option = self.maps_font.render(item, True, (0, 255, 0))
                loc = option.get_rect()
                loc.topleft = (550, 215 + loc.height*1.2*self.items.index(item))
                self.buttonize(loc)
                self.screen.blit(option, loc)
                if loc not in self.rects:
                    self.rects.append(loc)

        elif self.controls == True:
            self.screen.fill(self.background_colour)
            self.draw_back()
            draw_controls(self.screen, self.background_colour, (0,255,0), "Controls")

        elif self.rules == True:
            self.screen.fill(self.background_colour)
            title = self.title_font.render("Rules", True, (0, 255, 0))
            centerx, centery = self.bounds.center
            loc = title.get_rect()
            loc.center = (centerx, centery - 200)
            self.draw_back()
            self.screen.blit(title, loc) 
            self.items = []
        
        pygame.display.flip()

    def draw_back(self):
        back = self.menu_font.render("Back", True, (0, 255, 0))
        self.back = back.get_rect()
        self.back.bottomright = self.bounds.bottomright
        self.screen.blit(back, self.back)

    def buttonize(self,rect):
        x, y = rect.topleft
        if self.main == True or rect == self.back:
            button = pygame.Rect((x-10,y-2),(rect.width + 15,rect.height+1))
            pygame.draw.rect(self.screen, (0,255,0), button, 1)
                                   

    def inputs(self):
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if self.main:
                        if self.rects[0].collidepoint(pygame.mouse.get_pos()):
                            self.main = False
                            self.maps = True
                        elif self.rects[1].collidepoint(pygame.mouse.get_pos()):
                            self.main = False
                            self.controls = True
                        elif self.rects[2].collidepoint(pygame.mouse.get_pos()):
                            self.main = False
                            self.rules = True
                    elif self.maps:
                        if self.back.collidepoint(pygame.mouse.get_pos()):
                            self.maps = False
                            self.main = True
                        for rect in self.rects:
                            if rect.collidepoint(pygame.mouse.get_pos()):
                                self.map = self.rects.index(rect)
                                self.maps = False
                                self.menu_off = True

                    elif self.controls:
                        if self.back.collidepoint(pygame.mouse.get_pos()):
                            self.controls = False
                            self.main = True
                    elif self.rules:
                        if self.back.collidepoint(pygame.mouse.get_pos()):
                            self.rules = False
                            self.main = True

                elif event.type == KEYDOWN and event.key == K_l:
                    self.background_colour = (0,0,0)
                elif event.type == pygame.QUIT:
                    self.menu_off = True
                elif event.type == KEYDOWN and event.key== K_ESCAPE:
                    self.menu_off = True



def draw_controls(screen, back_color, font_color, title):
    cfont = pygame.font.Font(None, 60)
    cbigfont = pygame.font.Font(None, 170)
    csmallfont = pygame.font.Font(None, 30)
    control_list = ["","Add Firewall:", "Subtract Firewall:",
                   "Add X-Virus:", "Subtract X-Virus:",
                   "Add Y-Virus:", "Subtract Y-Virus:",
                   "Add/Detonate Bomb:", "Increase Virus Limit:",
                   "Pause:", "Quit Game:"]
    p1_list = ["","Q", "A", "W", "S", "E", "D", "R", "F", "Spacebar", "Escape"]
    p2_list = ["","Y", "H", "U", "J", "I", "K", "O", "L", "Spacebar", "Escape"]
                   
    backrect = pygame.Rect((0,0),(700,600))
    bounds = screen.get_rect()
    x,y = bounds.center
    backrect.center = x, y

    box1 = pygame.Rect((x, y), (backrect.width/3+30, backrect.height-150))
    box2 = pygame.Rect((x, y), (backrect.width/3+30, backrect.height-150))
    box1.bottomleft = backrect.bottomleft
    box2.bottomright = backrect.bottomright

    pygame.draw.rect(screen, back_color, backrect) 
    pygame.draw.rect(screen, font_color, box1, 2)
    pygame.draw.rect(screen, font_color, box2, 2)

    #Title
    title = cbigfont.render(title, True, font_color)
    loc = title.get_rect()
    loc.center = (x, y - 245)
    screen.blit(title,loc)

    #P1 Title
    title = cfont.render("Player 1", True, font_color)
    loc = title.get_rect()
    x,y = box1.center
    p, q = box1.topleft
    loc.center = x, q - loc.height/2
    screen.blit(title, loc)

    #P2 Title
    title = cfont.render("Player 2", True, font_color)
    loc = title.get_rect()
    x,y = box2.center
    p, q = box2.topleft
    loc.center = x, q - loc.height/2
    screen.blit(title,loc)
    
    #Draw Texts
    for item in control_list:
        text1 = csmallfont.render(item, True, font_color)
        x,y = box1.topleft
        loc = text1.get_rect()
        loc.topleft = (x+5, y + (loc.height+5)*1.5*control_list.index(item))
        screen.blit(text1, loc)
        text2 = csmallfont.render(item, True, font_color)
        x,y = box2.topleft
        loc = text2.get_rect()
        loc.topleft = (x+5, y + (loc.height+5)*1.5*control_list.index(item))
        screen.blit(text2, loc)

    for button in p1_list:
        text = csmallfont.render(button, True, font_color)
        x,y = box1.topright
        loc = text.get_rect()
        loc.topright = (x-5, y + (loc.height+5)*1.5*p1_list.index(button))
        screen.blit(text, loc)
        
    for button in p2_list:
        text = csmallfont.render(button, True, font_color)
        x,y = box2.topright
        loc = text.get_rect()
        loc.topright = (x-5, y + (loc.height+5)*1.5*p2_list.index(button))
        screen.blit(text, loc)
        

    
