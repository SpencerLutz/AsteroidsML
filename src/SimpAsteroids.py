import pygame as pg
import math
import random as rd
from Player import Player
from Debris import Debris
from Bullet import Bullet
import Settings as s

pg.init()
BLACK = (0, 0, 0)
screen = pg.display.set_mode((s.w,s.h))
background = pg.Surface(screen.get_size()).convert_alpha()
pg.draw.rect(background, BLACK, [0, 0, s.w, s.h])
pg.display.set_caption("Asteroids ML")
done = False
clock = pg.time.Clock()

a_img = pg.image.load('Asteroid.png').convert_alpha()

player = Player()
debris = []
bullets = []
level = 0
score = 0
cooldown = 0
levelup = False
ptime = pg.time.get_ticks()

sprites = pg.sprite.LayeredUpdates()
player.add(sprites)

while not done:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True
	keys = pg.key.get_pressed()
	if keys[pg.K_LEFT]:
		player.turnLeft()
	if keys[pg.K_RIGHT]:
		player.turnRight()
	if keys[pg.K_UP]:
		player.thrust()
	if not keys[pg.K_UP] and player.pthrust:
		player.unthrust()
	if keys[pg.K_SPACE] and cooldown <= 0:
		cooldown = 0
		new = Bullet(player.rect.centerx-2, player.rect.centery-2, player.r)
		bullets.append(new)
		new.add(sprites)

	cooldown -= 1

	# if len(debris) == 0:
	# 	level += 1
	# 	for i in range(level+3): debris.append(Debris(80, rd.uniform(0, s.w), rd.uniform(0, s.h), rd.uniform(0,2), rd.uniform(-math.pi, math.pi)))
	# 	for d in debris: d.add(sprites)
	
	player.move()

	for b in bullets:
		b.move()

	for d in debris:
		d.move()
		if pg.sprite.collide_circle(d, player):
			player.reset()
		for b in bullets:
			if pg.sprite.collide_circle(d, b):
				if d.size >= 30:
					debris.append(Debris(int(d.size/2), d.rect.x, d.rect.y, d.v*1.5, d.r+30))
					debris.append(Debris(int(d.size/2), d.rect.x, d.rect.y, d.v*1.5, d.r-30))
					debris[len(debris)-1].add(sprites)
					debris[len(debris)-1].add(sprites)
				d.kill()
				b.kill()
				debris.remove(d)
				bullets.remove(b)

	screen.blit(background, (0,0))
	pg.display.update(sprites.draw(screen))
	clock.tick(60)

	ctime = pg.time.get_ticks()
	etime = ctime-ptime
	ptime = ctime
	if etime > 0 and 1000/etime < 50: print(1000/etime)