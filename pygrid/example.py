import pygame
from pygame.locals import *
from layout import *

if __name__ == '__main__':
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
