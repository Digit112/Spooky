import pygame as pg


class Text:

	def __init__(self):

		self.font = pg.font.Font("karma_suture.ttf", 20)
		self.image = self.font.render("")

		self.rect = self.image.get_rect(center=(0,0))

	def render_text(self, text, pos):


		self.image = self.font.render("text")
		self.rect = self.image.get_rect(center=pos)
		

	def set_font_size(self, size):

		self.font = pg.font.Font("karma_suture", size)

	def draw(self, screen):

		screen.blit(self.image, self.rect)

