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

def goldbach(n):
    primes = []
    res = []
    if n % 2 != 0:
        return None
    for i in range(2 , n + 1):
        if is_it_prime(i) == False:
            primes.append(i)
    for i in primes:
        for j in primes:
            if i + j == n:
                if (j, i) not in res:
                    res.append((i,j))
    print(res)
    return res


