# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:14:42 2016

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  In order to get a bit more information about each group, we can
            run the important words used through wikipedia and get more words
            out of the summary.
            In a first try, I focused on the words unique to the group, to
            prevent the groups from becoming too homogeneous.
"""


# PREP

# Imports
import wikipedia
import nltk
import numpy as np
import codecs


#------------------------------------------------------------------------------

# FUNCTIONS

# Function to get words from wikipedia
def get_wiki_words(searchterm):
    
    # Get the summary of the wiki article
    text = wikipedia.summary(searchterm)
    
    # Tokenize
    tokens = nltk.word_tokenize(text)
    #for token in tokens: print token 
    
    # Done
    return tokens


#------------------------------------------------------------------------------

# MAIN SCRIPT

# Protected so the functions above can be used by other scripts
if __name__ == '__main__':

    # Prep
    from extract_words import clean_words

    # Loading the data
    import json
    with open('embl_group_words.json', 'r') as fp:
        words_dict = json.load(fp)
    
    # Create flat array of words that are unique across all groups
    words_flat = np.array([word for name in words_dict.keys() for word in words_dict[name]])
    words_unique,wordcounts = np.unique(words_flat,return_counts=True)
    words_unique = words_unique[wordcounts==1]
    
    # For every group...
    for group_number,name in enumerate(words_dict.keys()):
     
        # For every word...
        all_new_words = []
        for word in words_dict[name]:
            
            # Skip if the word is not unique
            if word not in words_unique:
                continue
        
            # Retrieve more words from wikipedia
            try:
                more_words = get_wiki_words(word)
                print "Retrieval successful for", word
            except Exception:
                print "Retrieval failed for", word
                continue
            
            # Get rid of unicode issues
            more_words = [codecs.unicode_escape_encode(w)[0] for w in more_words]
            
            # Clean new words by means of clean_words() from extract_words.py
            more_words = clean_words(more_words)
            
            # Keep the words
            all_new_words = all_new_words + more_words
            
        # Add new words to the words_dict  
        words_dict[name] = sorted(words_dict[name] + all_new_words)
        
        # Report
        print "### RETRIEVAL COMPLETE FOR GROUP", group_number+1, 'OF', len(words_dict), '('+name+')\n'

    # Save the result as json
    with open('embl_group_words_wiki.json', 'w') as fp:
        json.dump(words_dict, fp)
            
    # Save the result as txt
    with open('embl_group_words_wiki.txt','w') as outfile:
        for name in words_dict.keys():
            outfile.write('### '+name+'\n')
            for word in words_dict[name]:
                outfile.write((word+', '))
            outfile.write('\n\n')    
        

#------------------------------------------------------------------------------



