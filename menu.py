import pygame as pg

class MainMenu:

	def __init__(self):

		self.title = pg.font.Font("karma_suture.ttf", 90)
		self.options = [["PLAY", pg.font.Font("karma_suture.ttf", 60)],["QUIT", pg.font.Font("karma_suture.ttf", 60)]]
		self.image = pg.Surface((800,800) , pg.SRCALPHA, 32)
		self.x = 100
		self.y = 100 

		self.rect = self.image.get_rect(topleft=(0,0))

		self.update()
	def update(self):


		self.image.blit(self.title.render("Placeholder", True, (255,255,255)), (self.x,self.y))

		for i in self.options:
			self.y += 200
			self.image.blit(i[1].render(i[0], True, (255,255,255)), (self.x, self.y))


	def draw(self,screen):

		screen.blit(self.image, (self.rect))