import json
import unittest

from fibonacci.api.fibonacci_api import app

class TestFibonacciApi(unittest.TestCase):
    """
    Integration tests for the Fibonacci REST Api.
    These are integration tests (and not unit tests). They require that the REST API application is running and
    serving requests
    """
    def setUp(self):
        self.app = app.test_client()

    def test_success(self):
        response = self.app.get('/fibonacci/5')
        assert response.status_code == 200
        fibonacci_dict = json.loads(response.get_data().decode())
        sequence = fibonacci_dict['fibonacci']
        assert sequence == [0, 1, 1, 2, 3]

    def test_bad_quantity_handled(self):
        result = self.app.get('/fibonacci/abc')
        assert result.status_code == 422
        assert result.data == b'{\n  "message": "The quantity value specified is not valid: abc", \n  "status": 422\n}\n'
