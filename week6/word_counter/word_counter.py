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

    # rows left to right and right to left
    for i in matrix.tolist():
        if word in to_string(i):
            result += 1
        if word in to_string(list(reversed(i))):
            result += 1

    # columns top to bottom and bottom to top
    for i in range((len(matrix[0,:]))):
        if word in to_string(matrix[::,i].tolist()):
            result += 1
        if word in to_string(list(reversed(matrix[::,i].tolist()))):
            result += 1
    # anagram check
    if word == word[::-1]:
        result = result//2


    print(result)
    return result
word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]
#
# word = "actually"
# matrix = [
#     ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],
#     ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],
#     ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],
#     ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],
#     ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],
#     ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],
#     ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],
#     ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]
# ]
#
# word = "madam"
# matrix = [
#     ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
#     ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
#     ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
#     ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
#     ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
#     ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
#     ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
#     ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
# ]
#
# word = "python"
# matrix = [
#   ["r", "u", "b", "y"],
#   ["r", "u", "b", "y"],
#   ["r", "u", "b", "y"],
#   ["r", "u", "b", "y"],
# ]
word_counter(matrix, word)
