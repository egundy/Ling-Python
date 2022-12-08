'''
Examine my script for the interrogative conversion. Some blocks of the code are very similar, 
containing repetitive operations. In every step, you make a replacement in the sentence and then 
re-tokenize it. This type of code is wasteful and unclean. 
Your job is to generalize the code, putting repetitive operations in a single function. In doing so, 
you will need to explicitly specify what you are searching for and what operations you want to 
perform on it by either replacing it with another token or adding a token before it.
'''

# imports
import spacy

# set up spaCy
# set nlp to the English model
nlp = spacy.load('en_core_web_sm')
# set doc to the nlp object of the sentence