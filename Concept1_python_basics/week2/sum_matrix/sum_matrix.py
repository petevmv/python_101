import numpy as np
def sum_matrix(m):
    if isinstance(m, str):
        raise TypeError('function does not accept string as param')
    arr = np.array(m)
    return arr.sum()
