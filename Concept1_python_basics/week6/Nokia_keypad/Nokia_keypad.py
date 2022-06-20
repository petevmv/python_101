from Group import group

KEYPAD = { 0:' ',
    2:'abc',3:'def',
    4:'ghi',5:'jkl',
    6:'mno',7:'pqrs',
    8:'tuv',9:'wxyz'}

def numbers_to_message(pressed_sequence):
    letters = []
    upper = False
    KEYPAD = {0:" ",2:'abc',
              3:'def', 4:'ghi',
              5:'jkl',
              6:"mno", 7:"pqrs",
              8:"tuv", 9:"wxyz"}

    grouped_sequence = group(pressed_sequence)
    for grouped in grouped_sequence:
        key = grouped[0]
        time_pressed = len(grouped)
        #print(key, time_pressed)
        
        if key == -1:
            continue
        
        if key == 1:
            upper = True
            continue
        
        if key == 0:
            letters.append(' ' * time_pressed)
            continue

        sequence = KEYPAD[key]
        letter = sequence[(time_pressed - 1) % len(sequence)]
        
        if upper:
            letter  = letter.upper()
            upper = False
        letters.append(letter)
    # print(''.join(letters))
    return ''.join(letters)


def message_to_numbers(message):
    result = []
    nums = []
    
    for char in message:
        if char.isupper():
            nums.append([1])
        for k, v in KEYPAD.items():
            for letter in v:
                if letter == char.lower():
                    times_pressed = v.index(letter) + 1
                    nums.append([k]*times_pressed)

    for idx, val in enumerate(nums[:-1]):
        if val[0] == nums[idx-1][0]:
            val.append(-1)

    for i in nums:
         result.extend(i)

    # print(result)
    return result
