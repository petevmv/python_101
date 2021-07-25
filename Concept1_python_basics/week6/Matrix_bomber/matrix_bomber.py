def matrix_bombing_plan(m):
    import numpy as np
    matrix = np.array(m)
    result_dict = {}
    n, m = np.shape(matrix)
    last_row = len(range(n-1))
    last_col = len(range(m-1))
    for i in range(n):
        for j in range(m):
            # print(matrix[i][j], i, j)
            matrix_copy = matrix.copy()

            # Upper left corner
            if (i, j) == (0, 0):
                matrix_copy[i][j+1] = matrix[i][j+1] - matrix[i][j]
                matrix_copy[i+1][j] = matrix[i+1][j] - matrix[i][j]
                matrix_copy[i+1][i+1] = matrix[i+1][i+1] - matrix[i][j]

            # Lower left corner
            elif (i, j) == (last_row, 0):
                matrix_copy[i][j+1] = matrix[i][j+1] - matrix[i][j]
                matrix_copy[i-1][j+1] = matrix[i-1][j+1] - matrix[i][j]
                matrix_copy[i-1][j] = matrix[i-1][j] - matrix[i][j]

            # Upper right corner
            elif (i, j) == (0,last_col):
                matrix_copy[i][j-1] = matrix[i][j-1] - matrix[i][j]
                matrix_copy[i+1][j-1] = matrix[i+1][j-1] - matrix[i][j]
                matrix_copy[i+1][j] = matrix[i+1][j] - matrix[i][j]

            # Lower right corner
            elif (i, j) == (last_row,last_col):
                matrix_copy[i][j-1] = matrix[i][j-1] - matrix[i][j]
                matrix_copy[i-1][j-1] = matrix[i-1][j-1] - matrix[i][j]
                matrix_copy[i-1][j] = matrix[i-1][j] - matrix[i][j]

            # First row
            elif (i, j) == (0, j) and (i, j) != (0,0) and (i, j) != (0, last_col):
                matrix_copy[i][j-1] = matrix[i][j-1] - matrix[i][j]
                matrix_copy[i][j+1] = matrix[i][j+1] - matrix[i][j]
                matrix_copy[i+1][j] = matrix[i+1][j] - matrix[i][j]
                matrix_copy[i+1][j-1] = matrix[i+1][j-1] - matrix[i][j]
                matrix_copy[i+1][j+1] = matrix[i+1][j+1] - matrix[i][j]

            # Last row
            elif (i, j) == (last_row, j) and (i, j) != (last_row,0) and (i, j) != (last_row, last_col):
                    matrix_copy[i][j-1] = matrix[i][j-1] - matrix[i][j]
                    matrix_copy[i][j+1] = matrix[i][j+1] - matrix[i][j]
                    matrix_copy[i-1][j] = matrix[i-1][j] - matrix[i][j]
                    matrix_copy[i-1][j+1] = matrix[i-1][j+1] - matrix[i][j]
                    matrix_copy[i-1][j-1] = matrix[i-1][j-1] - matrix[i][j]

            # First col
            elif (i, j) == (i, 0) and (i, j) != (0, 0) and (i, j) != (last_row, 0):
                matrix_copy[i][j+1] = matrix[i][j+1] - matrix[i][j]
                matrix_copy[i-1][j+1] = matrix[i-1][j+1] - matrix[i][j]
                matrix_copy[i-1][j] = matrix[i-1][j] - matrix[i][j]
                matrix_copy[i+1][j] = matrix[i+1][j] - matrix[i][j]
                matrix_copy[i+1][j+1] = matrix[i+1][j+1] - matrix[i][j]

            # Last col
            elif (i, j) == (i, last_col) and (i, j) != (0, last_col) and (i, j) != (last_row,last_col):
                matrix_copy[i][j-1] = matrix[i][j-1] - matrix[i][j]
                matrix_copy[i-1][j-1] = matrix[i-1][j-1] - matrix[i][j]
                matrix_copy[i-1][j] = matrix[i-1][j] - matrix[i][j]
                matrix_copy[i+1][j-1] = matrix[i+1][j-1] - matrix[i][j]
                matrix_copy[i+1][j] = matrix[i+1][j] - matrix[i][j]

            # Everything in between
            else:
                print(i,j)
                matrix_copy[i][j-1] = matrix[i][j-1] - matrix[i][j]
                matrix_copy[i][j+1] = matrix[i][j+1] - matrix[i][j]
                matrix_copy[i+1][j] = matrix[i+1][j] - matrix[i][j]
                matrix_copy[i+1][j+1] = matrix[i+1][j+1] - matrix[i][j]
                matrix_copy[i+1][j-1] = matrix[i+1][j-1] - matrix[i][j]
                matrix_copy[i-1][j+1] = matrix[i-1][j+1] - matrix[i][j]
                matrix_copy[i-1][j-1] = matrix[i-1][j-1] - matrix[i][j]
                matrix_copy[i-1][j] = matrix[i-1][j] - matrix[i][j]

            matrix_copy[matrix_copy < 0] = 0
            result_dict[i, j] = matrix_copy.sum()

    print(matrix_copy)
    print(result_dict)

    return matrix_copy

test1 =[[1,2,3],[4,5,6],[7,8,9]]
matrix_bombing_plan(test1)
