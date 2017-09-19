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

# Get the command-line arguments
import sys
argv = sys.argv

# Display help
if '-h' in argv or '--help' in argv:
    print """
    Help for ex_fin:
    
        ex_fin TARGETDIR [-i] [-s|--save-png] [-e EXAMPLE]
    
    Given a target directory, a simple 'avatar' is generated (based on  
    the hash of the directory's name). The avatar can be saved as a png 
    image or displayed with matplotlib.        
    
    PARAMETERS
    ----------
    TARGETDIR: string
        Path of the target directory. This path will be hashed and used as the
        seed for avatar generation.
    -i: flag
        If passed, the avatar will be displayed with matplotlib.
    -s|--save-png: flag
        If passed, the avatar will be saved to the target dir as a png.
    -e EXAMPLE: integer
        An example of an optional integer argument. This is just to illustrate
        further cmd-line handling, it has no effect on the program.
        Default is 42.
        
    DEPENDENCIES
    ------------
    python 2.7.11
    numpy 1.11.0
    matplotlib 1.5.1
    """
    sys.exit()

# Display version
if '--version' in argv:
    print "ex_fin version 0.1"
    sys.exit()

# Check if the number of parameters makes sense
if len(argv) < 2 or len(argv) > 6:
    raise IOError("Inconsistent number of arguments. See ex_fin -h for help.")
    
# Get the target directory name
target_dir = argv[1]

# Check if it is really a directory
import os
if not os.path.isdir(target_dir):
    raise IOError(target_dir+" not found or invalid. See ex_fin -h for help.")

# Get flag -i; should the image be displayed?
if '-i' in argv:
    show_img = True
else:
    show_img = False
    
# Get flags -s|--save-png; should the image be saved as png?
if '-s' in argv or '--save-png' in argv:
    save_png = True
else:
    save_png = False

# Get the integer parameter (or set to default)
if '-e' in argv:
    try: 
        example_integer = int(argv[argv.index('-e')+1])
    except ValueError:
        raise IOError("-e must be an integer. See ex_fin -h for help.")
else:
    example_integer = 42


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



