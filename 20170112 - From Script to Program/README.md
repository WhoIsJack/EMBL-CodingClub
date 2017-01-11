## From (Python) Script to (Python) Program
EMBL Coding Club Mini-Tutorial
by Jonas Hartmann
12.01.2017

### Abstract
Every now and then, we all actually manage to finish a script. Good job, us! Next, we may want to use this script on a regular basis, probably with slightly different input and parameters each time. We may also want to make the script available for others to use, quickly and easily. One very simple way of accomplishing this is to make the script into a command-line executable program. This tutorial will illustrate how this can be done with a python example.


### Introduction

#### The Command-Line
Command-line interfaces provide a simple and efficient way of interacting with programs and operating systems. The command-line is ideal for making scripts developed in a scientific context readily re-usable.

To get an introduction to the Linux command-line (called "Bash"), be on the look-out for the corresponding Bio-IT courses (check [here](https://bio-it.embl.de/events/)), or check out the materials of the basic course [here (git)](https://git.embl.de/dinkel/linuxcommandline/tree/master/linux_beginner) or [here (pdf)](https://git.embl.de/dinkel/linuxcommandline/raw/master/linux_beginner/_build/latex/IntroductiontotheLinuxCommandline.pdf) (internal access only). An alternative online introduction to Bash can be found [here](http://linuxcommand.org/). The command-lines of different operating systems are slightly different, but if you get how one works you get how all of them work. I would recommend learning Bash first; it can also be used on operating systems other than Linux.

For this mini-tutorial, **you don't need prior experience with the command-line**, but of course you should learn at least the basics if you are planning on using the command-line to handle your scripts.


#### Running Programs

In general, statements on the command-line have the following order:

```command options arguments```

- *Command:* what to do
- *Options:* how to do it
- *Arguments:* further specifications, i.e. on what data to operate

In a bit more detail, this is what a statement might look like for running a python program:

```python Scriptname.py positional_argument --optional argument --someFlag -x```

Example:

```python calculate_age.py my_birthday --currentdate 20170112 --days```

- The command here is `python`, telling the command-line to use the python installation on the system to run something.
- The second element (an 'option') is the script that python is suppposed to run. If you just want to run a script (without passing any additional arguments), simply typing ```python Scriptname.py``` will be enough. It is essentially the same as double-clicking the script file in the graphical user interface.
- The remaining elements are the arguments:
	- The first is a *positional argument*. The script must be configured to interpret positional arguments based on their position (unsurprisingly). Positional arguments are usually mandatory, meaning the script should raise an error if they are not given.
	- The second and third together are an *optional argument*. In the example, `--currentdate` indicates that the next element will be the argument named "currentdate", which here is `20170112`. If the user does not specify the optional argument, the program should still run and produce a useful output, for example by using a default value.
	- The fourth and fifth arguments are both *flags*, one in the typical long form (`--someFlag`), the other in the short form (`-x`). Flags are a way of telling the program to do something in a particular way. If a flag is not passed, the program should do things in a "default" way. In the example, the flag `--days` might demand the age to be calculated in days, whereas the default might be years.


### Making a Script Into a Command-Line Program
To make your script usable from the command-line, all you need to do is add some code to the beginning of the script to parse the command-line arguments. Many programming languages come with modules that make this easier. In python, the recommended module is [argparse](https://docs.python.org/3/library/argparse.html) (introductory tutorial [here](https://docs.python.org/3/howto/argparse.html#id1)). In this mini-tutorial, however, will not use such a pre-made module and instead look at a simple example of how to parse command-line arguments explicitely. For simple scripts, this can be easier than using a pre-made module, plus it has the advantage of illustrating the general principle (applicable in a similar way to most languages).


#### Tutorial Contents
- `ex_raw.py` A small example script *before* it is made into a command-line program.
- `ex_instructions.py` The same example script but with instructions for what needs to be done to make it into a command-line program.
- `ex_fin.py` The solution, i.e. the same example script but now ready for use from the command-line.
- `ex_bonus.py` Here I was just having some extra fun. ;p

In the mini-tutorial at the coding club, we will fill in the blanks in `ex_instructions.py` together.


#### Bonus Exercise
Write an implementation of *calculate_age.py* (it should be pretty clear what it should do just from its name) and configure it such that it can parse the arguments in the example above. You can of course use a language other than python if you prefer.

Note: If you are using python and planning on creating some more sophisticated command-line programs in the future, you may also want to use the exercise to try out [argparse](https://docs.python.org/3/library/argparse.html), as it is more convenient than manual argument parsing in many cases (in particular, it is easier to maintain when you make changes to your program).

