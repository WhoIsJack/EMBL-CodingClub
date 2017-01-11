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

# USER INPUT

# Path to the target directory
target_dir = r"/path/to/file"

# Flags
show_img = False        # Should the image be displayed with matplotlib?
save_png = False        # Should the image be saved as a png?


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



