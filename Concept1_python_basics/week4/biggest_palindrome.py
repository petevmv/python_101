def get_biggest_palindrome(n):
	result = [x for x in range(10, n + 1) if str(x) == str(x)[::-1]]
	return max(result)
print(get_biggest_palindrome(92009))