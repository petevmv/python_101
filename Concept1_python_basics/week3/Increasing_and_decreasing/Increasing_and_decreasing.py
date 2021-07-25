from enum import Enum
import pandas as pd

class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3

def increasing_or_decreasing(nl):
    if nl == [] or len(nl) <= 1:
        print('NONE')
        return Monotonicity.NONE

    series_obj = pd.Series(nl)

    if series_obj.is_monotonic_increasing and series_obj.is_unique == True:
        print("incresing")
        return Monotonicity.INCREASING
    elif series_obj.is_monotonic_decreasing and series_obj.is_unique == True:
        print('decreseing')
        return Monotonicity.DECREASING
    else:
        print('NONE')
        return Monotonicity.NONE
