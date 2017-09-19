# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:11:12 2017

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  Example of simple multiprocessing in Python.
            This is the solution where the loop is replaced by multiprocessing.
            
            Steps to reach this solution:
                1) Transform the operations done within the loop into a
                   function, here the function 'square'.
                2) Import the Pool class from the multiprocessing module
                   and generate a pool of worker processes.
                3) Give the worker pool the function they are supposed
                   to compute (here 'square') together with a list of 
                   all the inputs for which that function should be
                   evaluated (here 'values').
                4) 'Protect' all statements that should not be 're-run'
                   by the subprocesses.
"""

# Calculation to perform (now as function)
def square(value):
    value_squared = value * value
    from time import sleep
    sleep(0.5)
    return value_squared

# Protection from recursive multiprocessing
# Note: The new subprocesses generated in multiprocessing will "re-run" the
#       script to "learn" about function definitions and variables (e.g. the
#       function square). This if-statement ensures that the lines below are
#       not re-executed in the subprocesses.
if __name__ == '__main__':

    # Values to loop over (input)
    values = range(100)
    print values

    # Preparing for multiprocessing by generating a "pool" of worker processes
    # Note: The ideal number of processes depends on the computer you are using
    #       and on the algorithm you are running. As a starting point, use the
    #       number of CPUs on the machine minus one (the remaining CPU can host
    #       other processes, including the operating system). This can be done
    #       automatically using the function cpu_count.
    from multiprocessing import Pool, cpu_count
    workerPool = Pool(processes=cpu_count()-1)

    # Timing how long the multiprocessing takes
    from time import time
    start = time()

    # Running the multiprocessing
    # Note: This basically tells the pool of worker processes what to work on.
    results = workerPool.map(square,values)

    # How long did it take?
    print '\n', time() - start, 'sec'

    # Printing the result
    print '\n', results

