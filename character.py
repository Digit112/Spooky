import pygame as pg
from sprite import Sprite



fup, fdown, fleft, fright = (
	Sprite("ch_up", 2, down=True),
	Sprite("ch_down", 2, down=True),
	Sprite("ch_left", 2, down=True),
	Sprite("ch_right", 2, down=True)
)

aura = Sprite("aura", 2, down=True)


class Character(pg.sprite.Sprite):

	def __init__(self):

		super().__init__()
		self.sprite = fright

		self.dir = "right"
		self.image = self.sprite.sprite
		self.rect = self.sprite.rect

		self.rect.x = 400
		self.rect.y = 400


		self.dt = 0

	def light(self,scr,angle):

		s = pg.Surface((1000,1000), pg.SRCALPHA)
		s.set_alpha(128)
		p = pg.draw.polygon(s, (208,215,140,0), [(160,75),(145,75),(0,630),(250,630)])

		self.blitRotate(scr,s,(self.rect.centerx+20,self.rect.centery-6), (150,30), angle)

	def update(self,a):

		self.move()
		self.face(a*-1)
		self.aura_rect = aura.sprite.get_rect(center=(self.rect.x+22, self.rect.y+50))


	def face(self, a):

		if a <= 350 and a >= 250:
			self.sprite = fright
			self.dir = "right"

		if a >= 349 and a <= 430:
			self.sprite = fdown
			self.dir = "down"

		if a >= 103 and a < 150:
			self.sprite = fleft
			self.dir = "left"

		if a >= 180 and a <= 240:
			self.sprite = fup
			self.dir = "up"


		self.image = self.sprite.sprite


	def move(self):

		k = pg.key.get_pressed()


		up,down,left,right = (
			k[pg.K_UP] or k[pg.K_w],
			k[pg.K_DOWN] or k[pg.K_s],
			k[pg.K_LEFT] or k[pg.K_a],
			k[pg.K_RIGHT] or k[pg.K_d]
		)

		if up :
			self.rect.y -= 400 * self.dt
		if down :
			self.rect.y += 400 * self.dt
		if left:
			self.rect.x -= 400 * self.dt
		if right:
			self.rect.x += 400 * self.dt



	def blitRotate(self, surf, image, origin, pivot, angle):


		image_rect = image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
		offset_center_to_pivot = pg.math.Vector2(origin) - image_rect.center

		rotated_offset = offset_center_to_pivot.rotate(-angle)
		rotated_image_center = (origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)
		rotated_image = pg.transform.rotate(image, angle)
		rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)


		return (rotated_image, rotated_image_rect)

	def draw(self,screen):

		screen.blit(self.image,self.rect)

	def draw_aura(self,screen):

		screen.blit(aura.sprite,self.aura_rect)
