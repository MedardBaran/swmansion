import math


def short_function(a, b):
    from sympy import isprime
    from collections import Counter
    return [i for i in a if not isprime(Counter(b)[i])]


def _my_is_prime(n) -> bool:
    if n <= 3:
        return n > 1

    if n % 2 == 0:
        return False

    last_to_check = int(math.sqrt(n))
    for i in range(3, last_to_check, 2):
        if n % i == 0:
            return False
    return True


def my_function(a, b):
    excluded = set()
    primes = set()

    result = []

    for n in a:
        if n in excluded:
            continue
        elif n in result:
            result.append(n)
        else:
            i = b.count(n)
            if i in primes:
                excluded.add(n)
            if _my_is_prime(i):
                primes.add(i)
                excluded.add(n)
            else:
                result.append(n)

    return result


if __name__ == '__main__':
    a = [2, 3, 9, 2, 5, 1, 3, 7, 10]
    b = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
    expected_c = [2, 9, 2, 5, 7, 10]

    assert short_function(a, b) == expected_c
    assert my_function(a, b) == expected_c
