import random

# Generates a tilemap of the given size that represents a maze.
def gen_maze_map(w, h, sx, sy):
	tiles = []
	for i in range(w):
		tiles.append([])
		for j in range(h):
			tiles[i].append(0)
	
	path = [(sx, sy)]
	
	# Move in a random direction and mark the new cell as visited.
	# If you can't move in any direction, backtrack according to the path already taken (shown above)
	while True:
		tiles[sx][sy] = -1
		
		dirs = [(2, 0), (0, 2), (-2, 0), (0, -2)]
		random.shuffle(dirs)
		
		# Try to move in each direction
		went_forward = False
		for d in dirs:
			nx = sx + d[0]
			ny = sy + d[1]
			if nx >= 0 and nx < w and ny >= 0 and ny < h and tiles[nx][ny] == 0:
				tiles[sx+d[0]//2][sy+d[1]//2] = -1
				tiles[nx][ny] = -1
				
				sx = nx
				sy = ny
				
				path.append((sx, sy))
				
				went_forward = True
				
				break
		
		# If no direction worked, backtrack.
		if not went_forward:
			if len(path) > 1:
				sx = path[-2][0]
				sy = path[-2][1]
				
				del path[-1]
			
			else:
				break
				
	return tiles