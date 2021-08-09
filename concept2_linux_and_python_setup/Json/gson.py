import sys
import json



f = open(sys.argv[1])
the_json = json.load(f)
splited_arg = sys.argv[2].split('.')

json_check = splited_arg[0].split('[')[0]
if json_check not in the_json.keys():
	print('Error: Propertiy not found')
	sys.exit(1)


if len(splited_arg) == 1:
	number_arg = [int(word) for word in splited_arg[0] if word.isdigit()]
	

if len(splited_arg) > 1:
	number_for_second_arg = [int(word) for word in splited_arg[1] if word.isdigit()]
	number_arg = [int(word) for word in splited_arg[0] if word.isdigit()]


if len(splited_arg) > 1 and number_arg and not number_for_second_arg:	
	first_argument = splited_arg[0].split('[')[0]
	second_argument = splited_arg[1]
	number_arg = number_arg[0]
	print(the_json[first_argument][number_arg][second_argument])

elif len(splited_arg) > 1 and number_for_second_arg:
	first_argument = splited_arg[0].split('[')[0]
	second_argument = splited_arg[1].split('[')[0]
	number_arg = number_arg[0]
	number_for_second_arg = number_for_second_arg[0]
	print(the_json[first_argument][number_arg][second_argument][number_for_second_arg])

elif len(splited_arg) > 1 and not number_arg:
	first_argument = splited_arg[0]
	second_argument = splited_arg[1]
	print(the_json[first_argument][second_argument])

elif len(splited_arg) == 1 and not number_arg:
	first_argument = splited_arg[0]
	print(the_json[first_argument])

elif len(splited_arg) == 1 and len(number_arg) == 1:
	first_argument = splited_arg[0].split('[')[0]
	number_arg = number_arg[0]
	print(the_json[first_argument][number_arg])

elif len(splited_arg) == 1 and len(number_arg) > 1:
	first_argument = splited_arg[0].split('[')[0]
	first_index = number_arg[0]
	second_index = number_arg[1]
	print(the_json[first_argument][first_index][second_index])










