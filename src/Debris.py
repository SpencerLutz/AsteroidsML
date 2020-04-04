import pygame as pg
import random as rd
import math
import Settings as s

class Debris(pg.sprite.Sprite):
	global size, rect, v, r, track
	def __init__(self, size = 80, x = rd.uniform(0, s.w), y = rd.uniform(0, s.h), v = rd.uniform(0,2), r = rd.uniform(-math.pi,math.pi)):
		pg.sprite.DirtySprite.__init__(self)
		self.size = size
		self.v = v
		self.r = r
		self.rect = pg.Rect(x,y,self.size,self.size)
		self.image = pg.transform.scale(pg.image.load('Asteroid.png').convert_alpha(), (size,size))

	def move(self):
		self.rect.x += self.v*math.cos(self.r)
		self.rect.y += self.v*math.sin(self.r)
		if self.rect.centerx < 0: self.rect.centerx = s.w+self.rect.centerx
		if self.rect.centery < 0: self.rect.centery = s.h+self.rect.centery
		if self.rect.centerx > s.w: self.rect.centerx = self.rect.centerx-s.w
		if self.rect.centery > s.h: self.rect.centery = self.rect.centery-s.h
		
