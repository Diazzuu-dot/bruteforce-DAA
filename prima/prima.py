import math


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i <= math.isqrt(n):
        if n % i == 0:
            return False

        i += 2

    return True


numbers = [2, 17, 29, 91, 97, 100]

for n in numbers:
    if is_prime(n):
        print(n, "adalah bilangan prima")
    else:
        print(n, "bukan bilangan prima")