def histogram(strin):
    if isinstance(strin, str):
        my_dict = {}
        for ch in strin:
            if ch not in my_dict:
                my_dict[ch] = 0
            my_dict[ch] = my_dict[ch] + 1
        return my_dict
    raise Exception('Strings only')