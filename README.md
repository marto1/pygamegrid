# About:

A little bit of code to make working in pygame more organized.  It is
by no means a fully-fledged grid layout with big widget system
underneath. The goal to interfere as little as possible with a
preexisting workflow and provide a barebone grid layout.

# Usage:

```python
import pygame
from pygame.locals import *
from pygrid.layout import create_layout,

def draw_rect(s, pos, size): #the callback that the layout will use for a given spot
    pygame.draw.rect(s, [200,200,200], pygame.Rect(pos,size), 2)

if __name__ == '__main__':
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    STDFONT = "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-L.ttf" #a font path on your system
    font = pygame.font.Font(STDFONT,20)

    xtot = 10 #x columns
    ytot = 10 #y rows
    layout = create_layout(surface, xtot, ytot) #initialize grid layout with a surface and columns x rows 

    for x in xrange(xtot):
        for y in xrange(ytot):
            layout.put(draw_rect, x, y, 1, 1) #"putting" things on the surface, these loops will draw a grid.

    # layout.put(draw_rect, 5, 2, 2, 8) #we can also specify spans. Here we have span for columns of 2 and span for rows of 8.

    #starting the whole thing up.
    clock = pygame.time.Clock()
    while(True):
        clock.tick(60)
        pygame.display.flip()

```
