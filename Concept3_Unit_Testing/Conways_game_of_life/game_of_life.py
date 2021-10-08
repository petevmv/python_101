import numpy as np

def update_grid(idx_i, idx_j, number_of_live_neighbors, matrix):
	matrix_copy = matrix.copy()
	print(number_of_live_neighbors)

	if number_of_live_neighbors in [2, 3] and matrix[idx_i][idx_j] == 1:
		matrix_copy[idx_i][idx_j] = 1
	elif number_of_live_neighbors == 3 and matrix[idx_i][idx_j] == 0:
		matrix_copy[idx_i][idx_j] = 1
	else:
		matrix_copy[idx_i][idx_j] = 0
	return matrix_copy

def get_neighbor(matrix):
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
					


	print(matrix_copy)
	# print(number_of_live_neighbors)
			
	


test = np.array([[0, 1, 0],[0,1,1],[1,0,1],[1,0,1]])
a = np.random.randint(2, size=(3,3))
# print(a)
# print("______________________")
# print(test[0])
get_neighbor(test)