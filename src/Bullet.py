import pygame as pg
import math
import Settings as s

class Bullet(pg.sprite.Sprite):
	global r, x, y
	def __init__(self, x, y, r, v = 5):
		pg.sprite.DirtySprite.__init__(self)
		self.v = v
		self.r = math.pi/2-r #snaps to 73pi/48, 79pi/48, 90pi/48, 93pi/48 112pi/48
		self.rect = pg.Rect(x,y,4,4)
		self.image = pg.transform.scale(pg.image.load('Bullet.png').convert_alpha(), (4,4))
		self.radius = 2
		print(self.r, r)

	def move(self):
		print(self.r)
		self.rect.x += self.v*math.cos(self.r)
		self.rect.y += self.v*math.sin(self.r)
		if self.rect.centerx < 0: self.rect.centerx = s.w+self.rect.centerx
		if self.rect.centery < 0: self.rect.centery = s.h+self.rect.centery
		if self.rect.centerx > s.w: self.rect.centerx = self.rect.centerx-s.w
		if self.rect.centery > s.h: self.rect.centery = self.rect.centery-s.h

#in future add support for passing bullets; bullets might skip over an asteroid