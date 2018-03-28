# Fibonacci
This project provides a Fibonacci generator and a REST API for the generator.

This repository includes the following:

* Scripts

## Setup
### How to setup your environment

* Setup a virtual environment using the virtualenv tool to create an environment specific to this project

	    virtualenv fib-env

* Recreate the enviroment using the requirements.txt file

        pip install -r requirements.txt

## How to run the tests

####To run the unit tests

    pytest tests/test_fibonacci.py

####To run the integration tests 

**Note**: The integration tests require the REST API application to be running and serving requests in order for these tests to pass.

    pytest tests/integration/test_fibonacci_functions.py

####To run **ALL** the tests (unit tests + integration tests)

    pytest

## Future
### Further improvements
Use a cache to store values already calculated rather than re-calculating them.