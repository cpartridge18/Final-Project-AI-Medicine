#Cleaning program

#read data
import pandas as pd       
train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)

#relic of the movie review thing, rev is the number review to read
rev = 70

# Import BeautifulSoup
from bs4 import BeautifulSoup             
import re

# Initialize the BeautifulSoup object on a single movie review     
example1 = BeautifulSoup(train["review"][rev], "html5lib")  

# Use regular expressions to do a find-and-replace
letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                      " ",                   # The pattern to replace it with
                      example1.get_text() )  # The text to search
print(letters_only)

lower_case = letters_only.lower()        # Convert to lower case
words = lower_case.split()               # Split into words
print(words)

#get stopwords
import nltk
from nltk.corpus import stopwords # Import the stop word list
print(str(stopwords.words("english")))

#create new list of words without stopwords using list comprehension
trim = [w for w in words if w not in set(stopwords.words("english"))]
print (trim)

#add something to count the number of duplicates
import collections
count = collections.Counter(trim)
print (count)

#List of all the words in the comparison string
comp_input = "" #comparison string
comp_letters_only = re.sub("[^a-zA-Z]",      # The pattern to search for
                      " ",                   # The pattern to replace it with
                      comp_input)            # The text to search
comp_lower_case = comp_letters_only.lower()        # Convert to lower case
comp_words = comp_lower_case.split()               # Split into words
print(comp_words)

#method taking two input lists giving a list of the first list and a 1 or 0 depending on if the second word appears
def match(list, comp_list):
    D = {}
    for w in trim:
        if w in comp_words:
            D[w]=1
        else:
            D[w]=0

    return(D)
print(match(trim, comp_words))

#print just the 1's and 0's
print(list(match(trim, comp_words).values()))

counter=collections.Counter(list(match(trim, comp_words).values()))
print(counter.values())
sim = float(counter[1]/(counter[0]+counter[1]))   #percent of words that appeared in the compared text
print(sim)