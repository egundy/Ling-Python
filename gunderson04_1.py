import re
import operator
import sys

with open('prideprej.txt') as file_in:
    clean_text = re.sub(r'[^\w\s\_',file_in)
    clean_text_new = re.sub(r'\_','', clean_text)
    word_list = clean_text_new.lower().split()
