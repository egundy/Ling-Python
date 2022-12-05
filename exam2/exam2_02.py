""" 
Clean the text and create a combined PDF of all the PDFs in the directory; then, create 
a frequency list (starting with the most frequently used word) for the combined PDF and save it 
as a json file. You should exclude stopwords for your frequency lists. 
"""

# Import modules
import re
import os
import PyPDF2 as pypdf
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define functions
# Function to merge PDFs in directory
def merge_pdfs():
    """ 
    Merge PDFs in directory. 
    """
    pdf_writer = pypdf.PdfFileWriter()
    for filename in os.listdir():
        if filename.endswith('.pdf'):
            pdf_reader = pypdf.PdfFileReader(filename)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
    with open('combined_pdf.pdf', 'wb') as file:
        pdf_writer.write(file)

# Function to open combined PDF and return text
def pdf_to_text(pdf):
    with open(pdf, 'rb') as file:
        pdf_reader = pypdf.PdfFileReader(file)
        text = ''
        for page in range(pdf_reader.getNumPages()):
            text += pdf_reader.getPage(page).extractText()
        return text
    
    # Function to clean text
def clean_text(text):
    """ 
    Clean text by removing non-alphanumeric characters and converting text to lowercase. 
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = text
    return cleaned_text

# Remove stopwords
def remove_stopwords(clean_text):
    """ 
    Remove stopwords from text. 
    """
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(clean_text)
    filtered_text = [w for w in word_tokens if not w in stop_words]
    return filtered_text

# Create frequency list in descending order
def create_freq_list(filtered_text):
    """ 
    Create a frequency list of words in the text. 
    """
    freq_list = {}
    for word in filtered_text:
        if word in freq_list:
            freq_list[word] += 1
        else:
            freq_list[word] = 1
    sorted_freq_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq_list

# Output frequency list as json file with new line for each word
def output_json(sorted_freq_list):
    """ 
    Output frequency list as json file with new line for each word. 
    """
    with open('freq_list.json', 'w', encoding="UTF-8") as file:
        json.dump(sorted_freq_list, file, indent=2)
        
# Main function to call other functions
def main():
    merge_pdfs()
    text = pdf_to_text('combined_pdf.pdf')
    cleaned_text = clean_text(text)
    filtered_text = remove_stopwords(cleaned_text)
    sorted_freq_list = create_freq_list(filtered_text)
    output_json(sorted_freq_list)
    
if __name__ == '__main__':
    main()