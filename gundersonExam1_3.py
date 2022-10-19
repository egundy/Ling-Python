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
text = readfile(argv[1]) #reads file and makes it a list of strings

#cleaning the text
cleantext = re.sub(r'[^\w\d\s\']+', '', text)
cleantext = cleantext.lower().split()#making text lower case to ignore capitalization while checking correct spelling and makes it a list

#check words in text are in wordlist
misspelled_words = []
for word in cleantext:
    if word in wordlist:
        continue
    else:
        misspelled_words.append(word)

print("The incorrect words in your text are:", misspelled_words)