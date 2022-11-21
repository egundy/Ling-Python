"""Finish the in-class project. I will summarize the steps you have to follow here again. 
• Combine all pdf files in the current directly (Park&Turner.pdf and Park&Park.pdf).
• Convert it to a text file.
• Clean up the text; remove all punctuations and numbers.
• From the cleaned text, generate a frequency list (reverse order) using a dictionary 
structure and save it as a text file. Note that you should use the operator module to create 
the frequency list, which will result in a list of tuples. 
• Save the list of tuples as it is, using the json module. Note that json does not have a tuple 
data structure, and the saved output is in the form of a list of lists.   
• In doing so, your script should take two command line arguments: output1.txt and 
output2.json """

import json
import operator
import os
import re
import sys
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader

# Combine all pdf files in the current directory
def combine_pdf():
    merger = PdfFileMerger()
    for file in os.listdir():
        if file.endswith(".pdf"):
            merger.append(file)
    merger.write("combined.pdf")
    merger.close()

# Convert PDF to text
def convert_to_txt():
    with open("combined.pdf", "rb") as f:
        pdf = PdfFileReader(f)
        text = ""
        for page in pdf.pages:
            text += page.extractText()
    with open("combined.txt", "w") as f:
        f.write(text)

# Clean up the text; remove all punctuations and numbers
def clean_up():
    with open("combined.txt", "r") as f:
        text = f.read()
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        text = re.sub(r"\d+", "", text)
        text = re.sub(r"\t+", "", text)
        text = text.lower()
    with open("combined.txt", "w") as f:
        f.write(text)

# From the cleaned text, generate a frequency list (reverse order) using a dictionary structure and save it as a text file
# Note that you should use the operator module to create the frequency list, which will result in a list of tuples
def generate_frequency_list():
    with open("combined.txt", "r") as f:
        text = f.read()
        words = text.split()
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        word_dict_sorted = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
        # write word_dict_sorted tuples to a text file in reverse order with a colon separating the word and the count
        with open(sys.argv[1], "w") as f:
            for word, count in word_dict_sorted:
                f.write(f"{word}:{count}\n")
    return word_dict_sorted # return the list of tuples

# Save the list of tuples as it is, using the json module
def save_as_json():
    sorted_word_dict = generate_frequency_list()
    with open(sys.argv[2], "w") as f:
        json.dump(sorted_word_dict, f)

# main function
if __name__ == "__main__":
    combine_pdf()
    convert_to_txt()
    clean_up()
    save_as_json()