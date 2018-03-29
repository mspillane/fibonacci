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

## How to run the REST API application

The REST API is run by running the following file:

    fibonacci/api/fibonacci_api.py

This will make the REST API available at the following endpoint:
    
    http://127.0.0.1:5000/ 
    
The Fibonacci function provided on the REST API can be called using the following endpoint. The parameter specifies the number of items in the Fibonacci series to return

    http://127.0.0.1:5000/fibonacci/5    
    

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
* Use a cache to store values already calculated rather than re-calculating them. (NOW IMPLEMENTED)
* Use pytest parametrization in unit test to give more test coverage and test corner cases. (NOW IMPLEMENTED)
