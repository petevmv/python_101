import numpy as np
def sum_matrix(m):
    if not isinstance(m, list):
        raise TypeError(f'sum_matrix only takes array/matrix as argument, you have given it {m}')
    arr = np.array(m)
    return arr.sum()
