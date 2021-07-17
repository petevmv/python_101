def matrix_bombing_plan(m):
    import numpy as np
    matrix = np.array(m)
    n, m = np.shape()
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], i, j)
