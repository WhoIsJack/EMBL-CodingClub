## Materials for EMBL Coding Club Mini-Tutorials
This repo collects my materials (as well as possibly those of some other tutors in the future) for the mini-tutorials held at the EMBL coding club.


### Contents

#### From (Python) Script to (Python) Program
**Date & Time:** 12.01.2017, 17:00-17:30    
**Tutor:** Jonas    
**Level:** Beginner and Intermediate    
**Language:** Python (though the basic considerations apply for all languages)    
**Abstract:** Every now and then, we all actually manage to finish a script. Good job, us! Next, we may want to use this script on a regular basis, probably with slightly different input and parameters each time. We may also want to make the script available for others to use, quickly and easily. One very simple way of accomplishing this is to make the script into a command-line executable program. This tutorial will illustrate how this can be done with a python example.    

#### Multiprocessing for Mortals
**Date & Time:** 23.03.17, 17:00-17:30    
**Tutor:** Jonas    
**Level:** Beginner and Intermediate    
**Language:** Python    
**Abstract:** We often work with relatively large datasets and with relatively slow algorithms (either by necessity or because we just don't know how to optimize our code). As a consequence, our scripts can take a long time to run. One very simple way of speeding things up is by running multiple independent processes at the same time - in short: multiprocessing. Although this can become quite complicated if you really get into it, python's multiprocessing module offers a very easy to use solution for the "common mortal". I will demonstrate its use with a simple example.    


#### Biological Modeling with Differential Equations
**Date & Time:** 04.05.2017, 17:00-17:30    
**Tutor:** Jonas    
**Level:** All Levels   
**Language:** General, with an example in Python (and one in Excel ;p)    
**Abstract:** Differential Equations provide an intuitive and powerful mathematical framework for modeling and simulating dynamical systems, in particular bio-chemical systems such as signaling pathways, metabolic pathways, or gene regulatory circuits. The basics of differential equation modeling are easy to grasp and readily applicable to learn something about any pathway of interest. In this tutorial, you will learn how to transform typical "arrow schemes" of pathways into a set of Ordinary Differential Equations (ODEs), and how to use these ODEs to simulate a pathway and understand its dynamics.    


#### Easily Organise and Parallelise Your Python Workflow Using a ‘Task Scheduler’
**Date & Time:** 01.06.2017, 17:00-17:30    
**Tutor:** Marvin Albert    
**Level:** All Levels    
**Language:** Python    
**Abstract:** 
The goal of this mini-tutorial will be to become familiar with an intuitive and straight-forward way to define data analysis/processing pipelines in python, which
- structures code to keep it simple and reproducible
- manages the workflow and lets us focus on our pipeline’s goals
- provides automatic parallelisation on a laptop or cluster.

More specifically, we will identify the data dependencies of a given data processing pipeline and break it down into elementary tasks. This will lead to a graph representation of our problem in which
- nodes represent the data and intermediate results
- edges represent data dependencies and processing functions.

Having defined such a graph in a simple python dictionary we will then use the python module dask to conveniently handle the execution, visualisation and parallelisation of our workflow.    


