import pygame as pg
import sys,os
import math


size = width, height = (1920,1080)

pg.init()

screen = pg.display.set_mode(size)

clock = pg.time.Clock()

from sprite import Sprite
from character import Character
from tiles import TileMap
from enemy import Enemy, Enemies
from menu import MainMenu

en = Enemies()


level = TileMap()
level.draw_tiles()

ch = Character()
menu = MainMenu()

center = (ch.rect.centerx,ch.rect.centery)
radius = 100
sc = (center[0]+radius, center[1])
spr = Sprite("ch_arm", 2 , down=True)

dt = 0
aa = 0


while 1:

	for e in pg.event.get():

		if e.type == pg.QUIT:

			pg.quit()
			sys.exit()


	center = (ch.rect.centerx,ch.rect.centery)
	m_x, m_y = pg.mouse.get_pos()

	# angle = math.tan((m_y-ch.rect.y)/(m_x-ch.rect.x))
	# print(angle)
	# x = (300 * math.cos(angle) + ch.rect.centerx)
	# y = (300 * math.sin(angle) + ch.rect.centery)

	v = (m_x - center[0], m_y - center[1])
	distance = (v[0]**2 + v[1]**2 )**0.5

	# dx, dy = mousex - ch.rect.centerx, mousey - ch.rect.centery 
	# xx, yy = (mousex-ch.rect.centerx)-150, (mousey-ch.rect.centery)-150

	if distance > 0:

		scalar = radius / distance
		sc = (
			int(round(center[0] + v[0]*scalar)),
			int(round(center[1] + v[1]*scalar))
		)


	screen.fill(0)
	screen.blit(level.surf,(0,0))

	angle = -(math.degrees(math.atan2(center[1] - sc[1], center[0] - sc[0] )) % 360 + 90)


	ch.dt = dt
	en.dt = dt 

	#c = pg.draw.circle(screen,(255,255,255,0),center,radius)

	ch.update(angle)
	
	ss = ch.blitRotate(screen,spr.sprite,(ch.rect.centerx,ch.rect.centery), (190,-20), angle)


	if ch.dir in ["left","down"]:

		#ch.light(screen,angle)
		ch.draw_aura(screen)
		ch.draw(screen)

	else:

		#ch.light(screen,angle)
		ch.draw_aura(screen)
		ch.draw(screen)


	spr.image = ss[0]
	spr.rect = ss[1]
	spr.mask = pg.mask.from_surface(spr.image, 0)

	screen.blit(spr.image,spr.rect)
	en.update(ch.rect,spr)
	en.draw(screen)
	# pg.draw.polygon(screen, (10,0,0), spr.mask.outline(), 20)
	menu.draw(screen)
	menu.mouse_event((m_x,m_y))

	pg.display.flip()
	dt = clock.tick(60)/1000.0