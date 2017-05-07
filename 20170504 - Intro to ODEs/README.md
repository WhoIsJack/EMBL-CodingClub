## Biological Modeling with Differential Equations
EMBL Coding Club Mini-Tutorial    
by Jonas Hartmann    
04.05.2017    


### Abstract

Differential Equations provide an intuitive and powerful mathematical framework for modeling and simulating dynamical systems, in particular bio-chemical systems such as signaling pathways, metabolic pathways, or gene regulatory circuits. he basics of differential equation modeling are easy to grasp and readily applicable to learn something about any pathway of interest. n this tutorial, you will learn how to transform typical "arrow schemes" of pathways into a set of Ordinary Differential Equations (ODEs), and how to use these ODEs to simulate a pathway and understand its dynamics.


### Notes

- The materials for this mini-tutorial are contained in the jupyter notebook `ODE_Mini_Tutorial.ipynb`.
    - If you are not working with jupyter, I recommend you [get into it](http://jupyter.org/)!
    - Alternatively, you can look through the tutorial inside a browser with the html file `ODE_Mini_Tutorial.html`.
    - Note that GitHub itself can also render notebooks, but html code used within the notebook (e.g. for colored text) does not get displayed correctly (at the time of writing this). It is therefore not recommended to read through the notebook directly on GitHub.

- The tutorial is built to be self-explanatory. However, given the limited scope of the mini-tutorial, it is naturally only a very superficial introduction to the field. Suggestions for further reading can be found at the end of the tutorial.

- The tutorial uses python 2.7, but it features very little actual python code. It can thus be appreciated regardless of your preferred language.


### Files

- `ODE_Mini_Tutorial.ipynb`
    - The jupyter notebook containing the tutorial.

- `ODE_Mini_Tutorial.html`
    - The html-exported version of the tutorial. Can be opened in browsers.

- `enzymatic_reaction.xlsx`
	- Fun example showing numerical solution of an ODE with Microsoft Office Excel.
	- Some more information on this can be found within the tutorial.

- `ipynb_figures/`
    - Directory containing figures for the tutorial.
    - This directory needs to be available as a subfolder inside the folder where the tutorial is saved, otherwise the tutorial will not display the figures.