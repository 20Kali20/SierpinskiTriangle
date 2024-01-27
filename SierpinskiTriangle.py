import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000,860))
screen.fill('white')
triangle = [[500, 0], [0, 860], [1000, 860]]
start = [50, 10]
for x in range(2000000):
    pygame.draw.circle(screen, 'black', (start[0], start[1]), 1)
    pygame.display.update()
    corner = random.randint(0, 2)
    start = [(start[0]+triangle[corner][0])/2, (start[1]+triangle[corner][1])/2]
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            exit()
pygame.time.wait(2000)
