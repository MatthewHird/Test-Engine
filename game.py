import pygame
import os
import math
from vehicle import Vehicle
from boundary import Boundary


class Game:
    fps = 60
    black = (0, 0, 0)
    white = (255, 255, 255)

    def __init__(self, app_name, display, display_size):
        self.return_value = None
        self.display = display
        self.clock = pygame.time.Clock()
        self.display_size = display_size
        self.app_name = app_name
        self.vehicle = Vehicle(self.display)
        self.boundary = Boundary(self.display, self.display_size)

    def run(self):
        self.return_value = None

        while not self.return_value:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
            pygame.display.set_caption("fps: " + str(self.clock.get_fps()))

        return self.return_value

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.return_value = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.vehicle.left = -1
                elif event.key == pygame.K_d:
                    self.vehicle.right = 1
                elif event.key == pygame.K_w:
                    self.vehicle.gas = 1
                elif event.key == pygame.K_s:
                    self.vehicle.brake = 1
                elif event.key == pygame.K_RSHIFT:
                    self.vehicle.turn_mod = 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.vehicle.left = 0
                elif event.key == pygame.K_d:
                    self.vehicle.right = 0
                elif event.key == pygame.K_w:
                    self.vehicle.gas = 0
                elif event.key == pygame.K_s:
                    self.vehicle.brake = 0
                elif event.key == pygame.K_RSHIFT:
                    self.vehicle.turn_mod = 1

    def update(self):
        self.vehicle.update()

    def draw(self):
        self.display.fill(self.black)
        self.vehicle.draw()
        pygame.display.update()
