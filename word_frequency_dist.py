# module to create a frequency distribution of words in a text and plot the results
# import the necessary modules
import nltk
import matplotlib.pyplot as plt
import numpy as np
import re

# define a function to create a frequency distribution in reverse order
def create_freq_dist(text):
    # create a frequency distribution
    freq_dist = nltk.FreqDist(text)
    # sort the frequency distribution in reverse order
    sorted_freq_dist = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq_dist

# define a function to plot the frequency distribution
def plot_freq_dist(freq_dist):
    # create a list of the frequencies
    freqs = [freq for (word, freq) in freq_dist]
    # create a list of the words
    words = [word for (word, freq) in freq_dist]
    # create a numpy array of the frequencies
    freqs = np.array(freqs)
    # create a numpy array of the words
    words = np.array(words)
    # create a numpy array of the cumulative frequencies
    cum_freqs = np.cumsum(freqs)
    # plot the cumulative frequencies
    plt.plot(cum_freqs)
    # plot the frequencies
    plt.plot(freqs)
    # plot the words
    plt.plot(words)
    # show the plot
    plt.show()

