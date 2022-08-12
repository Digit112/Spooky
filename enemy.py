import pygame as pg
from sprite import Sprite
import random

enemy1 = enemy1_left, enemy1_right,  = (
	Sprite("enemy1_left", 2, down=True),
	Sprite("enemy1_right", 2, down=True)
)

enemy2 = enemy2_left, enemy2_right = (
	Sprite("enemy2_left", 2, down=True),
	Sprite("enemy2_right", 2, down=True)
)

class Enemy(pg.sprite.Sprite):

	def __init__(self):

		pg.sprite.Sprite.__init__(self)
		self.sprite = random.choice([enemy1,enemy2])
		xy= [(random.randrange(-100,0), random.randrange(0,1080)), (random.randrange(1920,2020), random.randrange(0,1080))]

		self.image = self.sprite[0].sprite
		self.rect = self.image.get_rect(center=(random.choice(xy)))
		self.mask = pg.mask.from_surface(self.image)

		self.dt = 0
		self.move_speed = random.randrange(2,5) * self.dt * 60
		self.momentum = 0 

		self.collided = False

		self.death_anim = [-2,2]
		self.current_anim = 0
		self.death_timer = 0
		self.dead = False


	def update(self, ch_rect, light):

		self.direction = pg.math.Vector2(ch_rect.x - self.rect.x , ch_rect.y - self.rect.y)

		self.move_towards_player()
		self.collided_with_light()


	def collided_with_light(self):


		if self.collided:

			self.kill_ghost()

		else:

			self.reset_enemy()




	def kill_ghost(self):

		self.current_anim = (self.current_anim+1) % len(self.death_anim)

		self.death_timer += 1

		self.death_anim[0] -= 0.2
		self.death_anim[1] += 0.2


		self.rect.x += self.death_anim[self.current_anim]
		self.rect.y -= 0.01

		if self.death_timer == 70:

			self.dead = True


	def reset_enemy(self):

		self.death_timer = 0
		self.current_anim = 0 
		self.death_anim = [-2,2]

	def move_towards_player(self):

		if sum(self.direction) != 0:

			self.direction.normalize()
			self.direction.scale_to_length(self.move_speed)

			self.rect.move_ip(self.direction) 

		if self.move_speed <= 10:

			self.move_speed += 0.02


class Enemies:

	def __init__(self):

		self.enemy_list = pg.sprite.Group()
		self.max_enemy = 1
		self.current_enemies = len(self.enemy_list)


	def update(self,ch_rect,light):


		if len(self.enemy_list) < self.max_enemy:

			self.enemy_list.add(Enemy())
			self.current_enemies = len(self.enemy_list)
		
		self.check_collision(ch_rect, light)

		for i in self.enemy_list:
			i.dt = self.dt
			i.update(ch_rect,light)

	def check_collision(self,ch_rect,light):

		for spr in self.enemy_list:

			col = pg.sprite.collide_mask(spr,light)
			if col:
				spr.move_speed -= 0.04 if spr.move_speed > 0 else 0
				spr.collided = True
			else:
				spr.collided = False

			if spr.dead:

				self.enemy_list.remove(spr)

				self.max_enemy += 1




	def draw(self, screen):

		for i in self.enemy_list:
			
			screen.blit(i.image, i.rect)

