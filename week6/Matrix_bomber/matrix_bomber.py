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
            if (i, j) == (0, 0):
                matrix_copy[0][1] = matrix[0][1] - matrix[0][0]
                matrix_copy[1][0] = matrix[1][0] - matrix[0][0]
                matrix_copy[1][1] = matrix[1][1] - matrix[0][0]

            if (i, j) == (last_row, 0):
                matrix_copy[last_row][1] = matrix[last_row][1] - matrix[last_row][0]
                matrix_copy[last_row-1][1] = matrix[last_row-1][1] - matrix[last_row][0]
                matrix_copy[last_row-1][0] = matrix[last_row-1][0] - matrix[last_row][0]

            if (i, j) == (0,last_col):
                matrix_copy[0][last_col-1] = matrix[0][last_col-1] - matrix[0][last_col]
                matrix_copy[1][last_col-1] = matrix[1][last_col-1] - matrix[0][last_col]
                matrix_copy[1][last_col] = matrix[1][last_col] - matrix[0][last_col]

            if (i, j) == (last_row,last_col):
                matrix_copy[last_row][last_col-1] = matrix[last_row][last_col-1] - matrix[last_row][last_col]
                matrix_copy[last_row-1][last_col-1] = matrix[last_row-1][last_col-1] - matrix[last_row][last_col]
                matrix_copy[last_row-1][last_col] = matrix[last_row-1][last_col] - matrix[last_row][last_col]

            if (i, j) == (0, j) and (i,j) != (0,0) and (i,j) != (0,last_col):
                print(i,j)
                matrix_copy[i][j-1] = matrix[i][j-1] - matrix[i][j]
                matrix_copy[i][j+1] = matrix[i][j+1] - matrix[i][j]
                matrix_copy[i+1][j] = matrix[i+1][j] - matrix[i][j]
                matrix_copy[i+1][j-1] = matrix[i+1][j-1] - matrix[i][j]
                matrix_copy[i+1][j+1] = matrix[i+1][j+1] - matrix[i][j]


            matrix_copy[matrix_copy < 0] = 0
            result_dict[i, j] = matrix_copy.sum()

    print(matrix_copy)
    print(result_dict)

    return matrix_copy

test1 =[[1,2,3],[4,5,6],[7,8,9]]
matrix_bombing_plan(test1)
