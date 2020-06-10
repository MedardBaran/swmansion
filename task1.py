def short_function(a, b):
    from sympy import isprime
    from collections import Counter
    return [i for i in a if not isprime(Counter(b)[i])]


if __name__ == '__main__':
    a = [2, 3, 9, 2, 5, 1, 3, 7, 10]
    b = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
    expected_c = [2, 9, 2, 5, 7, 10]

    assert short_function(a, b) == expected_c
