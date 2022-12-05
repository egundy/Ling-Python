# module to clean and tokenize text of a given file
import re
from nltk.tokenize import word_tokenize
def clean_and_tokenize_text(text):
    # remove all punctuation
    cleantext = re.sub(r'[^\w\s]', '', text)
    # remove all numbers
    cleantext = re.sub(r'\d+', '', cleantext)
    # tokenize the text
    tokenized_text = word_tokenize(cleantext)
    return tokenized_text