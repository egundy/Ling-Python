from clean_text import clean_and_tokenize_text
from word_frequency_dist import create_freq_dist, plot_freq_dist
from open_file import open_file
from nltk.tokenize import word_tokenize

def main():
    text = open_file('alice.txt')
    frequency_distribution = create_freq_dist(clean_and_tokenize_text(text))
    print(frequency_distribution)

if __name__ == '__main__':
    main()