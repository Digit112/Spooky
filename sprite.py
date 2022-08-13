import pygame as pg
import sys
from spritesheet import SpriteSheet


ss = SpriteSheet("spritesheetghost.png")

class Sprite(pg.sprite.Sprite):

	def __init__(self, sprite_name, size=1, up=False, down=False):

		super().__init__()

		self.sprite_loc =  {
			"bg": (720,0,219,219),
			"wall": (975,0,219,219),
			"ch_right":(210,220,110,190),
			"ch_down":(10,220,110,190),
			"ch_left":(10,10,110,190),
			"ch_up":(210,10,110,190),
			"aura":(50,450,1070,1090),
			"ch_arm":(1210,0,720,1210),


			"enemy1_left": (340,10,160,190),
			"enemy1_right": (370,220,160,190),

			"enemy2_left": (520,10,160,190),
			"enemy2_right": (550, 220, 160, 190)
			
		}

		self.type = sprite_name
		self.sprite = ss.image_at(self.sprite_loc[sprite_name])
		
		if up or down:
			self.sprite = self.sprite_scaled(size,up,down)

		self.image = self.sprite
		self.rect = self.sprite.get_rect(center=(0,0))
		self.mask = pg.mask.from_surface(self.image, 0)
		self.w = self.sprite.get_width()
		self.h = self.sprite.get_height()

	def sprite_scaled(self, scale, up, down):

		return ss.scale_image(self.sprite, 2, up, down)

