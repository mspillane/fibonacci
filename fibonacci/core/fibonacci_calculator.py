import logging

from functools import lru_cache
from itertools import islice

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fib(a=0, b=1):
    """
    Generator for Fibonacci numbers.
    :param a: Initial seed value for generator function
    :param b: Second seed value for generator function
    :return: The next generated value is returned each time the generator is called
    """
    yield a
    while True:
        yield b
        a, b = b, a + b

@lru_cache(maxsize=4)
def get_fibonacci_numbers(quantity):
    """
    Get a list of fibonacci numbers. The size of the list is governed by the quantity parameter passed to this function.

    :param quantity:
    :return: A list composed of fibonacci numbers. The size of the list is governed by the quantity parameter
             passed in.
    """
    logger.info('Get fibonacci numbers %s', quantity)
    # Use ValueError rather than assert function because it can be disabled and bypassed
    if not isinstance(quantity, (int)):
        raise ValueError('The quantity parameter must be a valid integer. Invalid parameter={}'.format(quantity))

    if quantity < 0:
        raise ValueError('The quantity parameter must be >= 0. Invalid parameter={}'.format(quantity))

    return list(islice(fib(), quantity))


if __name__ == '__main__':
    logger.info('Running fibonacci calculator')

    fib_numbers = get_fibonacci_numbers(10)
    print(fib_numbers)
    print(get_fibonacci_numbers.cache_info())

    fib_numbers = get_fibonacci_numbers(10)
    print(fib_numbers)
    print(get_fibonacci_numbers.cache_info())

    fib_numbers = get_fibonacci_numbers(5)
    print(fib_numbers)
    print(get_fibonacci_numbers.cache_info())