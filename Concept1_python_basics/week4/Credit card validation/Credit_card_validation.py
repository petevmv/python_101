def sum_of_digits(x):
    if x * 2 >= 10:
        y = str(x * 2)
        return (int(y[0]) + int(y[1]))
    else:
        return x * 2
def is_credit_card_valid(number):
    num_list = []
    for idx, num in enumerate(reversed(str(number))):
        if idx % 2 != 0:
            num_list.append(sum_of_digits(int(num)))
        else:
            num_list.append(int(num))
    result = sum(num_list)
    if result % 10 == 0:
        print("valid")
        return True
    else:
        print("not valid")
        return False


print(is_credit_card_valid(79927398715))
