"""The purpose of this example is to demonstrate a ball
rolling down a series of ramps.  The goal is to create
an example that not only demonstrates how to use pymunk,
but does so in an OOP style."""

import os, sys
import pygame as pg
import pymunk as pk

SCREEN_SIZE = (600, 800)


class Ball(object):
    """Ball that rolls down ramps"""
    def __init__(self, x, y):
        self.body = body
        self.shape = shape

class Ramp(object):
    """Ramp that the ball rolls on"""
    def __init__(self, x, y):
        pass

class Control(object):
    """Controls the game"""
    def __init__(self):
        self.screen = self.setup_pygame()
        self.screen_rect = self.screen.get_rect()
        self.space = pk.Space()
        self.space.gravity = (0.0, -900)
        self.done = False
        self.fps = 60
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()

        self.add_ramps_to_space()
        self.add_ball_to_space()

    def setup_pygame(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_caption('Balls and Ramps')
        screen = pg.display.set_mode(SCREEN_SIZE)

        return screen

    def add_ramps_to_space(self):
        """Add the ramps to build the level and space for physics"""
        pass

    def add_ball_to_space(self):
        """Add the ball to the level and space for physics"""
        pass

    def update(self):
        """Updates game"""
        while not self.done:
            self.get_user_input()
            self.current_time = pg.time.get_ticks()
            self.update_space()
            pg.display.update()
            self.clock.tick(self.fps)

    def get_user_input(self):
        """Get user events and keys pressed"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()

    def update_space(self):
        """Updates the physics simulation"""
        pass


if __name__ == '__main__':
    game = Control()
    game.update()
    pg.quit()
    sys.exit()












