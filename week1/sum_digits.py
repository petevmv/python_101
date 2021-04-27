def sum_digits(nums):
    nums = abs(nums)
    num_list = []
    for num in str(nums):
        num_list.append(int(num))
    return sum(num_list)
