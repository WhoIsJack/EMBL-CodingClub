# -*- coding: utf-8 -*-
"""
Created on Sun Jan 08 15:21:56 2017

@author:        Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@description:   Given a target directory, a simple 'avatar' is generated (based
                on the hash of the directory's name). The avatar can be saved
                as a png image, displayed with matplotlib or set as the icon of
                the target directory (Windows only).

@WARNING:       Setting the target directory's icon to the avatar will overwrite
                desktop.ini in the target directory. For any normal directory,
                this ought not be a problem, but if a directory is already
                customized or has special properties (e.g. Desktop, Downloads)
                this may cause problems!

@purpose:       This script serves as a simple (but fun?) example for an EMBL
                coding club mini-tutorial on how to make python scripts into
                command-line programs.
                
@dependencies:  python 2.7.11
                numpy 1.11.0, matplotlib 1.5.1, PIL 1.1.7
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
    Help for ex_bonus:
    
        ex_bonus TARGETDIR [-i] [-s|--save-png] [--set-dir-icon]
    
    Given a target directory, a simple 'avatar' is generated (based on  
    the hash of the directory's name). The avatar can be saved as a png 
    image or displayed with matplotlib. It can also be set as the target
    directory's new icon (Windows only).       
    
    PARAMETERS
    ----------
    TARGETDIR: string
        Path of the target directory. This path will be hashed and used as the
        seed for avatar generation.
    -i: flag
        If passed, the avatar will be displayed with matplotlib.
    -s|--save-png: flag
        If passed, the avatar will be saved to the target dir as a png.
    --set-dir-icon: flag
        If passed, the avatar will be set as the new icon of the target dir.
        Works on Windows only.
        WARNING: This action overwrites desktop.ini in the target directory.
        This is fine for normal directories but probably shouldn't be done for
        special directories (such as Downloads, System Files, Desktop, ...)!
        
    DEPENDENCIES
    ------------
    python 2.7.11
    numpy 1.11.0
    matplotlib 1.5.1
    PIL 1.1.7
    """
    sys.exit()

# Display version
if '--version' in argv:
    print "ex_bonus version 0.1"
    sys.exit()

# Check if the number of parameters makes sense
if len(argv) < 2 or len(argv) > 6:
    raise IOError("Inconsistent number of arguments. See ex_bonus -h for help.")
    
# Get the target directory name
target_dir = argv[1]

# Check if it is really a directory
import os
if not os.path.isdir(target_dir):
    raise IOError(target_dir+" not found or invalid. See ex_bonus -h for help.")

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

# Get flag --set-dir-icon
if "--set-dir-icon" in argv:
    generate_icon = True
    
    # Warn and demand explicit permission
    check = raw_input("WARNING: You have specified --set-dir-icon! Are you sure [Y/[N]]: ")
    if check != 'Y':
        print "Please check ex_bonus -h for more informations."
        sys.exit()
        
else:
    generate_icon = False


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
import os
if save_png or generate_icon:    
    savepath_png = os.path.join(target_dir,'logo.png')           # Path to save in target dir
    plt.savefig(savepath_png,bbox_inches='tight',pad_inches=0)   # Saving the image
    
# Display the image
if show_img:
    plt.show()


#------------------------------------------------------------------------------

# SETTING THE IMAGE AS DIRECTORY ICON

# If desired, set the img as the directory's icon
if generate_icon:
    
    if not os.name == 'nt':
        raise OSError("Icon generation only implemented for Windows!")        
        
    # Convert to an ico file using PIL
    from PIL import Image
    img = Image.open(savepath_png)
    savepath_ico = os.path.join(target_dir,'folder.ico')
    img.save(savepath_ico)

    # Remove the png file unless saving is desired
    if not save_png:
        os.remove(savepath_png)

    # Generate the desktop.ini file that sets the directory icon
    savepath_ini = os.path.join(target_dir,'desktop.ini')
    if os.path.isfile(savepath_ini): # To avoid permission issue if the file already exists
        os.system('attrib -s "'+savepath_ini+'"')
    with open(savepath_ini,"w") as outfile:
        outfile.write("""[.ShellClassInfo]\nIconResource=folder.ico,0""")

    # Adjust the file and directory properties so it displays the icon
    # Note: The alternative with hiding will hide the desktop.ini file because
    #       it's ugly to have it lying around in the folder. However, for
    #       illustration the alternative without hiding is preferred.
    os.system('attrib +s "'+savepath_ini+'"')      # Alternative without hiding
    #os.system('attrib +s +h "'+savepath_ini+'"')  # Alternative with hiding
    os.system('attrib +r "'+target_dir+'"')


#------------------------------------------------------------------------------



