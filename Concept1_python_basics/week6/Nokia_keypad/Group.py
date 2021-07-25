#C01P08 - Group
from itertools import groupby
def group(items):
    res = [list(y) for x, y in groupby(items)]
    return res
