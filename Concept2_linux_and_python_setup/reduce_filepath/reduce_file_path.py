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





print(reduce_file_path("/") == "/")
print(reduce_file_path("/srv/../") == "/")
print(reduce_file_path("/srv/www/htdocs/wtf/") == "/srv/www/htdocs/wtf")
print(reduce_file_path("/srv/www/htdocs/wtf") == "/srv/www/htdocs/wtf")
print(reduce_file_path("/srv/./././././") == "/srv")
print(reduce_file_path("/etc//wtf/") == "/etc/wtf")
print(reduce_file_path("/etc/../etc/../etc/../") == "/")
print(reduce_file_path("//////////////") == "/")
print(reduce_file_path("/../") == "/")
print(reduce_file_path('/home//user/courses/./Programming101-Python/week01/../') == '/home/user/courses/Programming101-Python')
