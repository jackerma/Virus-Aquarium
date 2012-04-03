#!/usr/bin/env python

import pygame
import networkx

class CirclesThing():
    def __init__(self,width,height):
        self.width = width
        self.height = height

        self.number_of_circles = 80
        self.radius = 60

        from random import randint
        self.circles = sorted(set((randint(self.radius,width-self.radius),randint(self.radius,height-self.radius)) for i in range(self.number_of_circles)))
        #sort by x to speed up collision detection

        self.sink = (self.width/2, self.height-10)
        self.source = (self.width/2, 10)
        self.f = None

        self.find_cut()


    def find_cut(self):
        G = networkx.Graph()
        for node1,node2 in self.get_connections_to_source_sink()+self.intersect_circles():
            G.add_edge(node1,node2,capacity=1)
            #print self.G.adj
        G2 = networkx.DiGraph()
        for node in G:
            if node not in (self.source,self.sink):
                G2.add_edge((node,1),(node,2),capacity=1)

        for edge in G.edges_iter():
            if self.source in edge:
                continue
            if self.sink in edge:
                continue
            node1,node2 = edge
            G2.add_edge((node1,2),(node2,1),capacity=1)
            G2.add_edge((node2,2),(node1,1),capactiy=1)

#        for node in G[self.source]:
#            G2.add_edge(self.source,(node,1))
#        for node in G[self.sink]:
#            G2.add_edge((node,2),self.sink)

#        print networkx.min_cut(G2,self.source,self.sink)

        #flowValue, flowGraph = networkx.ford_fulkerson(G2,(self.source,'b'),(self.sink,'a'))
        ##print flowValue
        #print flowGraph
        #self.f = flowGraph

    def display(self):
        self.draw_circles()
        self.draw_circles(circle_radius=5, circle_colour=(255,0,0))
        lines = self.intersect_circles()
        self.draw_lines(lines)
        self.draw_source_sink()

    def draw_circles(self,circle_radius=None,circle_colour=(0,0,255),circles=None):
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

    def draw_source_sink(self):


        self.draw_circles(circles=(self.sink,self.source),circle_radius=15,circle_colour=(0,255,0))

        bottom_line = ((0,self.height-self.radius),(self.width,self.height-self.radius))
        top_line = ((0,self.radius),(self.width,self.radius))

        self.draw_lines([top_line, bottom_line],line_colour=(60,60,60))

        self.draw_lines(self.get_connections_to_source_sink(),line_colour=(0,255,0))

    def get_connections_to_source_sink(self):
        connections = []
        for x,y in self.circles:
            if y<2*self.radius:
                connections.append((self.source,(x,y)))
            elif y>height-2*self.radius:
                connections.append((self.sink,(x,y)))
        return connections



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
