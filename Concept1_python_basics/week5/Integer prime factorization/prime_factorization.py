def is_it_prime(num):
    # To take input from the user
    #num = int(input("Enter a number: "))

    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    # if flag:
    #     print(num, "is not a prime number")
    #     print(flag)
    # else:
    #     print(num, "is a prime number")
    #     print(flag)
    return flag


def prime_factorization(n):
    simple_primes = []
    temp = n
    prime = []
    prime_power = {}
    tupples = []
    for i in range(2, n + 1):
        if is_it_prime(i) == False:
            simple_primes.append(i)
    for i in simple_primes:
        while temp % i == 0:
            temp = temp // i
            prime.append(i)
    for num in prime:
        if num not in prime_power:
            prime_power[num] = 0
        prime_power[num] = prime_power[num] + 1

    for key, value in prime_power.items():
        tupples.append((key, value))
    print(tupples)

prime_factorization(356)
