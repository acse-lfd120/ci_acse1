from functools import lru_cache
import pandas as pd

__all__ = ['my_sum', 'factorial', 'do_something_with_pandas']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)
def factorial(n):
    return n * factorial(n-1) if n else 1


def do_something_with_pandas(x):
    return pd.DataFrame({str(x): [x*2, x*3],
                         str(x[0]): [x[0]*2, x[0]*3]},
                        index=['double', 'triple'])
