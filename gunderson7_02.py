from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import sys
import re

def get_text(variable_url):
    base_url = 'https://en.wikipedia.org/wiki/'
    combined_url = base_url + variable_url
    source = urlopen(combined_url)
    soup = bs(source, 'lxml')
    soup

    paragraphs = []
    for paragraph in soup.find_all('p'):
        paragraphs.append(str(paragraph.text))

    headers = []
    for head in soup.find_all("span", attrs={"mw-headline"}):
        headers.append(str(head.text))

    text = [val for pair in zip(paragraphs,headers) for val in pair]
    text = ' '.join(text)

    text = re.sub(r"\[.*?\]+", '' , text)
    text = text.replace('\n', '')[:-11]
    return text

def each_link():
    alltext = []
    for i in sys.argv[2:]:
        text = get_text[i]
        alltext.append(text)
    return alltext

def output_to_txt(words):
    with open("wiki_output.txt","a") as f:
        f.write(words)
    
def main():
    alltext = each_link()
    words = {}
    freq = 0
    for j in alltext:
        if j not in alltext:
            words.update({"word" : freq})
        if j in alltext:
            freq += 1
            words.update({j : freq})
    output_to_txt(words)