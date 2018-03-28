
# from common import notify_error, log_api_call
from fibonacci.core.fibonacci_calculator import get_fibonacci_numbers
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import request
import logging
# from logging.handlers import RotatingFileHandler

# HTTP_STATUS_CODES_MAP = {
#     'INVALID_DATA_ERROR': 422
# }
app = Flask("Fibonacci")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from flask import jsonify

# class InvalidUsage(Exception):
#     status_code = 400
#
#     def __init__(self, message, status_code=None, payload=None):
#         Exception.__init__(self)
#         self.message = message
#         if status_code is not None:
#             self.status_code = status_code
#         self.payload = payload
#
#     def to_dict(self):
#         rv = dict(self.payload or ())
#         rv['message'] = self.message
#         return rv


@app.errorhandler(422)
def invalid_quantity_error(quantity=None, error=None):
    message = {
            'status': 422,
            'message': 'The quantity value specified is not valid: ' + quantity,
    }
    resp = jsonify(message)
    resp.status_code = 422
    return resp


# @app.route('/fibonacci/', methods=['GET'])
@app.route('/fibonacci/<quantity>', methods=['GET'])
def get_fibonacci_sequence(quantity):
    logger.info('Get fibonacci sequence - items requested=%s', quantity)
    # Use ValueError rather than assert function because assert can be disabled and bypassed
    # if not isinstance(quantity, (int)):
    #     raise ValueError('The quantity parameter must be a valid integer. Invalid parameter={}'.format(quantity))

    # TODO Use a cache here. Return values from the cache rather than re-calculating them.
    try:
        # return jsonify(answer=fibonacci_calc(count))
        items_requested = int(quantity)
    except ValueError as ex:
        return invalid_quantity_error(quantity)
        # raise InvalidUsage('This view is gone', status_code=410)
        # return notify_error(ex, HTTP_ERROR_SERVER)


    sequence = get_fibonacci_numbers(items_requested)

    return jsonify(fibonacci=sequence)

    # if 'count' not in request.args or request.args['count'] in ("", None):
    #     return notify_error("ERR_NO_ARG:  'count' argument required to /fibonacci/api", HTTP_ERROR_CLIENT)


if __name__ == '__main__':
    app.run()