import game_of_life
import unittest
import numpy as np


class Test_game_of_life(unittest.TestCase):
	def test_run(self):
		initial_input = np.array([[0, 1, 0],
					 [0, 1, 1],
					 [1, 0, 1],
					 [1, 0, 1]])
		  	
		expected = np.array([[0, 1, 1],
					[1, 0, 1],
					[1, 0, 1],
					[0, 0, 0]])

		self.assertEqual(game_of_life.run(initial_input).tolist(), expected.tolist())

	def test_universe_and_plant_seed(self):
		board = np.zeros((6, 6))

		seed = game_of_life.glider
		board[1:4, 1:4] = seed
		
		expected = np.array([[0, 0, 0, 0, 0 ,0],
							 [0, 0, 0, 1, 0, 0],
							 [0, 1, 0, 1, 0, 0],
							 [0, 0, 1, 1, 0, 0],
							 [0, 0, 0, 0, 0, 0],
							 [0, 0, 0, 0, 0, 0]])
		
		expected_after_one_gen = np.array([[0, 0, 0, 0, 0, 0],
									   	   [0, 0, 1, 0, 0, 0],
										   [0, 0, 0, 1, 1, 0],
										   [0, 0, 1, 1, 0, 0],
										   [0, 0, 0, 0, 0, 0],
										   [0, 0, 0, 0, 0, 0]])

		
		self.assertEqual(board.tolist(), expected.tolist())
		self.assertEqual(game_of_life.run(expected).tolist(),
							 expected_after_one_gen.tolist())
	
	def test_update_grid(self):
		initial_input = np.array([[0, 1, 0],
					 [0, 1, 1],
					 [1, 0, 1],
					 [1, 0, 1]])
		
		updated_grid = game_of_life.update_grid(1, 2, 3, initial_input)

		expected = game_of_life.run(initial_input)[1][2]
		
		self.assertEqual(updated_grid[1][1], expected)





if __name__ == '__main__':
	unittest.main()