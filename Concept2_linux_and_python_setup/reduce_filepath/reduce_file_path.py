from collections import deque

def reduce_file_path(path):
    result = deque()
    for ch in path.split('/'):
        if ch == '..' and len(result) > 0:
            result.pop()
        if ch not in ('.','..',''):
            result.append(ch)


    print('/' + '/'.join(result))
    return '/' + '/'.join(result)





