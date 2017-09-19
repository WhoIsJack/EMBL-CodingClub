# -*- coding: utf-8 -*-
"""
Created on Sun Jan 08 15:21:56 2017

@author:        Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@description:   Given a target directory, a simple 'avatar' is generated (based
                on the hash of the directory's name). The avatar can be saved
                as a png image or displayed with matplotlib.

@purpose:       This script serves as a simple (but fun?) example for an EMBL
                coding club mini-tutorial on how to make python scripts into
                command-line programs.
                
@dependencies:  python 2.7.11
                numpy 1.11.0, matplotlib 1.5.1
                (or equivalent)
"""

#------------------------------------------------------------------------------

# USER INPUT from command-line

# First we need to somehow get the command-line arguments into the script
import sys
argv = sys.argv
# ->> argv is a list of strings, where each string is an argument from the 
#     command-line, split at blank spaces. Try printing argv and understand 
#     how it relates to the input on the command-line.


# Every command-line program should print help when asked to do so
# ->> The two most common arguments to get help are '--help' and '-h'
# ->> The format of the printed help can vary, but usually it shows at least
#     how program is used, what it does, and which arguments it accepts.
#     The format here is more inspired by python's help function, which I find
#     very nice to read. Check out the -h or --help options on other cmd-line
#     commands to get an idea of format and content of the help sections!
if '-h' in argv or '--help' in argv:
    print """
    Help for program_name:
    
        program_name POSITIONAL_ARG [--optional ARG] [-a|--a_flag] [-b] [--c_flag]
    
    Here goes a sentence or two on how the program works.
    
    PARAMETERS
    ---------
    POSITIONAL_ARG: argument_type
        A sentence or two describing the argument goes here!
    --optional ARG: argument_type
        Optional arguments do not have to be given. Often, a default value is
        assumed if they are not specified. The default value should be noted 
        here.
    -a|--a_flag: flag
        Flags trigger the program to do something if they are passed. They can
        be optional or a mandatory choice between several otions. Also, they 
        usually come as single letters with a single dash (e.g. -a) or as a
        full word with a double dash (e.g. --a_flag). The | indicates that
        the user can specify either the full flag or the single letter.
    -b: flag
        Some flags do not have a full word option...
    --c_flag: flag
        ...and some flags do not have a single letter options. It is up to you
        to decide what is the most convenient way of handling your program!
    
    MORE INFORMATION
    ----------------
    You can add more info, such as infos on what the output will look like, or
    the dependencies of your program, or whom to contact with bug reports, etc.
    """
    # After displaying the help, the program should terminate.
    # ->> This can also be done with the sys module!


# Another thing all cmd-line programs should provide is the version number of
# the currently installed program.
if '--version' in argv:
    print "program_name version VERSION_NUMBER"
    # After this call, the program shouild also terminate!
    # ->> See above.


# As a simple check for consistency, I like to check if the number of arguments
# provided make sense
# ->> This is easy to do with an if-statement
    # If the number of arguments is incorrect, this can be reported via an
    # error, for example an IO error
    raise IOError("Inconsistent number of arguments. Check program_name -h for help!")


# Now it's time to actually parse the arguments.
# In this program, the first argument is a mandatory argument that specifies
# a target directory. In ex_raw, this parameter was specified like this:
target_dir = r"/path/to/file"
# Instead, we now take the argument from the command-line:
target_dir = argv[1]
# Done - it's really simple for mandatory arguments that are strings! If this
# argument was a number, we would have to convert it, e.g. float(argv[1]).


# However, we want to be careful and make sure that the given path actually
# makes sense.
# --> Use os.path.isdir to check if the specified directory exists.
# --> If it does not exist, raise an appropriate IOErrro.


# Next, we want to parse the flags. In this program, we have to specify two
# things using flags:
# show_img   # Should the image be displayed with matplotlib?
# save_png   # Should the image be saved as a png?
# ->> We already learned how to check for flags when we displayed the help and
#     version number above, so it should be easy to do.
if something: # <-- write an expression here to check if the flag is present
    show_img = True
else:
    show_img = False


# ->> And the same for save_png.
   
   
# Finally, let's assume as an example that we get also have an optional
# argument that is an integer
#   -e EXAMPLE
# ->> If -e is not given, the variable example_integer should be set to the
#     default value, which is 42. 
# ->> Otherwise, example_integer should be set to EXAMPLE. Note that the order 
#     of optional arguments and flags is usually not fixed, so EXAMPLE has to 
#     be extracted relative to -e.


#------------------------------------------------------------------------------

# GENERATING THE IMAGE

# Hash the directory
import hashlib
dir_hash = hashlib.md5(target_dir).hexdigest()

# Convert first 8 digits of hash to a base 10 int
dir_hash = int(dir_hash[:8],base=16)

# Use the digits to seed numpy's random number generator
import numpy as np
np.random.seed(dir_hash)

# Create half a random image, then mirror it to get symmetry (looks better)
img = np.zeros((10,10),dtype=np.uint16)
img[:,:5] = np.random.binomial(1,0.4,size=(10,5))
img[:,5:] = np.fliplr(img[:,:5])

# Pick a random foreground color (background always white); create cmap
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
randomColor = plt.cm.jet(np.random.randint(0,256))
randomCmap = LinearSegmentedColormap.from_list('randomCmap',[(1.0,1.0,1.0,1.0),randomColor])

# Create the image
plt.imshow(img,interpolation='nearest',cmap=randomCmap)  # Generate image
plt.axis('off')                                          # Remove outside stuff
plt.gca().get_xaxis().set_visible(False)                 # Remove outside stuff
plt.gca().get_yaxis().set_visible(False)                 # Remove outside stuff

# Save the image to the target directory
if save_png:
    import os
    savepath = os.path.join(target_dir,'logo.png')           # Path to save in target dir
    plt.savefig(savepath,bbox_inches='tight',pad_inches=0)   # Saving the image

# Display the image
if show_img:
    plt.show()


#------------------------------------------------------------------------------



