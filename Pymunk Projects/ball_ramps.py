import pygame as pg
import pymunk as pym

class Ball(object):
	"""Ball that rolls down ramps"""
	def __init__(self, x, y):
		pass

class Ramp(object):
	"""Ramp that the ball rolls on"""
	def __init__(self, x, y):
		pass

class Control(object):
	"""Controls the game"""
	def __init__(self):
		pass

	def setup_pygame(self):
		pg.init()
		screen = pg.