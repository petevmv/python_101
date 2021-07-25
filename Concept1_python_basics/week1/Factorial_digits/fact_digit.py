def fact_digits(num):
    import math
    fac_list = []
    for i in str(num):
        fac_list.append(math.factorial(int(i)))
    return sum(fac_list)
