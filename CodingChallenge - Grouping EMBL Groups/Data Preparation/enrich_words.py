# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:14:42 2016

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  Enrich the extracted (and expanded) words by adding the tf-idf
            (the "term frequency - inverse document frequency", see
            https://en.wikipedia.org/wiki/Tf-idf). This allows us assign 
            weights when we use the words as features for clustering in the 
            next step.
"""

# PREP

# Imports
from __future__ import division
import numpy as np


#------------------------------------------------------------------------------

# FUNCTIONS

# Function to compute the IDF of a word
def get_idf(word,words_dict):
    
    # Count the number of 'documents' containing the word
    nr_of_positive = 0
    for name in words_dict.keys():
        if word in words_dict[name]:
            nr_of_positive += 1
    
    # Compute IDF in its simplest form
    idf = np.log(len(words_dict) / nr_of_positive)
    
    # Done!
    return idf
    

# Function to compute the TF-IDF of a text in a doc, given the IDF is known
def get_tf_idf(word,document,idf):
    
    # Count the number of occurrences of the tf in the document
    word_count = document.count(word)
    
    # Compute simplest version of tf
    tf = word_count / len(document)
    
    # Compute tf-idf
    tf_idf = tf * idf
    
    # Done!
    return tf_idf
    

#------------------------------------------------------------------------------

# SCRIPT

# MAIN SCRIPT

# Protected so the functions above can be used by other scripts
if __name__ == '__main__':
    
    # Loading the data
    #inName = 'embl_group_words_wiki'      # With wiki expansion
    inName = 'embl_group_words'            # Without wiki expansion
    import json
    with open(inName+'.json', 'r') as fp:
        words_dict = json.load(fp)
        
    # Computing the IDF for all words
    unique_words = list(set([word for wordlist in words_dict.values() for word in wordlist])) # Create list of unique words
    all_idf = [get_idf(w,words_dict) for w in unique_words]
    
    # Computing the tf-idf (for every word in every group...)
    tf_idf_dict = {}
    for group_index,name in enumerate(words_dict.keys()):
        
        # For every unique (!) word in the current group...
        all_tf_idf = []
        for word in set(words_dict[name]):
            
            # Compute the tf-idf
            tf_idf = get_tf_idf(word,words_dict[name],all_idf[unique_words.index(word)])
            all_tf_idf.append([word,tf_idf])
        
        # Append to the result dict
        tf_idf_dict[name] = all_tf_idf
        
        # Report
        print "Done for group", group_index+1, "of", len(words_dict.keys()), '('+name+')'
    
    # Save the result to json
    with open(inName+'_tfidf.json', 'w') as fp:    
        json.dump(tf_idf_dict, fp)
    
    # Save the result as txt
    with open(inName+'_tfidf.txt', 'w') as outfile:
        for key in tf_idf_dict.keys():
            outfile.write('### '+key+'\n')
            for word in tf_idf_dict[key]:
                outstring = (word[0] + ', ' + str(word[1]) + '\n')
                outfile.write(outstring)
            outfile.write('\n\n')


#------------------------------------------------------------------------------



