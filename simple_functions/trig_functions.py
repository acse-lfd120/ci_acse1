from simple_functions import factorial

from functools import lru_cache

__all__ = ['sin']


def sin(x):
    max_n = 1000
    min_diff = 1e-6
    sin_x = 0
    stop = False
    n = 0
    while not stop:
        new_term = (-1)**n * x**(2*n + 1) / factorial(2*n + 1)
        sin_x += new_term
        if n == max_n or abs(new_term) < min_diff:
            stop = True
        n += 1
    return sin_x
