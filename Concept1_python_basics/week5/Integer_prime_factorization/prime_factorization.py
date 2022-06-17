def is_it_prime(num):
    # To take input from the user
    #num = int(input("Enter a number: "))

    # define a flag variable
    flag = True

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to False
                flag = False
                # break out of loop
                break

    # check if flag is True
    # if flag:
    #     print(num, "is a prime number")
    #     print(flag)
    # else:
    #     print(num, "is not a prime number")
    #     print(flag)

    return flag


def prime_factorization(n):
    simple_primes = []        # list to store all prime numbers < n
    temp = n                    
    prime_factor_base = []    
    prime_power = {}   
    result_as_tupples = []
    for i in range(2, n + 1):
        if is_it_prime(i) == True:
            simple_primes.append(i)
    print("Simple primes", simple_primes)
    for i in simple_primes:
        while temp % i == 0:
            temp = temp // i
            prime_factor_base.append(i)
    print('prime factor base', prime_factor_base)
    for num in prime_factor_base:
        if num not in prime_power:
            prime_power[num] = 0
        prime_power[num] = prime_power[num] + 1

    for key, value in prime_power.items():
        result_as_tupples.append((key, value))
    print(result_as_tupples)
    return result_as_tupples

# prime_factorization(356)
# print(is_it_prime(25))
