import pygame
import os
import math
from display import Display
from game import Game


class App:

    app_name = 'Archduke'
    icon = 'icon.png'
    display_size = (1000, 800)

    def __init__(self):
        pass

    def execute(self):
        display_init = Display(self.app_name, self.icon, self.display_size[0], self.display_size[1])
        display_init.run()
        display = display_init.display

        app_quit = False

        while not app_quit:

            game = Game(self.app_name, display, self.display_size)
            game.run()
            app_quit = True


if __name__ == '__main__':
    app = App()
    app.execute()
