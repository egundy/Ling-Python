'''Write a program that reads a file and displays all of the words in that are misspelled. Misspelled words 
will be identified by checking each word in the file against a list of known words. Any words in the user’s 
file that do not appear in the list of known words will be reported as spelling mistakes. The user will 
provide the name of the file to check for spelling mistakes as a command line parameter. Beware that 
words followed by a comma, period, or other punctuation mark should not be reported as spelling 
mistakes. To do so, you should use the solution to Question 2. Ignore the capitalization of the words when 
checking their spelling. For this question, you need to import the nltk module. Do the following. Then, 
you will see the list of English words in word_list. '''

#imports
import re #for cleaning text
from sys import argv #for user input
from nltk.corpus import words #for checking spelling

#get list of correctly spelled words
wordlist = words.words()

#function to read in file as text
def readfile(filename):
    with open(filename,'r') as file_in:
        text = file_in.read()
    return text
text = readfile('alice.txt')#argv[1]) #reads file and makes it a list of strings

#cleaning the text
cleantext = re.sub(r'[^\w\s]', ' ', text)
cleantext = cleantext.lower().split()#makes it a list
cleantext = set(cleantext) #change to set for speed purposes
#check words in text are in wordlist
misspelled_words = []
for word in cleantext:
    if word in wordlist:
        continue
    else:
        misspelled_words.append(word)

print("The incorrect words in your text are:", misspelled_words)