import pygame
import os
import math

DEG = math.pi / 180
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
os.chdir("..")
os.chdir("..")
os.chdir("..")
screen = pygame.display.set_mode((400, 400))
car = pygame.image.load('car.png')

screen.fill(black)
screen.blit(car, (400, 275))
pygame.display.flip()

x = 0
offset = 30 * math.sin(x * DEG)
sprite = pygame.transform.rotate(car, x)
screen.fill(black)
pygame.draw.line(screen, white, (100, 0), (100, 400))
pygame.draw.line(screen, white, (0, 100), (400, 100))
screen.blit(sprite, (100, 100))
pygame.display.flip()
