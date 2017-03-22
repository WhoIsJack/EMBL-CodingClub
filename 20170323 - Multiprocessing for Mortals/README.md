## Multiprocessing for Mortals (M4M)
EMBL Coding Club Mini-Tutorial    
by Jonas Hartmann    
23.03.2017    


### Abstract

We often work with relatively large datasets and with relatively slow algorithms (either by necessity or because we just don't know how to optimize our code). As a consequence, our scripts can take a long time to run. One very simple way of speeding things up is by running multiple independent processes at the same time - in short: multiprocessing. Although this can become quite complicated if you really get into it, python's multiprocessing module offers a very easy to use solution for the "common mortal". I will demonstrate its use with a simple example. 


### Introduction

*TO BE ADDED*


### Files

- `M4M_simpleExample.py`
    - Trivial example of an algorithm where a loop sequentially performs many independent calculations.
    - Whenever we have such a loop, we can easily make it into a multiprocessed version.

- `M4M_simpleSolution.py`
	- The same algorithm as in simpleExample, but now made into a multiprocessed version.

- `M4M_exercise.py`
    - A slightly less trivial case. The exercise is to make this into a multiprocessed version.

- `M4M_exerciseSolution.py`
    - Multiprocessed version of the exercise.
    - *Not available yet!*