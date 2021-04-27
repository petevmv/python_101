def is_number_balanced(number):
    number = str(number)
    Leftsum = 0
    Rightsum = 0
    for i in range(0, int(len(number) / 2)):
        Leftsum = Leftsum + int(number[i])
        Rightsum = (Rightsum + int(number[len(number) - 1 - i]))
    if (Leftsum == Rightsum):
        print("Balanced", end = '\n')
        return True
    else:
        print("Not Balanced", end = '\n')
        return False

is_number_balanced(1238033) is True
