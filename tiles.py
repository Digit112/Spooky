
import pygame as pg
from sprite import Sprite


class Tile():
	##- Expects: Sprite(image), x pos, y pos
	def __init__(self, image, x, y, layer=0):


		##- Type is always the name of the sprite
		self.type = image.type
		##- The actual sprite surface
		self.image = image.sprite
		##- Width, height of sprite
		self.w, self.h = self.image.get_width(), self.image.get_height()
		##- Sprite rect/ position in window
		self.rect = self.image.get_rect(topleft=(x,y))
		
		# Layer of this tile
		self.layer = layer
		
##- Actual tile map which has evolved into a class for more than just the tile map

class TileMap:

	def __init__(self, h_map):

		self.home_map = h_map

		##- Tiles is all Tile() objects pushed into this array from the make_tile function
		##- Matrix mirrors this with pg.Rect for the paint
		self.tiles = []
		##- Camera = True when character.x = 600. This is what drives the map forward
		self.camera = False
		##- Delta time
		self.dt = 0
		##- Surface to be drawn later, in level()
		self.surf = pg.Surface((1920,1080), pg.SRCALPHA, 32)
		##- list of obstacles to draw in level(), and the rate of which they can be drawn
		##- Array full of coordinates to be used for paint later
		self.make_tile()

	##- Creates sprite object for each corresponding integer in array map
	def make_tile(self):
		##- x, y : determines the position and location of each tile in map
		x = 0
		y = 0
		
		##- For each corresponding integer in array map, create the corresponding sprite, and pass the x,y position
		for i in range(len(self.home_map)):
			for j in range(len(self.home_map[i])):
				if self.home_map[i][j] == -2:
					self.tiles.append(Tile(Sprite("bg"), x, y))
				if self.home_map[i][j] == 0:
					self.tiles.append(Tile(Sprite("wall"), x, y))
				
				##- Increment x, y by width and height, then reset x to zero once j loop completes
				x += self.tiles[-1].w
			y += self.tiles[-1].h
			x = 0
		self.draw_tiles()
	def draw_tiles(self):
		for i in self.tiles:
			self.surf.blit(i.image, i.rect)

