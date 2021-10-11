import pygame
from pygame.draw import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()

FPS = 30

sc = pygame.display.set_mode((640, 480))
sc.fill((255, 255, 255))

circle(sc, YELLOW, (320, 240), 100)
circle(sc, BLACK, (320, 240), 100, 1)

circle(sc, RED, (270, 210), 20)
circle(sc, BLACK, (270, 210), 20, 1)
circle(sc, BLACK, (270, 210), 10)

circle(sc, RED, (370, 210), 16)
circle(sc, BLACK, (370, 210), 16, 1)
circle(sc, BLACK, (370, 210), 6)

rect(sc, BLACK, (280, 280, 80, 15))

line(sc, BLACK, [220, 170], [300, 190], 10)

line(sc, BLACK, [420, 170], [340, 190], 10)

# polygon(sc, BLACK, [[300, 250], [320, 280],
#                      [190, 190], [130, 130]])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()