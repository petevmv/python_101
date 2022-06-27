

MOVES = {
		'A': (-1, 0),
		'B': (1, 0),
		'R': (0, 1),
		'L': (0, -1)
		}


# GE
# CD
# B
# AF



friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]

def generate_friends_pos(friends_configuration):
	# create structure of friends that can be applyed to the cinema layout

	relative_position = {}
	relative_position[friends_configuration[0]] = (0, 0)
	
	for configuration in friends_configuration:
		if len(configuration) == 1:
			continue
		
		name, position, relative_to = configuration
		relative_x, relative_y = relative_position[relative_to]

		dx, dy = MOVES[position]

		relative_position[name] = (relative_x + dx, relative_y + dy)
	
	return relative_position




def stranger_form(cinema_layout, friends_configuration):
	result = []
	friends_positions = generate_friends_pos(friends_configuration)

	for x in range(len(cinema_layout)):
		for y in range(len(cinema_layout[0])):
			if cinema_layout[x][y] == '*':
				continue
			

	return result


cinema_layout = ['..*...*.**',
				 '.....**...',
				 '*.*...*..*',
				 '.**....*.*',
				 '...*..*.*.',
				 '.***...*..',
				 '*......*.*',
				 '.....**..*',
				 '..*.*.*..*',
				 '***.*.**..']

