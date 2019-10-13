import pygame

pygame.init()

w, h = 650, 350
size = w, h

screen = pygame.display.set_mode(size)


def draw():
    line_1_color = pygame.Color('white')
    line_1_w = 0
    line_1_points = ((25, 25), (600, 100))
    pygame.draw.rect(screen, line_1_color, line_1_points, line_1_w)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
