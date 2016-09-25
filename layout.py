# -*- coding: utf-8 -*-
"""
A non-intrusive grid layout for pygame.
"""
import pygame
from pygame.locals import *

class Layout(object):

    def __init__(self, surface, cols, rows):
        self.surface = surface
        self.cols = cols
        self.rows = rows
        self.xstep = surface.get_width() / cols
        self.ystep = surface.get_height() / rows

    def put(self, draw, xtile, ytile, xspan=1, yspan=1, args=()):
        xstep, ystep = self.xstep, self.ystep
        return draw(
            self.surface,
            (xstep*xtile, ytile*ystep),
            (xstep*xspan, ystep*yspan))

def create_layout(surface, cols, rows):
    return Layout(surface, cols, rows)

def draw_rect(s, pos, size):
    pygame.draw.rect(s, [200,200,200], pygame.Rect(pos,size), 2)

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
STDFONT = "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-L.ttf"
font = pygame.font.Font(STDFONT,20)

xtot = 10
ytot = 10
layout = create_layout(surface, xtot, ytot)

for x in xrange(xtot):
    for y in xrange(ytot):
        layout.put(draw_rect, x, y, 1, 1)


clock = pygame.time.Clock()
while(True):
    clock.tick(60)
    pygame.display.flip()


