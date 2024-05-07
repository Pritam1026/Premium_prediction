from insurance.logger import logging
from insurance.exception import InsuranceException
import sys

def test_logger_and_exception():
    try:
        logging.info('Starting the test logger and exception')
        result=3/0
        print(result)
        logging.info('Ending the test logger and exception')
    except Exception as e:
        logging.error(str(e))
        raise InsuranceException(e,sys)

if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)
