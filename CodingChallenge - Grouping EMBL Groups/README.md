*EMBL Coding Club Advent Challenge, December 2016*    
*(Hastily) put together by Jonas Hartmann, Gilmour group, CBB*    
*Later somewhat cleaned and improved by Jonas Hartmann*

## Restructuring EMBL based on SCIENCE!
**Congratulations!** You have been selected to follow in the footsteps of Iain Mattaj as the new *Director General* of EMBL. On your first day in office, you feel that you have to find the answer to one key question: *How can I imprint my mark on EMBL forever?* Fortunately, you already have a great idea: you could completely restructure the units, clustering the different research groups based on *scientific data (yay!)* rather than *hiring politics (boo!)*.

### Task
In this repository, you'll find the descriptions of all the groups currently working at EMBL Heidelberg, mined from the EMBL website. Your task is to use this data to determine a scientific measure of "similarity" between the groups, based on which you can cluster them into a new unit structure.

### Data
- **faculty_list.txt --**  names of faculty members and their unit association
- **embl_group_texts.txt --** raw text of group descriptions
- **embl_group_words.txt --** extracted and cleaned words from the raw text.     
  **IT IS RECOMMENDED THAT YOU START WITH THIS AS YOUR INPUT DATA!**
- **embl_group_words_wiki.txt --** extracted and cleaned words from raw text, expanded with similar words based on wikipedia.
- **embl_group_words_tfidf.txt --** extracted and cleaned words from raw text, but including a measure of "word relevance" for each word, the TF-IDF.
- **embl_group_words_wiki_tfidf.txt --** extracted, cleaned and wiki-expanded words with TF-IDF.

### Scripts
If you are curious about how I produced the input data, you can have a look at these python scripts:
- **get_names.py --** Quick & dirty script to get the names of all the group leaders from the web. This script is only semi-automatic; it requires a manual curation step.
- **extract_words.py --** Quick & dirty script for extracting the texts from the web and cleaning them up.
- **enrich_words.py --** Quick & dirty script to compute the TF-IDF measure for each word.
- **expand_words.py --** Quick & dirty script to expand the word list using wikipedia.

** IMPORTANT NOTE:** I am not very experienced with retrieving text data from the web or performing computer-linguistic clean-up and so forth, so these scripts should ***not*** be seen as a gold standard reference for how to do such things!

***Good luck - the future of EMBL's excellence in research depends on you!***

### UPDATE: Example Solution
After playing around a bit myself, I have added an example solution that showcases some of the techniques and methods one could use to address this challenge. I ultimately couldn't come up with a good solution for how to restructure the units, though; according to my analysis, the data does not naturally cluster into groups. If anything, I would thus propose to reorganize EMBL with some sort of continuum model rather than with discrete units! ;p

Here's what my analysis produced:
- **example_solution.py --** the python script that shows the things I've tried. It's relatively elaborate, so it may be easier to first look at the 'SIMPLE' version if you'd like to understand the general approach I've taken.
- **example_solution_SIMPLE.py --** slightly pruned/simplified version of the full example_solution script.
- **graph_figure.png --** the ultimate output of my analysis; a similarity graph between EMBL groups, organized by force-directed clustering. It indicates that there are not clusters ("units"), but there is a continuum along an axis that is defined by SCB/GB vs. CBB/DB, with some groups being closer to the interface of these domains and some groups being further away. Proposing a well-functioning organization structure for EMBL based on this result would probably not be easy...

** IMPORTANT NOTE:** There is no "right" solution to this challenge - what I've posted here simply shows how I would address the challenge in a first instance. It serves as an inspiration more so than a solution to the challenge or a guide on data analysis. ***Please feel free to give it a try yourself and please let me know if you come up with a different solution!***








