import numpy as np
import pytest

from simple_functions import sin


class TestSin(object):
    '''Class to test the sin function is computed correctly'''

    @pytest.mark.parametrize('number, expected', [
        (0, 0),
        (np.pi/2, 1),
        (-0.5, np.sin(-0.5))
    ])
    def test_sin(self, number, expected):
        '''Test computation of sin(x)'''
        answer = sin(number)
        assert np.isclose(answer, expected, atol=1e-6)
