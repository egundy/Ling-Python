import nltk
from nltk.tokenize import word_tokenize
from nltk.tree import *
import nltk.draw
import re
import nltk.draw.tree


def generate_tree_diagram1(sentence):    # Function to generate a tree diagram using nltk
    grammar = grammar = nltk.CFG.fromstring(r"""
S -> NP VP
NP -> ProperNoun
VP -> Verb NP
ProperNoun -> "John" | "Mary" | "him"
Verb -> "believes" | "loves"
NP -> "that" NP
""")
    sentence = sentence.replace(".", "")    # Remove the period
    tokens = word_tokenize(sentence)    # Tokenize the sentence
    print(tokens)    # Print the tokens
    parser = nltk.ChartParser(grammar)    # Create a parser
    for tree in parser.parse(tokens):    # For each tree in the parser
        print(tree)    # Print the tree
        tree.draw()    # Draw the tree
generate_tree_diagram1("John believes Mary loves him.")