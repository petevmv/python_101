from Group import group
def numbers_to_message(pressed_sequence):
    letters = []
    upper = False
    keypad = {0:" ",2:'abc',
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

        sequence = keypad[key]
        letter = sequence[(time_pressed - 1) % len(sequence)]
        if upper:
            letter  = letter.upper()
            upper = False
        letters.append(letter)
    print(''.join(letters))
    return ''.join(letters)


print(numbers_to_message([0, 0, 0, 0]) == '    ')
numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
numbers_to_message([2])
numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2])
numbers_to_message([2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2])



def message_to_numbers(message):
    pass


# message_to_numbers("abc")
#[2, -1, 2, 2, -1, 2, 2, 2]
# message_to_numbers("a")
# [2]
# message_to_numbers("Ivo e Panda")
# [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
# message_to_numbers("aabbcc")
# [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
