def palindromes_count(n):

    res = [True for x in range(10, n+1) if str(x) == str(x)[::-1]].count(True)
    return res
