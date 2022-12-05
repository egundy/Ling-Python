"""Write a program that takes the name of a Wikipedia page as an argument, looks at the textual 
information of their Wikipedia page, and returns a frequency list (starting with the most 
frequent) for any years that appear on the Wikipedia pages. Assume that a year will be four 
characters long."""

# imports for the script
import re
from urllib.request import urlopen
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup as bs
import json

# function to open a wikipedia page and read the contents using beautiful soup and return words
def open_wiki_page(page):
    # read in the file
    try:
        with urlopen(f'https://en.wikipedia.org/wiki/{page}') as f:
            html = f.read()
    except:
        raise Exception('Page not found')
    soup = bs(html, 'html.parser')
    text = soup.get_text()
    # clean the text
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # tokenize the text
    text = text.lower()
    words = word_tokenize(text)
    return words

# function to find the years in the text and return a frequency distribution of the years starting with the most frequent
def find_years(words):
    # find the years in the text
    years = []
    for w in words:
        if len(w) == 4 and w.isdigit() and int(w) <= 2022:
            years.append(w)
    # generate the frequency distribution
    freq_dist = {}
    for w in years:
        if w in freq_dist:
            freq_dist[w] += 1
        else:
            freq_dist[w] = 1
    # sort the frequency distribution in descending order
    sorted_freq_dist = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq_dist

# function to output to file with the name of the page, as a txt file, wiith new lines between each year and frequency
def output_to_file(sorted_freq_dist, page):
    with open(f'{page}_freq_dist.txt', 'w') as f:
        for item in sorted_freq_dist:
            f.write(f"{item[0]}:{item[1]}\n")

# main function to call the other functions
def main():
    page = input('Enter the name of a Wikipedia page: ')
    words = open_wiki_page(page)
    sorted_frequency_dist = find_years(words)
    output_to_file(sorted_frequency_dist, page)
    
if __name__ == '__main__':
    main()