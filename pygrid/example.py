import pygame
from pygame.locals import *
from layout import *

def draw_rect(s, pos, size):
    pygame.draw.rect(s, [200,200,200], pygame.Rect(pos,size), 2)

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
    # layout.put(draw_rect, 0, 1)
    # layout.put(draw_rect, 3, 6)
    # layout.put(draw_rect, 5, 2, 2, 8)

    clock = pygame.time.Clock()
    while(True):
        clock.tick(60)
        pygame.display.flip()
