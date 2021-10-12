import game_of_life
import unittest
import numpy as np
import ipdb

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
		
		spawn_live_cell_on_i_j = game_of_life.update_grid(0, 2, 3, initial_input)[0][2]
		kill_cell_on_i_j = game_of_life.update_grid(3, 0, 1, initial_input)[3][0]
		survival_cell_on_i_j = game_of_life.update_grid(0, 1, 2, initial_input)[0][1]
		
		dead_expected = 0
		live_expected = 1
				
		self.assertEqual(spawn_live_cell_on_i_j, live_expected)
		self.assertEqual(kill_cell_on_i_j, dead_expected)
		self.assertEqual(survival_cell_on_i_j, live_expected)

if __name__ == '__main__':
	unittest.main()