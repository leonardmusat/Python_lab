def is_prime(a):
    count = 0
    for index in range(1, a//2+1):
        if a % index == 0:
            count += 1
    if count > 1:
        return False
    else:
        return True


def which_is_prime(lst):
    primes = []
    for i in lst:
        if is_prime(i):
            primes.append(i)
    return primes


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(which_is_prime(lst))
