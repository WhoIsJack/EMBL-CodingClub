# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:14:42 2016

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  Quick & dirty script to extract a "cleaned" set of words from the
            group description website of each EMBL Heidelberg group.
            
@WARNING:   I am by no means an expert on text retrieval and processing, so the 
            following should not be viewed as an example of how to ideally 
            approach such a task!
"""


# PREP

# Imports
import nltk
from nltk.corpus import stopwords
import string
import urllib2
import codecs
from bs4 import BeautifulSoup


#------------------------------------------------------------------------------

# FUNCTIONS

# Function to get word list from webpage
def get_words(url):
    
    # Get the HTML
    page = urllib2.urlopen(url)
    #print page
    
    # Parse out the text
    soup  = BeautifulSoup(page)
    body  = soup.find_all('p')    # For all paragraphs
    text  = ' '.join([paragraph.get_text() for paragraph in body])
    #print text
    
    # Force-convert unicode to ascii to avoid problems later...
    text = codecs.unicode_escape_encode(text)[0]
    #print type(text)
    
    # Tokenize
    tokens = nltk.word_tokenize(text)
    #for token in tokens: print token
    
    # Done!
    return text, tokens
    

# Function to clean up a list of words
def clean_words(wordlist):
    
    # Remove punctuation
    wordlist = [w for w in wordlist if w not in string.punctuation]
    
    # Get rid of strings smaller than 3 characters
    wordlist = [w for w in wordlist if len(w) >= 3]    
    
    # Normalize to lower case
    wordlist = [w.lower() for w in wordlist]
    
    # Remove "stop words", i.e. trivial words
    wordlist = [w for w in wordlist if w not in stopwords.words('english')]    
    
    # Lemmatize; bring the words to their base form
    wnl = nltk.WordNetLemmatizer()
    wordlist = [wnl.lemmatize(w) for w in wordlist]
    
    # Remove numbers
    newlist = []
    for i,w in enumerate(wordlist):
        try:
            float(w)
        except Exception:
            newlist.append(w)
    wordlist = newlist[:]
    
    # Remove some remaining useless things explicitly
    unwanted = ["figure","al.","project","also","science","study"]
    wordlist = [w for w in wordlist if w not in unwanted]
    
    # Sort the list
    wordlist = sorted(wordlist)

    # Done!
    return wordlist    


#------------------------------------------------------------------------------

# MAIN SCRIPT

# Protected so the functions above can be used by other scripts
if __name__ == '__main__':
    
    
    # Import group names
    with open("faculty_list.txt","r") as infile:
        
        # For each line...
        grouplist = []
        for line in infile:
            
            # Clean, split, then rejoin the name
            line = line.strip()
            line = line.split()
            name = ' '.join(line[:-1])
            
            # Add to grouplist
            grouplist.append([name,line[-1]])
    
    
    # For each group, retrieve the data:
    texts_dict = {}
    words_dict = {}    
    for name,unit in grouplist:
              
        # Get name used in url
        if unit == 'CBB':
            unit_name = 'cbb'
        elif unit == 'DB':
            unit_name = 'dev_biology'
        elif unit == 'GB':
            unit_name = 'genome_biology'
        elif unit == 'SCB':
            unit_name = 'scb'
        
        # Construct url
        url = r"https://intranet.embl.de/research/"+unit_name+r"/"+name.split()[1].lower()+r"/index.html"
        
        # Try to get the words
        try:
            text,tokens = get_words(url)
        except Exception:
            print "Didn't work for", name, '('+unit+')'
            continue
    
        # Clean up the words
        tokens = clean_words(tokens)
    
        # Append to complete data dict
        texts_dict[name] = text
        words_dict[name] = tokens
        
        # Report progress
        print "Words retrieved for", name, '('+unit+')'
    
    
    # Save texts to txt
    with open('embl_group_texts.txt','w') as outfile:
        for name in texts_dict.keys():
            outfile.write('### '+name+'\n')
            outfile.write(texts_dict[name])
            outfile.write('\n\n')

    # Save words to txt
    with open('embl_group_words.txt','w') as outfile:
        for name in words_dict.keys():
            outfile.write('### '+name+'\n')
            for word in words_dict[name]:
                outfile.write((word+', '))
            outfile.write('\n\n')
 
    # Save texts to json
    import json
    with open('embl_group_texts.json', 'w') as outfile:
        json.dump(texts_dict, outfile)
    
    # Save words to json
    with open('embl_group_words.json', 'w') as outfile:
        json.dump(words_dict, outfile)


#------------------------------------------------------------------------------



