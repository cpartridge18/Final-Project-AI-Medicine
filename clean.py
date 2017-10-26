#Cleaning program

#read data
import pandas as pd       
train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)

#relic of the movie review thing, rev is the number review to read
rev = 32

# Import BeautifulSoup
from bs4 import BeautifulSoup             
import re

# Initialize the BeautifulSoup object on a single movie review     
example1 = BeautifulSoup(train["review"][rev], "html5lib")  

# Method to give a list of all the words in the comparison string
def just_words(input):
	letters_only = re.sub("[^a-zA-Z]",   # The pattern to search for
                      " ",               # The pattern to replace it with
                      input)             # The text to search
	lower_case = letters_only.lower()    # Convert to lower case
	words = lower_case.split()           # Split into words
	return words

# Just the words from the input
in_words = just_words(example1.get_text())
#print(words)

# Get stopwords
import nltk
from nltk.corpus import stopwords # Import the stop word list
#print(str(stopwords.words("english")))

# Create new list of input words without stopwords using list comprehension
trim = [w for w in in_words if w not in set(stopwords.words("english"))]
#print (trim)

# Import collections to count the number of duplicates
import collections
count = collections.Counter(trim)
#print (count)

# Method taking two input lists giving a dictionary of the first list and a 1 or 0 depending on if the word appears in the second list
def match(list, comp_list):
    D = {}
    for w in trim:
        if w in comp_words:
            D[w]=1
        else:
            D[w]=0

    return(D)

# Comparison Text
comp = "faithful adaptation, humerous, this is the best, down with the bourgeois"
comp_words = just_words(comp)

# Dictionary with input compared to comparison list with 1's and 0's
comp = match(trim, comp_words)
print(comp)

# Print just the 1's and 0's
print(list(comp.values()))

# Counter of similarites 
counter=collections.Counter(list(comp.values()))
print(counter.values())
sim = float(counter[1]/(counter[0]+counter[1]))   #percent of words that appeared in the compared text
print("Percent Similarity: " + str(sim))