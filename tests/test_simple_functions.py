import pytest

from simple_functions import my_sum, factorial, \
                             do_something_with_pandas


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize('x, expected', [
        ([1, 2, 3],
         [[1, 2, 3, 1, 2, 3],
          [1, 2, 3, 1, 2, 3, 1, 2, 3],
          2, 3]),
        ('abc', ['abcabc', 'abcabcabc', 'aa', 'aaa'])
    ])
    def test_do_something_with_pandas(self, x, expected):
        '''Test our do_something_with_pandas function'''
        df = do_something_with_pandas(x)
        answer = [df[str(x)].double,
                  df[str(x)].triple,
                  df[str(x[0])].double,
                  df[str(x[0])].triple]
        assert answer == expected
