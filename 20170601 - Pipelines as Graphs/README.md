## Easily Organise and Parallelise Your Python Workflow Using a ‘Task Scheduler’
EMBL Coding Club Mini-Tutorial    
by Marvin Albert    
01.06.2017    


### Abstract

The goal of this mini-tutorial will be to become familiar with an intuitive and straight-forward way to define data analysis/processing pipelines in python, which
- structures code to keep it simple and reproducible
- manages the workflow and lets us focus on our pipeline’s goals
- provides automatic parallelisation on a laptop or cluster.

More specifically, we will identify the data dependencies of a given data processing pipeline and break it down into elementary tasks. This will lead to a graph representation of our problem in which
- nodes represent the data and intermediate results
- edges represent data dependencies and processing functions.

Having defined such a graph in a simple python dictionary we will then use the python module dask to conveniently handle the execution, visualisation and parallelisation of our workflow.