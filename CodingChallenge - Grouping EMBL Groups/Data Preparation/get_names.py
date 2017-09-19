# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:14:42 2016

@author:    Jonas Hartmann @ Gilmour group @ EMBL Heidelberg

@descript:  Quick & dirty script to get all EMBL group leader names ordered by
            unit (director's research not included).
"""

# Get HTML from faculty webpage
import urllib2
page = urllib2.urlopen("https://www.embl.de/research/faculty/")

# Get out the 'alt' descriptions of the images (i.e. the group leader names)
from bs4 import BeautifulSoup
soup  = BeautifulSoup(page)
imgs  = soup.find_all('img')
alts  = [img.get('alt') for img in imgs]
print alts

# Note: The output from the above had to be manually curated in order to add 
#       the unit information and to make the names consistent with how they 
#       appear in the URLs of the group descriptions.
#       Manual curation resulted in this dict:
groupdict = {'CBB':['Jan Ellenberg', 'Alba Diz-Munoz', 'Darren Gilmour', 
                   'Christian Haering', 'Lars Hufnagel', 'Martin Jechlinger', 
                   'Peter Lenart', 'Francois Nedelec', 'Pierre Neveu', 
                   'Rainer Pepperkok', 'Robert Prevedel', 'Jonas Ries', 
                   'Carsten Schultz', 'Yannick Schwab'], 
            'DB': ['Anne Ephrussi', 'Detlev Arendt', 'Alexander Aulehla', 
                   'Stefano De_Renzis', 'Marcus Heisler', 'Takashi Hiiragi', 
                   'Francesca Peri'],
            'GB': ['Eileen Furlong', 'Wolfgang Huber', 'Jan Korbel', 
                   'Christoph Merten', 'Kyung-Min Noh', 'Mikhail Savitski', 
                   'Lars Steinmetz', 'Nassos Typas'],
            'SCB':['Peer Bork', 'Christoph Mueller_christoph', 
                   'Theodore Alexandrov', 'Orsolya Barabas', 'Martin Beck', 
                   'John Briggs', 'Anne-Claude Gavin', 'Toby Gibson', 
                   'Janosch Hennig', 'Edward Lemke', 'Kiran Patil', 
                   'Carsten Sachse', 'Judith Zaugg', 'Georg Zeller']}

# The dict is nice, but a list of tuples is more simple
grouplist = []
for unit in groupdict.keys():
    for name in groupdict[unit]:
        grouplist.append((name,unit))
        
# Save grouplist to txt
with open("faculty_list.txt","w") as outfile:
    for name,unit in grouplist:
        outfile.write(name+'\t'+unit+'\n')

