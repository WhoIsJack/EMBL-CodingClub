## Materials for EMBL Coding Club Mini-Tutorials

This repo collects a bunch of public materials for the [EMBL Coding Club](https://bio-it.embl.de/coding-club/).


### Contents

#### Coding Challenge: Grouping EMBL Groups
**Date & Time:** 15.12.2016, 17:00-19:00    
**Tutor:** Jonas    
**Level:** All Levels    
**Language:** Any    
**Abstract:** A coding challenge combining data analysis and visualization. The task is to analyze text descriptions of research groups at EMBL and automatically classify these groups into research units (or otherwise partition them in a meaningful manner based on similarities in the text).    


#### Mini-Tutorial: From (Python) Script to (Python) Program
**Date & Time:** 12.01.2017, 17:00-17:30    
**Tutor:** Jonas    
**Level:** Beginner and Intermediate    
**Language:** Python (though the basic considerations apply for all languages)    
**Abstract:** Every now and then, we all actually manage to finish a script. Good job, us! Next, we may want to use this script on a regular basis, probably with slightly different input and parameters each time. We may also want to make the script available for others to use, quickly and easily. One very simple way of accomplishing this is to make the script into a command-line executable program. This tutorial will illustrate how this can be done with a python example.    


#### Mini-Tutorial: Multiprocessing for Mortals
**Date & Time:** 23.03.17, 17:00-17:30    
**Tutor:** Jonas    
**Level:** Beginner and Intermediate    
**Language:** Python    
**Abstract:** We often work with relatively large datasets and with relatively slow algorithms (either by necessity or because we just don't know how to optimize our code). As a consequence, our scripts can take a long time to run. One very simple way of speeding things up is by running multiple independent processes at the same time - in short: multiprocessing. Although this can become quite complicated if you really get into it, python's multiprocessing module offers a very easy to use solution for the "common mortal". I will demonstrate its use with a simple example.    


#### Mini-Tutorial: Intro to ODEs
**Date & Time:** 04.05.2017, 17:00-17:30    
**Tutor:** Jonas    
**Level:** All Levels   
**Language:** General, with an example in Python (and one in Excel ;p)    
**Abstract:** Differential Equations provide an intuitive and powerful mathematical framework for modeling and simulating dynamical systems, in particular bio-chemical systems such as signaling pathways, metabolic pathways, or gene regulatory circuits. The basics of differential equation modeling are easy to grasp and readily applicable to learn something about any pathway of interest. In this tutorial, you will learn how to transform typical "arrow schemes" of pathways into a set of Ordinary Differential Equations (ODEs), and how to use these ODEs to simulate a pathway and understand its dynamics.    


#### Mini-Tutorial: Pipelines as Graphs
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


#### Coding Challenge: The Maze Stumbler
**Date & Time:** 27.07.2017, 17:00-19:00    
**Tutor:** Jonas    
**Level:** All Levels    
**Language:** Any    
**Abstract:** In this challenge, the aim is to program a bot that is able to navigate a maze and find the exit. For beginners, a basic working example is already provided for them to understand and build upon. Intermediate-level coders are expected to get to that point from scratch, whereas experts face the additional challenge of coding an "autonomous" bot, which improves upon its performance by means of machine learning instead of additional hard-coded rules.    


#### EPUG: Numpy Basics    
**Date & Time:** 31.03.2020, 16:00-17:00    
**Tutor:** Jonas    
**Level:** python basic/intermediate, numpy basic/intermediate    
**Language:** python    
**Abstract:** A brief introduction to the basics of numpy arrays and how to use them in scientific computing.    

#### EPUG: Numpy Simulation Example

**Date & Time:** 12.05.2020, 16:00-17:00    
**Tutor:** Jonas    
**Level:** python intermediate, numpy intermediate    
**Language:** python    
**Abstract:** Live coding of a simple implementation of a 2D particle model (with ballistic motion and elastic collision) to illustrate concepts and techniques in scientific computing with numpy and in numerical simulation in general.
