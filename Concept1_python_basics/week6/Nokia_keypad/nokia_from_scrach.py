from Group import group

keypad = { 0:' ',
	2:'abc',3:'def',
	4:'ghi',5:'jkl',
	6:'mno',7:'pqrs',
	8:'tuv',9:'wxyz'}

def numbers_to_msg(sequence):
	letters = []
	upper = False

	grouped_sequence = group(sequence)

	for grouped in grouped_sequence:
		key = grouped[0]
		times_presed = len(grouped)
		
		if key == -1:
			continue
		
		if key == 1:
			upper = True
			continue
		
		if key == 0:
			letters.append(' ' * times_presed)
			continue
		
		sequence = keypad[key]
		letter = sequence[times_presed % len(sequence)- 1]

		if upper:
			upper = False
			letters.append(letter.upper())
			continue		
		
		letters.append(letter)

	return ''.join(letters)


def msg_to_numbers(msg):
	nums = []
	result = [] 

	for char in msg:
		if char.isupper():
			nums.append([1])
		for k,v in keypad.items():
			for letter in v:
				if letter == char.lower():
					time_presed = v.index(letter)+1
					nums.append([k]*time_presed)
					

	for idx, val in enumerate(nums[:-1]):
		if val[0] == nums[idx - 1][0]:
			val.append(-1)	
	for i in nums:
		result.extend(i)
	return result


tests_for_numbers_to_msg = [
		(
			[0,0,0,0],
			'    '
		),
		(	
			[2, -1, 2, 2, -1, 2, 2, 2],
			'abc'
		),
		(
			[2, 2, 2, 2, 2, 2, 2],
			'a'
		),
		(
			[2, 3, 4, 5, 6, 7, 8, 9],
			'adgjmptw'
		),
		(
			[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2],
			'Ivo e Panda'
		)
]	

print('===Tests for numbers_to_msg()===')
for pressed, expected in tests_for_numbers_to_msg:
	print(expected == numbers_to_msg(pressed), numbers_to_msg(pressed))

test_for_msg_to_numberes = [	
		(
			'abc',
			[2,-1,2,2,-1,2,2,2]
		),
		(
			'aabbcc',
			[2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
		),
		(
			'Ivo e Panda',
			[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
		),
		(
			'a',
			[2]
		)
]

print('===Tests for msg_to_numbers()===')
for pressed, expected in test_for_msg_to_numberes:
	print(expected == msg_to_numbers(pressed), msg_to_numbers(pressed))