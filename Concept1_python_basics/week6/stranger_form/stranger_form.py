from copy import deepcopy

MOVMENTS = {
    'A':(-1, 0),
    'B':(1, 0),
    'L':(0, -1),
    'R':(0, 1)
}
def outside_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1

    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y



def add_point(p, q):
    px, qx = p
    py, qy = q
    return (px + py, qx + qy)


def print_layout(configuration, layout):
    layout = deepcopy([list(row) for row in layout])
    for name, point in configuration.items():
        x, y = point
        layout[x][y] = name
    for row in layout:
        print(''.join(row))


def build_layout(configuration, layout):
    layout = deepcopy([list(row) for row in layout])
    for name, point in configuration.items():
        x, y = point
        layout[x][y] = name

    new_layout = []
    for row in layout:
        new_layout.append(''.join(row))

    return new_layout


def in_cinema(point, cinema_layout):
    x, y = point

    return (# short-circuit (when python enterpreter sees "and"
    # and evaluates the first condition as False it does not evaluate any further)
        not outside_of_bounds(point, cinema_layout)
        and cinema_layout[x][y] == '.'
    )


def build_friends_relative_position(friends_configuration):
    relative_position = {}

    for configuration in friends_configuration:
        relative_position[configuration[0]] = (0,0)

    for configuration in friends_configuration:
        if len(configuration) == 1:
            continue

        name, position, relative_to = configuration

        x, y = MOVMENTS[position]

        relative_x, relative_y = relative_position[relative_to]

        relative_position[name] = (relative_x + x, relative_y + y)

    return relative_position


def stranger_form(cinema_layout, friends_configuration):
    result = []
    friends_relative_position = build_friends_relative_position(friends_configuration)
    for x in range(len(cinema_layout)):
        for y in range(len(cinema_layout[0])):
            if cinema_layout[x][y] == '*':
                continue

            friends_current_possition = {
                name:add_point((x,y), point)
                for name, point in friends_relative_position.items()
            }
            all_points_in = True

            for point in friends_current_possition.values():
                if not in_cinema(point, cinema_layout):
                    all_points_in = False
                    break


            if all_points_in:
                print_layout(friends_current_possition, cinema_layout)
                result.append(
                    build_layout(
                        friends_current_possition,
                        cinema_layout
                        )
                )
    return result

cinema_layout = [
    '..*...*.**',
    '.....**...',
    '*.*...*..*',
    '.**....*.*',
    '...*..*.*.',
    '.***...*..',
    '*......*.*',
    '.....**..*',
    '..*.*.*..*',
    '***.*.**..'
]

friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]
stranger_form(cinema_layout, friends_configuration)
