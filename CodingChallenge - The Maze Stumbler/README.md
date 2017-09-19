**WELCOME** to the **Coding Club Summer Challenge 2017**:


## The Maze Stumbler


**featuring:**

- Teresa, the bot
- You, the programmer

**created and directed by:**

- Jonas Hartmann (Gilmour group, EMBL Heidelberg)

----

### Background

This Challenge is intended as an opportunity for EMBL's novice and expert coders to come together and have a good time for a couple of hours, while also hopefully learning something new about coding! **;)**

The instructions below detail how the challenge works. Note that there are different levels, geared toward `beginner`, `intermediate` and `advanced` coders, respectively. However, you are completely free to decide yourself which level you would like to work on and how you would like to approach the challenge.

If you like, feel free to work together in groups of 2 or 3. Also, **don't hestitate to ask more experienced coders for help** if you are stuck!

**Have fun!**


### The Challenge

In this repository, you will find a set of generated mazes saved as text files. The mazes are represented as a `2D binary array`, where `1` stands for `corridor` and `0` stands for `wall`. The entrance to each maze is at the top left and the exit at the bottom right.

The goal of this challenge is to program a `bot` (an `autonomous program`) that starts at the maze entrance and finds its way to the exit.

Note that this is *not* the same as using an algorithm that automatically finds the shortest path through the maze, because such algorithms usually "see" the entire maze as input. Your bot, which is named `Teresa` (unless you want to give it a different name - it's up to you!), should only be able to see its immediate surroundings.


### Skill Levels

Depending on your coding skill level, you can approach this challenge in different ways:


- For the *beginners:*
	- There is example code already available, which shows how to load and display a maze
		- `example_teresa_jupyter_py27.ipynb` -- python 2.7 example for jupyter notebook
		- `example_teresa_python27.py` -- python 2.7 example as regular .py file
		- `example_teresa_R.R` -- R example *(beta version ;p)*
		- There is no MATLAB example as of now, but the python code should be easy to translate
	- The example also contains a very simple version of the Teresa-bot
	- As a first task, you should try and fully understand how the example code works
	- You will quickly realize that Teresa explores the maze very inefficiently in this example
    - Can you make improvements to Teresa so she becomes better at it?


- For the *experienced:*
    - Create your own custom version of Teresa from scratch
    - Feel free to get some inspiration from the example code mentioned for the beginners...
    - ...but your implementation should ultimately be your own (and better than the example!)
    - To test your Teresa, let her explore many mazes of different size and analyze the results!
    - Try to incorporate things you have recently been learning about:
    	- Have you been learning about object-oriented programming?
    		- Make sure Teresa is a class!
    	- Currently looking into cool visualizations?
    		- Create a movie showing Teresa's progress!
    		- Or how about an interactive plot!
    	- Know about multiprocessing?
    		- Let an army of Teresa's explore all the different mazes in parallel!
        - Learning a new language?
        	- Solve the challenge using this new tool!
		- And so on, and so forth...


- For the *advanced:*
	- If the above looks like child's play to you, here's your **serious** challenge:
		- Your Teresashould be an `intelligent, learning agent!`
	- Do not program any rules for her behavior; let her learn and get better on her own!
		- You could for example implement Teresa as a `Neural Network` and train her by optimizing some sort of `success measure`, using approaches such as `back-propagation` or `evolutionary optimization`
		- Make sure your implementation allows for good `memory`, since remembering where she has already been is likely key to Teresa's success
	- Feel free to choose between using existing packages or writing your own implementations
	- *There are 2 subchallenges*:
		1. Train on the same maze repeatedly to see how Teresa improves by getting to know a specific maze
			- This should work fairly well but will likely produce a Teresa that can only solve that particular maze
		2. Train on many different mazes to see if Teresa can get better at solving mazes in general


*At the end, feel free to briefly show off your ideas and what you achieved (this is not a must, though)!*

----

**Can you make your Teresa into a Maze Runner?! Or will she be just another Stumbler?**

***Good luck! :) ***
