def nan_expand(times):
    if times == 0:
        return ""
    if times == 1:
        return "Not a NaN"
    neg = 'Not a'
    return "{} ".format(neg)*times + "NaN"
