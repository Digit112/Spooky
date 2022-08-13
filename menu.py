import pygame as pg

class MainMenu:

	def __init__(self):

		self.title = pg.font.Font("karma_suture.ttf", 90)
		self.options = [["PLAY", pg.font.Font("karma_suture.ttf", 60)],["QUIT", pg.font.Font("karma_suture.ttf", 60)]]
		self.text_reference = []
		self.image = pg.Surface((800,800) , pg.SRCALPHA, 32)
		self.x = 100
		self.y = 100 

		self.rect = self.image.get_rect(topleft=(0,0))

		self.started = False
		
		self.update()

	def update(self):


		self.text_reference.append([self.title.render("Placeholder", True, (255,255,255)), (self.x,self.y)])

		for i in self.options:
			self.y += 200
			self.text_reference.append([i[1].render(i[0], True, (255,255,255)), (self.x, self.y)])
		for i in self.text_reference:
			self.image.blit(i[0], i[1])

	def mouse_event(self, pos):
		for i in self.text_reference[1:]:

			if i[0].get_rect(topleft=i[1]).collidepoint(pos):
				print("asd")
		
	def draw(self,screen):

		screen.blit(self.image, (self.rect))