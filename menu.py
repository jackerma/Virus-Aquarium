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
            self.items = ["1.Linear", "2.X-Roads", "3.Bridge", "4.Centipede"]
            
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
            self.draw_back()
            self.draw_next()
            draw_rules(self.screen, self.background_colour, (0,255,0), "Rules")

        elif self.rules2 == True:
            self.screen.fill(self.background_colour)
            self.draw_back()
            self.draw_next()
            draw_rules2(self.screen, self.background_colour, (0,255,0), "Rules Part 2")

        elif self.rules3 == True:
            self.screen.fill(self.background_colour)
            self.draw_back()
            self.draw_next()
            draw_rules3(self.screen, self.background_colour, (0,255,0), "Viruses")

        elif self.rules4 == True:
            self.screen.fill(self.background_colour)
            self.draw_back()
            self.draw_home()
            draw_rules4(self.screen, self.background_colour, (0,255,0), "Viruses Part 2")

        
        pygame.display.flip()

    def draw_back(self):
        back = self.menu_font.render("Back", True, (0, 255, 0))
        self.back = back.get_rect()
        self.back.bottomleft = self.bounds.bottomleft
        self.screen.blit(back, self.back)

    def draw_next(self):
        next = self.menu_font.render("Next", True, (0, 255, 0))
        self.next = next.get_rect()
        self.next.bottomright = self.bounds.bottomright
        self.screen.blit(next, self.next)

    def draw_home(self):
        home = self.menu_font.render("Home", True, (0, 255, 0))
        self.home = home.get_rect()
        self.home.bottomright = self.bounds.bottomright
        self.screen.blit(home, self.home)


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
                        elif self.next.collidepoint(pygame.mouse.get_pos()):
                            self.rules = False
                            self.rules2 = True

                    elif self.rules2:
                        if self.back.collidepoint(pygame.mouse.get_pos()):
                            self.rules2 = False
                            self.rules = True
                        elif self.next.collidepoint(pygame.mouse.get_pos()):
                            self.rules2 = False
                            self.rules3 = True

                    elif self.rules3:
                        if self.back.collidepoint(pygame.mouse.get_pos()):
                            self.rules3 = False
                            self.rules2 = True
                        elif self.next.collidepoint(pygame.mouse.get_pos()):
                            self.rules3 = False
                            self.rules4 = True

                    elif self.rules4:
                        if self.back.collidepoint(pygame.mouse.get_pos()):
                            self.rules4 = False
                            self.rules3 = True
                        elif self.home.collidepoint(pygame.mouse.get_pos()):
                            self.rules4 = False
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
                   "Add/Detonate Bomb:", "Hardware Upgrade:",
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
    title = cfont.render("Player 1 (Red)", True, font_color)
    loc = title.get_rect()
    x,y = box1.center
    p, q = box1.topleft
    loc.center = x, q - loc.height/2
    screen.blit(title, loc)

    #P2 Title
    title = cfont.render("Player 2 (Blue)", True, font_color)
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
        
#######################################################################################
    
def draw_rules(screen, back_color, font_color, title):
    cfont = pygame.font.Font(None, 60)
    cbigfont = pygame.font.Font(None, 170)
    csmallfont = pygame.font.Font(None, 30)
    rules_list = ["You are a hacker attempting to control a network by introducing various viruses.These viruses", 
                  "will spread from computer to computer, multiplying over time. But you are not alone: other hackers",
                  "are vying for control of the network. It's a race to see who can control the network and sabotage",
                  "their competitors' home systems.",
                  " ",
                  "Some virus in the network sends back pings (points), representing the vulnerability of the network.",
                  "The more viruses you have, the more pings you accumulate, and the more viruses you can introduce.", 
                  "At your disposal, you have multiple types of viruses -- the more insidious the virus, the more pings ",  
                  "it requires. Once introduced, to the system, your viruses will spread to connected computers and ",
                  "multiply on their own."]
                   
    backrect = pygame.Rect((0,0),(700,600))
    bounds = screen.get_rect()
    x,y = bounds.center
    backrect.center = x, y

    pygame.draw.rect(screen, back_color, backrect) 

    #Title
    title = cbigfont.render(title, True, font_color)
    loc = title.get_rect()
    loc.center = (x, y - 245)
    screen.blit(title,loc)
    
    #Draw Texts
    for item in rules_list:

        text1 = csmallfont.render(item, True, font_color)
        x,y = backrect.topleft
        x = x - 150
        y = y + 150
        loc = text1.get_rect()
        loc.topleft = (x+5, y + (loc.height+5)*1.5*rules_list.index(item))
        screen.blit(text1, loc)


