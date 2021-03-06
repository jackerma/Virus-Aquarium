#!/usr/bin/env python

import pygame


class CirclesThing():
    def __init__(self,width,height):
        self.width = width
        self.height = height

        self.number_of_circles = 20
        self.radius = 120

        from random import randint
        self.circles = sorted(set((randint(self.radius,width-self.radius),randint(self.radius,height-self.radius)) for i in range(self.number_of_circles)))
        #sort by x to speed up collision detection

        self.f = None


    def display(self):
        self.draw_circles()
        self.draw_circles(circle_radius=5, circle_colour=(255,0,0))
        lines = self.intersect_circles()
        self.draw_lines(lines)

    def draw_circles(self,circle_radius=None,circle_colour=(255,255,255),circles=None):
        if circle_radius is None:
            circle_radius = self.radius
        if circles is None:
            circles = self.circles

        circle_thickness = 2
        for pos in circles:
            pygame.draw.circle(screen, circle_colour, pos, circle_radius, circle_thickness)

    def intersect_circles(self):
        colliding_circles = []
        for i in range(len(self.circles)-1):
            for j in range(i+1,len(self.circles)):
                x1,y1 = self.circles[i]
                x2,y2 = self.circles[j]
                if x2-x1>2*self.radius:
                    break #can't collide anymore.
                if (x2-x1)**2 + (y2-y1)**2 <= (2*self.radius)**2:
                    colliding_circles.append(((x1,y1),(x2,y2)))
        return colliding_circles

    def draw_lines(self,lines,line_colour=(255, 0, 0)):
        for point_pair in lines:
            point1,point2 = point_pair
            pygame.draw.aaline(screen, line_colour, point1, point2, 1)


width, height = 1300, 700
background_colour = (255,255,255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 2')
screen.fill(background_colour)

world = CirclesThing(width,height)

world.display()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
