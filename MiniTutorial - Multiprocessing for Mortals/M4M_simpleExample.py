# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:11:12 2017

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  Example of simple multiprocessing in Python.
            This is the 'original' code, in which a loop sequentially performs
            a series of independent calculations. To speed up this code, one
            can parallelize it so that multiple of these calculations are run
            at once instead of one after the other.
            See m4c_simpleSolution.py for the multiprocessed version.
"""

# Values to loop over (input)
values = range(100)
print values

# List to collect the results
results = []

# Timing how long the loop takes
from time import time
start = time()

# Loop over the values
for value in values:

    # Calculation to perform
    value_squared = value * value

    # The above calculation is anyway very fast, so it is not very good to
    # demonstrate the power of multiprocessing. Let's delay things a bit
    # by waiting for half a second
    from time import sleep
    sleep(0.5)

    # Appending result to result list
    results.append(value_squared)

# How long did it take?
print '\n', time() - start, 'sec'

# Print the result
print '\n', results

