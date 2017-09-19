# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:14:42 2016

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  A reduced version of the other (more elaborate) example solution,
            working only with embl_group_words.txt as an input. 
            
            The following points are showcased:
              - Explicitly parsing a particular text file (pure python)
              - Organizing data in a feature space (with numpy)
              - Analyzing feature spaces by PCA and tsNE (with scikit-learn)
              - Transforming the feature space into an adjacency matrix
              - Visualizing a graph using networkx
             
@WARNING:   Note that this code should be carefully examined and understood 
            before it is re-used for any actual scientific work. I can in no 
            way guarantee that the way I do things here is "right"!

"""


#------------------------------------------------------------------------------

# PREP

# Imports
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


#------------------------------------------------------------------------------

# DATA IMPORT

# Name of input file
infile_name = "embl_group_words.txt"
    
# Load and parse the data
with open(infile_name,'r') as infile:
    
    # For every line in the file...
    samples = []
    data = {}
    for line in infile.readlines():         
        
        # Clean
        line = line.strip()
        
        # If it's a header, get the name
        if line.startswith("###"):
            samples.append(line[4:])
            current_name = line[4:]
            continue            
    
        # If it's an empty line, skip it
        if line == '':
            continue        
    
        # Otherwise, get the words
        line_words = line.split(', ')
        data[current_name] = np.array(line_words)

# Get a list of all unique words (features)
features = sorted(set([w for name in data.keys() for w in data[name]]))

# Make things into arrays for convenience and speed
samples  = np.array(samples)
features = np.array(features)
    
# Create the feature space: an array of samples-x-features holding word counts
fspace = np.zeros((len(samples),len(features)))
for s_index,name in enumerate(samples):
    for word in set(data[name]):
        
        # Count the words and add them to the appropriate position in the feature space
        wordcount = np.sum(data[name]==word)
        fspace[s_index,np.where(features==word)] = wordcount
        
        
#------------------------------------------------------------------------------

# ADDITIONAL CLEAN UP

# Focus on specialized vocabulary by removing words that are in a common language corpus
from nltk.corpus import gutenberg                            # Get the corpus
standard_words = set(w.lower() for w in gutenberg.words())   # Get the words
keep = sorted(set(features) - standard_words)                # Keep features not in corpus
keep = [np.where(features==w)[0][0] for w in keep]           # Get indices to keep
fspace = fspace[:,keep]                                      # Remove from fspace
features = features[keep]                                    # Remove from feature list

# Remove words that appear in only one or all but one texts
keep = np.where(np.logical_and(fspace.sum(axis=0) > 0, fspace.sum(axis=0) < fspace.shape[0]))[0]
fspace = fspace[:,keep]
features = [f for i,f in enumerate(features) if i in keep]


#------------------------------------------------------------------------------

# GET COLORS BY UNIT

# Use the faculty list to generate a colormap based on units
with open('faculty_list.txt','r') as infile:
    
    # Define colors
    unit_cmap = {'CBB':0.0,'DB':0.23,'GB':0.76,'SCB':1.0}   # Color values chosen empirically
    
    # Read in units for each group name
    name_unit_dict = {}
    for line in infile.readlines():
        line = line.strip().split('\t')
        name_unit_dict[line[0]] = line[1]
    
    # Construct a list of colors that maps to samples
    sample_colors = np.array([unit_cmap[name_unit_dict[name]] for name in samples])


#------------------------------------------------------------------------------

# ANALYSIS BY PCA OR tSNE

## Normalize and standardize the features
## NOTE: Normalizing data to mean=0 and standardizing them to unit variance is
##       usually a very good idea but seems to hurt more than help here!
#fspace = (fspace - fspace.mean(axis=0)) / fspace.std(axis=0)


# Perform PCA with scikit-learn
# Note: This doesn't work very well; the data is pretty much a spherical cloud
#       and does not have relevant axes of variance
from sklearn.decomposition import PCA
pca_estimator = PCA(copy=True)     # Instantiate estimator
pca_estimator.fit(fspace)          # Fit data
fspace_pca = pca_estimator.transform(fspace)                              # Transform data to PC space
#print "PC-explained variance:", pca_estimator.explained_variance_ratio_  # Print PC variance

# Simple scatterplot of pc1 vs pc2
plt.scatter(fspace_pca[:,0],fspace_pca[:,1],
            c=sample_colors,s=50,lw=0,cmap=plt.cm.seismic)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.axis("equal")
plt.title("PCA")
plt.show()


# Perform tSNE with scikit-learn
from sklearn.manifold import TSNE
model = TSNE(n_components=2, random_state=999)
fspace_tsne = model.fit_transform(fspace)                 # On full data
#fspace_tsne = model.fit_transform(fspace_pca[:,:10])     # On reduced PCA data

# Scatterplot of tSNE1 vs tSNE2
plt.scatter(fspace_tsne[:,0],fspace_tsne[:,1],
            c=sample_colors,s=50,lw=0,cmap=plt.cm.seismic)
plt.xlabel("tSNE1")
plt.ylabel("tSNE2")
plt.axis("equal")
plt.title("tSNE")
plt.show()


#------------------------------------------------------------------------------

# NETWORK VISUALIZATION: PREPARATION

# Create adjacency matrix from feature space
adj_mat = np.dot(fspace,fspace.T)

# Normalize weights between 0 and 1
adj_mat = (adj_mat - adj_mat.min()) / (adj_mat.max() - adj_mat.min())

# Threshold adjacency matrix to remove low-relevance edges
adj_mat = adj_mat - np.percentile(adj_mat,50)
adj_mat[adj_mat<0] = 0


#------------------------------------------------------------------------------

# NETWORK VISUALIZATION: PLOTTING

# Prepare to plot graph with networkd
import networkx as nx
D = nx.from_numpy_matrix(adj_mat)    

# Layout of node positions
#pos = nx.circular_layout(D)                # Just a circle
pos = nx.spring_layout(D,weight=D.edges)    # Force-directed
#pos = fspace_tsne[:,:2]                    # tsne distribution
#pos = nx.nx_pydot.graphviz_layout(D)       # Better force-directed (requires graphviz)

# Get the weights to adjust edge colors and widths
weights = np.array([i[2]['weight'] for i in D.edges(data=True)])

# Prepare label dictionary (has form {node:label})
label_dict = {}
for i in range(adj_mat.shape[0]):
    label_dict[i] = samples[i].split()[0]

# Draw simple graph
nx.draw_networkx(D,pos=pos,width=weights*10,node_color=sample_colors,labels=label_dict)
plt.show()


### Draw fancy graph

# Set figure size (affects resolution)
fig = plt.figure(figsize=(12.0,12.0))

# Set background black
fig.patch.set_facecolor('black')
fig.gca().set_axis_bgcolor('black')

# Draw edges with width and colors sensibly coded by weights
# Note: width only scales properly for use_tfidf==False and use_wiki==False...
egs = nx.draw_networkx_edges(D,pos,width=weights*10,edge_color=np.log(weights),
                       edge_cmap=plt.cm.magma)

# Draw nodes              
nds = nx.draw_networkx_nodes(D,pos,linewidths=4.0,cmap=plt.get_cmap('Reds'),
                             vmin=-2,vmax=5,node_color='k', node_size=400)

# Adjust node edges with proper colors
nds.set_edgecolors(plt.cm.seismic(sample_colors))

# Add the labels
nx.draw_networkx_labels(D,pos,labels=label_dict,font_size=10,
                        font_color='w',font_weight='bold')

# Adjust display settings
plt.axis('off')
plt.gca().set_aspect('equal')
plt.tight_layout()

# Save and show graph
#plt.savefig('graph_figure.png',dpi=100,facecolor='k')
plt.show()


#------------------------------------------------------------------------------


