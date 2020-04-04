import pygame as pg
import Settings as s
import math
class Player(pg.sprite.Sprite):
	global rect, r, xv, yv, v, track, images, pthrust

	def __init__(self, x = (s.w-30)/2, y = (s.h-45)/2, r = math.pi, xv = 0, yv = 0, v = .5):
		pg.sprite.DirtySprite.__init__(self)
		self.r = r
		self.v = v
		self.xv = xv
		self.yv = yv
		self.rect = pg.Rect(x, y, 30, 45)
		self.radius = 1
		self.images = [pg.image.load('Player.png').convert_alpha(), pg.image.load('PThrust.png').convert_alpha()]
		self.imagec = self.images[0]
		self.image = self.imagec
		self.pthrust = False
		self.rx, self.ry = 0, 0

	def thrust(self):
		self.xv += self.v*math.sin(self.r)
		self.yv += self.v*math.cos(self.r)
		self.imagec = self.images[1]
		self.pthrust = True

	def unthrust(self):
		self.imagec = self.images[0]
		self.pthrust = False

	def turnLeft(self):
		self.r += math.pi/48

	def turnRight(self):
		self.r -= math.pi/48

	def move(self):
		self.xv *= .96
		self.yv *= .96
		if abs(self.xv) < 1:
			if abs(self.rx + self.xv) > 1:
				self.rect.left += self.xv + self.rx
				self.rx = 0
			else:
				self.rx += self.xv
		else:
			self.rect.left += self.xv
		if abs(self.yv) < 1:
			if abs(self.ry + self.yv) > 1:
				self.rect.top += self.yv + self.ry
				self.ry = 0
			else:
				self.ry += self.yv
		else:
			self.rect.top += self.yv
		if self.rect.centerx < 0: self.rect.centerx = s.w+self.rect.centerx
		if self.rect.centery < 0: self.rect.centery = s.h+self.rect.centery
		if self.rect.centerx > s.w: self.rect.centerx = self.rect.centerx-s.w
		if self.rect.centery > s.h: self.rect.centery = self.rect.centery-s.h
		self.image = pg.transform.rotate(self.imagec, math.degrees(self.r)-180)
		self.rect = self.image.get_rect(center=self.rect.center)

	def reset(self):
		self.rect.x = (s.w-30)/2
		self.rect.y = (s.h-45)/2
		self.r = math.pi
		self.xv = 0
		self.yv = 0
