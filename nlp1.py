# imports for the script
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer, PunktSentenceTokenizer
from nltk.corpus import webtext, stopwords
import nltk.data
import re

text = webtext.raw('overheard.txt')

sent_tokenizer = PunktSentenceTokenizer(text)

sents_list_1 = sent_tokenizer.tokenize(text)

sents_list_2 = sent_tokenize(text)

print(sents_list_1[0])
print(sents_list_1[678])
print("\n\n\n")
print(sents_list_2[0])
print(sents_list_2[678])