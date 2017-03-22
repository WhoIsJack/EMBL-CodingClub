# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:11:12 2017

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  Example of simple multiprocessing in Python.
            This is the solution where the loop is replaced by multiprocessing.
"""

# Calculation to perform (now as function)
def square(value):
    value_squared = value * value
    from time import sleep
    sleep(0.5)
    return value_squared

# Protection from recursive multiprocessing
if __name__ == '__main__':

    # Values to loop over (input)
    values = range(100)
    print values

    # Preparing for multiprocessing
    from multiprocessing import Pool
    workerPool = Pool(processes=4)

    # Timing how long the multiprocessing takes
    from time import time
    start = time()

    # Running the multiprocessing
    results = workerPool.map(square,values)

    # How long did it take?
    print '\n', time() - start, 'sec'

    # Printing the result
    print '\n', results

