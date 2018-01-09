#!/usr/bin/env python3

"""
    File: monitor.py
    Author: Jim Craveiro <jim.craveiro@gmail.com>
    Date: 1/9/2018
    
    Program to monitor and log network connectivity
    using python 3 standard libraries only
"""

import sys
import time
import signal
import logging
from urllib.request import urlopen

LOG_PATH      = './'
LOGGER_FORMAT = '%(asctime)s %(levelname)s - %(message)s'
TEST_URL      = 'https://www.google.com'
TEST_PERIOD   = 20

"""
    function that calls urlopen to the specified TEST_URL and logs status
    excepts all errors and logs them
    params:
        logger (object) - logging object
"""
def test_network(logger):
    try:
        response = urlopen(TEST_URL)
        logger.info('connected')
    except Exception as error:
        logger.error(str(error))

"""
    function that creates a logger in a specified LOG_PATH and with the 
    specified format LOGGER_FORMAT, then returns the logging object
    params:
        name (string) - name of logger
    return:
        (object) - logging object
"""
def make_logger(name):
    handler   = logging.FileHandler('{}{}.log'.format(LOG_PATH, name), mode='a')
    formatter = logging.Formatter(LOGGER_FORMAT)
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

"""
    signal handler for sigint; exits program
    params:
        signum (int) [unused] - number representing the signal being passed to handler
        frame (object) [unused] - stack frame interrupted by signal
"""
def on_sigint(signum, frame):
    sys.exit()

"""
    main function that sets up signal handler, creates the logger, and holds
    the main loop that calls the testing function on a period specified by TEST_PERIOD
"""
def main():
    signal.signal(signal.SIGINT, on_sigint)
    logger = make_logger('uptime')
    while True:
        test_network(logger)
        time.sleep(TEST_PERIOD)

if __name__ == '__main__': main()
