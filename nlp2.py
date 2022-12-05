"""generate frequency distribution of words without stop words in a text file"""
# imports for the script
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re


# function to open the file and read the contents
def open_file():
    # read in the file
    with open('prideprej.txt', 'r') as f:
        text = f.read()
    # clean the text
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # tokenize the text
    text = text.lower()
    words = word_tokenize(text)
    return words

# filter out stop words
def filter_stop_words(words):
    # get the stop words
    stop_words = set(stopwords.words('english'))
    # filter out the stop words
    filtered_words = [w for w in words if not w in stop_words]
    return filtered_words

# generate the frequency distribution in a python dictionary
def freq_dist(filtered_words):
    # generate the frequency distribution
    freq_dist = {}
    for w in filtered_words:
        if w in freq_dist:
            freq_dist[w] += 1
        else:
            freq_dist[w] = 1
    return freq_dist

# sort the frequency distribution in descending order
def sort_freq_dist(frequency_dist):
    # sort the frequency distribution in descending order
    sorted_freq_dist = sorted(frequency_dist.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq_dist

# output to file with the frequency distribution separated by a colon
def output_to_file(sorted_freq_dist):
    with open('freq_dist.txt', 'w') as f:
        for item in sorted_freq_dist:
            f.write(f"{item[0]}:{item[1]}\n")

# main function to call the other functions
def main():
    words = open_file()
    filtered_words = filter_stop_words(words)
    dist = freq_dist(filtered_words)
    sorted_frequency_dist = sort_freq_dist(dist)
    output_to_file(sorted_frequency_dist)
    
    
if __name__ == '__main__':
    main()