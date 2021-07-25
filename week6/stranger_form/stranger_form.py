import numpy as np
friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]
MOVMENTS = {
            'A': (-1, 0),
            'B': (1, 0),
            'R': (0, 1),
            'L': (0,-1)
            }
# {
#     'A':(0, 0)
#     'B':(-1, 0)
#     'F':(0, 1)
#     'C':(-2, 0)
#     'D':(-2, 1)
#     'E':(-3, 1)
#     'G':(-3, -1)
# }
def build_friends_layouot(friends_configuration):
    relative_position = {}
    for configuration in friends_configuration:
        relative_position[configuration[0]] = (0, 0)

    for configuration in friends_configuration:
        if len(configuration) == 1:
            continue
        name, position, relative_to = configuration
        relative_x, relative_y = relative_position[relative_to]
        x, y = MOVMENTS[position]
        relative_position[name] = (relative_x + x, relative_y + y)
    return relative_position

build_friends_layouot(friends_configuration)

def outside_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1

    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y


def stranger_forms(cinema_layout, friends_configuration):
    central = friends_configuration[0]
    for config in friends_configuration[1:]:
        name, position, related_to = config


    for i in range(len(cinema_layout)):
        for j in range(len(cinema_layout[0])):
            if cinema_layout[i][j] == '*':
                continue



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

stranger_forms(cinema_layout, friends_configuration)
