import numpy as np
# from PIL import Image as im
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import ipdb

def update_grid(idx_i, idx_j, number_of_live_neighbors, matrix):
	matrix_copy = matrix.copy()
	# print(number_of_live_neighbors)

	if number_of_live_neighbors in [2, 3] and matrix[idx_i][idx_j] == 1:
		matrix_copy[idx_i][idx_j] = 1
	elif number_of_live_neighbors == 3 and matrix[idx_i][idx_j] == 0:
		matrix_copy[idx_i][idx_j] = 1
	else:
		matrix_copy[idx_i][idx_j] = 0
	return matrix_copy

def run(matrix):
	size = matrix.shape
	matrix_copy = matrix.copy()
	number_of_live_neighbors = 0
	last_row = size[0] - 1
	last_col = size[1] - 1
	for idx_i, x in enumerate(matrix):
		for idx_j, y in enumerate(x):
			# upper left corner
			if (idx_i, idx_j) == (0, 0):
				if matrix[idx_i + 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				
				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix)
				
				# reset_counter
				number_of_live_neighbors = 0
				continue
			
			

			# lower left corner
			if (idx_i, idx_j) == (last_row, 0):
				if matrix[idx_i - 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i -1][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i][idx_j + 1] == 1:
					number_of_live_neighbors += 1

				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix_copy.copy())
				number_of_live_neighbors = 0
				continue
			
			# upper right corner
			if (idx_i, idx_j) == (0, last_col):
				if matrix[idx_i][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j -1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i +1][idx_j] == 1:
					number_of_live_neighbors += 1

				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix_copy.copy())
				number_of_live_neighbors = 0
				continue

			# lower righ corner
			if (idx_i, idx_j) == (last_row, last_col):
				if matrix[idx_i][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j] == 1:
					number_of_live_neighbors += 1

				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix_copy.copy())
				number_of_live_neighbors = 0
				continue
			
			# first row
			if (idx_i, idx_j) == (0, idx_j) and idx_j != 0 and idx_j != last_col:
				if matrix[idx_i][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i][idx_j - 1] == 1:
					number_of_live_neighbors +=1
				if matrix[idx_i + 1][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix_copy.copy())
				number_of_live_neighbors = 0
				continue
			
			# last row 
			if (idx_i, idx_j) == (last_row, idx_j) and idx_j != 0 and idx_j != last_col:
				if matrix[idx_i - 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix_copy.copy())
				number_of_live_neighbors = 0
				continue
			
			# first col 
			if (idx_i, idx_j) == (idx_i, 0) and idx_i != 0 and idx_i != last_row:
				if matrix[idx_i + 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix_copy.copy())
				number_of_live_neighbors = 0
				continue

			# last col
			if (idx_i, idx_j) == (idx_i, last_col) and idx_i != 0 and idx_i != last_row:
				if matrix[idx_i - 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix_copy.copy())
				number_of_live_neighbors = 0
				continue

			# everything in between
			else:
				if matrix[idx_i][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j + 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i + 1][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j - 1] == 1:
					number_of_live_neighbors += 1
				if matrix[idx_i - 1][idx_j + 1] == 1:
					number_of_live_neighbors += 1

				matrix_copy = update_grid(idx_i, idx_j, number_of_live_neighbors, matrix_copy.copy())
				number_of_live_neighbors = 0
				continue
	# print(matrix_copy)
	return matrix_copy




  
	
	# print(number_of_live_neighbors)
			


# SEEDS
beacon = [
	[1, 1, 0, 0],
	[1, 1, 0, 0],
	[0, 0, 1, 1],
	[0, 0, 1, 1]]

R_pentomino = [
		[0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0],
		[0, 1, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0]]

acron = [
	[1,1,0,1,1,1],
	[0,0,0,1,0,0],
	[0,1,0,0,0,0]]

glider =[
	[0,0,1],
	[1,0,1],
	[0,1,1]]
		  


# PLANTING SEED
universe = np.zeros((50, 50))

# universe[15:20, 21:26] = R_pentomino
# universe[0:3, 0:3] = glider
# universe[1:6, 1:7] = glider
universe[30: 33, 30:36] = acron


fig = plt.figure()
plt.axis('off')
images = []

number_of_generations = 30
if __name__ == "__main__":
	for i in range(number_of_generations):
		# ipdb.set_trace()
		images.append((plt.imshow(universe, cmap='binary'),))
		universe = run(universe)
		# plt.show()


	im_animation = animation.ArtistAnimation(fig, images, interval=100, repeat_delay=1000, blit=True)
	plt.show()
	im_animation.save('ani.gif', writer='imagemagic')
