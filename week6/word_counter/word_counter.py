import numpy as np
def to_string(alist):
    str = ''
    return (str.join(alist))

def word_counter(matrix, word):
    result = 0
    matrix = np.array(matrix)

    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]

    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))

    diagonals = [n.tolist() for n in diags]
    # diagonals left to right and right to left
    for i in diagonals:
        if word in to_string(i):
            result += 1
        if word in to_string(list(reversed(i))):
            result += 1
        # if word in to_string(list(reversed(i))):
        #     print(list(reversed(i)))
    if word == word[::-1]:
        result = result//2

    # result += diagonals.count(list(word))

    # diagonals right to left
    # result += diagonals.count(list(reversed(word)))


    # rows left to right
    result += matrix.tolist().count(list(word))
    print(result)

    # rows right to left
    result += matrix.tolist().count((list(reversed(word))))
    print(result)

    # columns
    # a = matrix[:,2]
    # print(list(reversed(a.tolist()))[0:len(word)])




    # for row in matrix:
    #     if list(word) == row:
    #         print(True)


    # for row_index in range(len(matrix)):
    #     for col_index in range(len(matrix[0])):
    print(result)
    return result

to_string(["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"])
word = "madam"
matrix = [
    ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
    ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
    ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
    ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
    ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
    ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
    ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
]

word_counter(matrix, word)
