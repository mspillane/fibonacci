import json
import pytest
import unittest
from unittest import mock
from fibonacci.core.fibonacci_calculator import get_fibonacci_numbers
from fibonacci.api.fibonacci_api import app

class TestFibonacciGenerator(unittest.TestCase):
    """
    Tests the Fibonacci generator and REST API
    """

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_get_fibonacci_sequence(self):
        fib_numbers = get_fibonacci_numbers(10)
        assert isinstance(fib_numbers, list)
        assert fib_numbers == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_get_fibonacci_sequence_fails_for_non_integer_argument(self):
        expected_msg = 'The quantity parameter must be a valid integer. Invalid parameter=abc'
        with pytest.raises(ValueError) as ex:
            get_fibonacci_numbers('abc')
        assert str(ex.value) == expected_msg


    # Setup some parameterized tests
    def test_get_fibonacci_sequence_handles_negative_integer_argument(self):
        expected_msg = 'The quantity parameter must be >= 0. Invalid parameter=-1'
        with pytest.raises(ValueError) as ex:
            get_fibonacci_numbers(-1)
        assert str(ex.value) == expected_msg

'''
class TestFibonacciApi(unittest.TestCase):
    """
    """
    def setUp(self):
        self.app = app.test_client()


    def test_fibonacci_success(self):
        response = self.app.get('/fibonacci/5')
        assert response.status_code == 200
        fibonacci_dict = json.loads(response.get_data().decode())
        sequence = fibonacci_dict['fibonacci']
        assert sequence == [0, 1, 1, 2, 3]


    # def test_thing(self):
    #     response = self.app.get('/')
    #     assert response == expected




    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
'''
