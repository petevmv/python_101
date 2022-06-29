import re
# from collections import deque

def reduce_file_path(path):
    patterns = [
            (
                '.\w*.[.]{2,}',  # pattern matches dots (someword/../) and the word the its left
                ''
            ),
            (
                '[.]{1,}', # pattern matches single dot /././. 
                ''
            ),
            (
                '[\/]{2,}', # pattern matches all remaining back slashes //, its used last  
                '/'         # as the pattern above sometimes leaves more slashes when used
            )

    ]

    for pattern, substitution in patterns:
        path = re.sub(pattern, substitution, path)

    while path[-1] in ('/') and len(path) > 1:
        path = path[0:-1]

    return ''.join(path)


    # result = deque()
    # for ch in path.split('/'):
    #     if ch == '..' and len(result) > 0:
    #         result.pop()
    #     if ch not in ('.','..',''):
    #         result.append(ch)


    # print('/' + '/'.join(result))
    # return '/' + '/'.join(result)





