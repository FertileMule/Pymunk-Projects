"""The purpose of this example is to demonstrate a ball
rolling down a series of ramps.  The goal is to create
an example that not only demonstrates how to use pymunk,
but does so in an OOP style."""

import os, sys
import pygame as pg
import pymunk as pk

SCREEN_SIZE = (600, 800)
WHITE = (255, 255, 255)
ORANGE = (255, 128, 0)
START_X = 100
START_Y = 700
GRAVITY = (0.0, -400)


class Ball(object):
    """Ball that rolls down ramps"""
    def __init__(self, x, y):
        self.mass = 1
        self.radius = 14
        self.inertia = pk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pk.Body(self.mass, self.inertia)
        self.body.position = x, y
        self.shape = pk.Circle(self.body, self.radius)

    def update(self):
        """Update ball information by converting pymunk coordinates
        into pygame coordinates"""
        self.x = int(self.body.position.x)
        self.y = int(self.body.position.y * -1 + SCREEN_SIZE[1])

    def draw(self, surface):
        """Draws ball to a surface"""
        circle_center = (self.x, self.y)
        radius = int(self.radius)
        pg.draw.circle(surface, ORANGE, circle_center, radius)


class Ramp(object):
    """Ramp that the ball rolls on"""
    def __init__(self, x, y):
        self.body = pk.Body()
        self.body.position = (x, y)
        self.shape = pk.Segment(self.body, (x, y), (x+100, y), 5)
        self.x = int(self.body.position.x)
        self.y = int(self.body.position.y)

    def draw(self, surface):
        """Draws ramp to a surface"""
        point_a = (int(self.shape.a[0]), 
                  int(self.shape.a[1] * -1 + SCREEN_SIZE[1]))
        point_b = (int(self.shape.b[1]),
                  int(self.shape.b[1] * -1 + SCREEN_SIZE[1]))

        pg.draw.line(surface, ORANGE, point_a, point_b, 5)


class Control(object):
    """Controls the game"""
    def __init__(self):
        self.screen = self.setup_pygame()
        self.screen_rect = self.screen.get_rect()
        self.space = pk.Space()
        self.space.gravity = GRAVITY
        self.done = False
        self.fps = 60
        self.current_time = 0.0
        self.clock = pg.time.Clock()
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
        self.ramp = Ramp(50, 200)
        self.space.add(self.ramp.shape)

    def add_ball_to_space(self):
        """Add the ball to the level and space for physics"""
        self.ball = Ball(START_X, START_Y)
        self.space.add(self.ball.body, self.ball.shape)

    def update(self):
        """Updates game"""
        while not self.done:
            self.get_user_input()
            self.current_time = pg.time.get_ticks()
            self.screen.fill((255, 255, 255))
            self.update_space()
            self.check_if_ball_off_screen()
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
        self.space.step(1/50.0)
        self.ball.update()
        self.ball.draw(self.screen)
        self.ramp.draw(self.screen)

    def check_if_ball_off_screen(self):
        """Checks if ball is no longer on screen.  If so,
        the ball is deleted, and a new one is created"""
        if self.ball.x > SCREEN_SIZE[0] or self.ball.x < 0:
            self.reset_ball_position()
        elif self.ball.y > SCREEN_SIZE[1] or self.ball.y < 0:
            self.reset_ball_position()

    def reset_ball_position(self):
        """Deletes ball and resets it to original position"""
        self.space.remove(self.ball.shape, self.ball.body)
        self.ball = Ball(START_X, START_Y)
        self.space.add(self.ball.body, self.ball.shape)



if __name__ == '__main__':
    game = Control()
    game.update()
    pg.quit()
    sys.exit()