def draw_rules2(screen, back_color, font_color, title):
    cfont = pygame.font.Font(None, 60)
    cbigfont = pygame.font.Font(None, 170)
    csmallfont = pygame.font.Font(None, 30)
    rules_list = ["The unsuspecting network users will be turning their computers on and off, freezing the spread of",
                  "viruses and limiting the number of pings you receive from the network. As in any well-run network,",
                  "the users will also sporadically run anti-virus software in hopes of saving their precious machines,",
                  "wiping out all but the most tenacious of viruses. If they fail to do so and their computer becomes",
                  "inundated with viruses, the computer will crash and the user will have no choice but to wipe their",
                  "hard drive, removing all viruses on the system.",
                  " ",
                  "Your ultimate goal is to sabotage the well-defended home systems of other hackers. The last hacker", 
                  "standing wins."]
                   
    backrect = pygame.Rect((0,0),(700,600))
    bounds = screen.get_rect()
    x,y = bounds.center
    backrect.center = x, y

    pygame.draw.rect(screen, back_color, backrect) 

    #Title
    title = cbigfont.render(title, True, font_color)
    loc = title.get_rect()
    loc.center = (x, y - 245)
    screen.blit(title,loc)
    
    #Draw Texts
    for item in rules_list:

        text1 = csmallfont.render(item, True, font_color)
        x,y = backrect.topleft
        x = x - 150
        y = y + 150
        loc = text1.get_rect()
        loc.topleft = (x+5, y + (loc.height+5)*1.5*rules_list.index(item))
        screen.blit(text1, loc)


def draw_rules3(screen, back_color, font_color, title):
    cfont = pygame.font.Font(None, 60)
    cbigfont = pygame.font.Font(None, 170)
    csmallfont = pygame.font.Font(None, 30)
    rules_list = ["X-Viruses:",
                  "Essential to any hacker, X-Viruses are the ONLY viruses that send back pings. While they do spread very quickly,",
                  "they are easy prey for Y-viruses.",
                  "",
                  "Y-Viruses:",
                  "These clever viruses form the backbone of the hacker's fight force. Taking inspiration from antivirus software,",
                  "they seek out and destroy the opponent's viruses.",
                  "",
                  "Fyrewalls:",
                  "Twisted versions of standard virus defense, these clever buggers trap enemy viruses in the system, ",
                  "preventing them from spreading."]
                   
    backrect = pygame.Rect((0,0),(700,600))
    bounds = screen.get_rect()
    x,y = bounds.center
    backrect.center = x, y

    pygame.draw.rect(screen, back_color, backrect) 

    #Title
    title = cbigfont.render(title, True, font_color)
    loc = title.get_rect()
    loc.center = (x, y - 245)
    screen.blit(title,loc)
    
    #Draw Texts
    for item in rules_list:

        text1 = csmallfont.render(item, True, font_color)
        x,y = backrect.topleft
        x = x - 150
        y = y + 150
        loc = text1.get_rect()
        loc.topleft = (x+5, y + (loc.height+5)*1.5*rules_list.index(item))
        screen.blit(text1, loc)



def draw_rules4(screen, back_color, font_color, title):
    cfont = pygame.font.Font(None, 60)
    cbigfont = pygame.font.Font(None, 170)
    csmallfont = pygame.font.Font(None, 30)
    rules_list = ["",
                  "Ad Bombs:",
                  "The most powerful, but most difficult to construct, Ad Bombs are slow to spread, but devastating once unleashed.",
                  "Not only can they not be killed, but once in place, the hacker can 'detonate' it, flooding the system with pop-ups.",
                  "This removes every single enemy virus (including other Bombs) and temporarily crashes the computer.",
                  "",
                  "Hardware Upgrade:",
                  "Eventually any good hacker will find that they just need more viruses than their server can support. While",
                  "it may be expensive, a hardware upgrade often pays off in the long run, which increases the maximum number",
                  "of viruses the home server can support."]
                   
    backrect = pygame.Rect((0,0),(700,600))
    bounds = screen.get_rect()
    x,y = bounds.center
    backrect.center = x, y

    pygame.draw.rect(screen, back_color, backrect) 

    #Title
    title = cbigfont.render(title, True, font_color)
    loc = title.get_rect()
    loc.center = (x, y - 245)
    screen.blit(title,loc)
    
    #Draw Texts
    for item in rules_list:

        text1 = csmallfont.render(item, True, font_color)
        x,y = backrect.topleft
        x = x - 150
        y = y + 150
        loc = text1.get_rect()
        loc.topleft = (x+5, y + (loc.height+5)*1.5*rules_list.index(item))
        screen.blit(text1, loc)
