import logging
from itertools import islice


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# TODO Check the type and value of the number passed in.

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


def get_fibonacci_numbers(quantity):
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