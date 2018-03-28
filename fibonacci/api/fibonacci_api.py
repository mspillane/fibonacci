import logging

from flask import Flask
from flask import jsonify

from fibonacci.core.fibonacci_calculator import get_fibonacci_numbers

ERROR_INVALID_DATA = 422

app = Flask("Fibonacci")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.errorhandler(ERROR_INVALID_DATA)
def invalid_quantity_error(quantity=None):
    """
    Error handler for use in returning a JSON error string for the REST API.
    :param quantity: The quantity parameter passed by the user which is resulting in this error being generated.
    :return: An error message in JSON format which can be returned to a request made to the REST API.
    """
    message = {
        'status': ERROR_INVALID_DATA,
        'message': 'The quantity value specified is not valid: ' + quantity,
    }
    resp = jsonify(message)
    resp.status_code = ERROR_INVALID_DATA
    return resp


@app.route('/fibonacci/<quantity>', methods=['GET'])
def get_fibonacci_sequence(quantity):
    """
    Gets a list of numbers in the Fibonacci series. The quantity parameter specifies the number of Fibonacci numbers requested.

    :param quantity: The number of fibonacci numbers requested
    :return: A list of Fibonacci numbers
    """
    logger.info('Get fibonacci sequence - items requested=%s', quantity)
    # TODO Use a cache here. Return values from the cache rather than re-calculating them.
    try:
        items_requested = int(quantity)
        sequence = get_fibonacci_numbers(items_requested)
    except ValueError:
        return invalid_quantity_error(quantity)

    return jsonify(fibonacci=sequence)


if __name__ == '__main__':
    app.run()
