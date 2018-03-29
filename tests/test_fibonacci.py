import pytest
import unittest
from fibonacci.core.fibonacci_calculator import get_fibonacci_numbers

class TestFibonacciGenerator(unittest.TestCase):
    """
    Tests the Fibonacci generator
    """
    def test_get_fibonacci_sequence(self):
        fib_numbers = get_fibonacci_numbers(10)
        assert isinstance(fib_numbers, list)
        assert fib_numbers == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


    def test_get_fibonacci_corner_cases(self):
        fib_numbers = get_fibonacci_numbers(0)
        assert isinstance(fib_numbers, list)
        assert fib_numbers == []


    def test_get_fibonacci_sequence_fails_for_non_integer_argument(self):
        expected_msg = 'The quantity parameter must be a valid integer. Invalid parameter=abc'
        with pytest.raises(ValueError) as ex:
            get_fibonacci_numbers('abc')
        assert str(ex.value) == expected_msg


    # TODO Setup some parameterized tests
    def test_get_fibonacci_sequence_handles_negative_integer_argument(self):
        expected_msg = 'The quantity parameter must be >= 0. Invalid parameter=-1'
        with pytest.raises(ValueError) as ex:
            get_fibonacci_numbers(-1)
        assert str(ex.value) == expected_msg

    def test_cache(self):
        fib_numbers = get_fibonacci_numbers(10)
        assert isinstance(fib_numbers, list)
        assert fib_numbers == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        cache_info = get_fibonacci_numbers.cache_info()
        assert cache_info.hits == 0
        assert cache_info.misses == 1

        get_fibonacci_numbers(10)
        cache_info = get_fibonacci_numbers.cache_info()
        assert cache_info.hits == 1
        assert cache_info.misses == 1

        get_fibonacci_numbers(5)
        cache_info = get_fibonacci_numbers.cache_info()
        assert cache_info.hits == 1
        assert cache_info.misses == 2
