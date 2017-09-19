# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:11:12 2017

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  Exercise on simple multiprocessing in Python.
            This code contains a loop that produces some interesting results
            but takes a while to run (about 2min with the default settings,
            depending on your computer).
            As an exercise, see if you can create a multiprocessed version of
            this and then check how much faster it gets.
"""

# Some imports
import numpy as np
import matplotlib.pyplot as plt

# Some parameters
r_start = -2.2
r_end   =  1.0
i_start = -1.4
i_end   =  1.4
resolution = 1000
# Note: Increasing the resolution improves the quality of the result but also
#       takes exponentially longer to compute! It is recommended to decrease
#       the resultion to 100 when testing modifications to the code!

# Lists to collect the results
results_r = []
results_i = []

# Loop [TO BE CONVERTED TO MULTIPROCESSING]
print '\nPerforming calculations...'
for r in np.linspace(r_start,r_end,resolution):

    # Second loop containing funky [DO NOT CONVERT]
    for i in np.linspace(i_start,i_end,resolution):

        z = complex(0)
        c = complex(r,i)
        converge = True

        for step in range(150):

             try:
                 z = z**2 + c
                 x = z.real
                 y = z.imag
                 if str(x) == 'nan' or str(y) == 'nan':
                     converge = False
                     break

             except Exception:
                 converge = False
                 break

        if converge:
             results_r.append(r)
             results_i.append(i)

# Done
print '\nCalculations complete!'

# Plotting
nice_coloring = [np.sqrt(r**2.0 + i**2.0) for r,i in zip(results_r,results_i)]
plt.scatter(results_r,results_i,
            c=nice_coloring,cmap=plt.cm.inferno_r,
            s=5,edgecolor="")
plt.xlabel("r")
plt.ylabel("i")
plt.axis('equal')
plt.show()



