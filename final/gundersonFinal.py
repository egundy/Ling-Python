"""
Code for the final exam by Evan Gunderson.
This code should be able to run correctly from the terminal with user input. *Must be run in Python 3.10 or higher*
Every task will be addressed in this program and will be identified by a triple quote comment.
To use this program, type the following in the terminal: python3.1x gundersonFinal.py
"""

# Imports
import re 
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk.draw
from nltk import CFG
from nltk.parse import RecursiveDescentParser
from nltk.tree import *
import spacy
from spacy import displacy
import json
import PyPDF2
import numpy as np
import concurrent.futures
import requests
from bs4 import BeautifulSoup

# Global variables
nlp = spacy.load("en_core_web_sm")   # Load the English language model

def menu(): # define the function to display the menu
    print("""
=====================================================
| 1. Capitalize a sentence correctly                |   # complete; runs
| 2. Identify if a string is a palindrome           |   # complete; runs
| 3. Generate a freq. list of words in a PDF        |   # complete; runs
| 4. Pride and Prejudice similies                   |   # incomplete; does not run
| 5. People form Linguistics Wikipedia page         |   # incomplete; runs
| 6. Use spaCy to find 78th sentence of wiki page   |   # incomplete; does not run
| 7. Generate tree diagram of a sentence            |   # incomplete; does not run
| 8. Chunk all NPs, PPs, and VPs from a sentence    |   # incomplete; does not run
|                                                   |
| *Type 'q' to quit*                                |
=====================================================""")

""" functions that are used in multiple tasks """
def repeat_task(task): # function to repeat a task
    print("\nThank you for using this program! Would you like to run it again? (y/n) \n")
    again = input("Enter your selection: ")
    if again == 'y':
        print("Thank you! Returning to the task...\n")
        return task()
    elif again == 'n':
            print("Thank you! Returning to the main menu...\n")
    else:
        print("You must enter a 'y' or an 'n'!")
        repeat_task(task)

def is_correct_task(task): # function to check if the user is on the correct task
    print("Is this the corect task? (y/n")
    correct_task = input("Enter your selection: ")
    if correct_task == 'y':
        print("Thank you! Now starting the task...")
        return task()
    elif correct_task == 'n':
        print("Thank you! Returning to the main menu...\n")
    else:
        print("You must enter a 'y' or an 'n'!")
        correct_task(task)

""" Task 1: Capitalize a sentence correctly"""
def capitalize(string): # function to capitalize the appropriate characters in a string
    string = string[0].upper() + string[1:]    # capitalize the first character in the string
    string = re.sub(r'([.!?]) ([a-z])', lambda x: x.group(1) + ' ' + x.group(2).upper(), string)    # Capitalize the first non-space character after a '.', '!' or '?'
    flag = True    # While loop flag
    while flag == True:    # While loop to capitalize the 'i' if it is both preceded and followed by a space
        search_for_i = re.search(r' ([i]) ', string)   # Search for the 'i' in the string
        if search_for_i:    # If the 'i' is found, capitalize it
            string = re.sub(r' ([i]) ', lambda x: ' ' + x.group(1).upper() + ' ', string)   # Capitalize the 'i' if it is both preceded and followed by a space
        else:   # If the 'i' is not found, set the flag to False
            flag = False    # Set the flag to False to exit the while loop
    return string    # Return the string

# execute the function with user input
def ui_capitalize():
    print("""
================================================================================================          
*** Welcome to the capitalizer! ***
This task correctly capitalize a sentece. 
================================================================================================
Is this the corect task? (y/n)""")
    correct_task = input("Enter your selection: ").lower()
    if correct_task == 'y':
        print("Thank you! Now starting the task...")
        # Get a string from the user
        string = input("Enter a string to capitalize: ")
        # Capitalize the string
        string = capitalize(string)
        # Display the string
        print(f"The correct capitalization of your sentence:\n{string}")
        print("\nThank you for using this program! Would you like to try another sentence? \n\
              Type 'y' for yes or 'n' for no and return to the menu.")
        user_input = input("Enter your selection: ")
        match user_input:
            case 'y':
                print("Thank you! Returning to the task...\n")
                ui_capitalize()
            case 'n':
                print("Thank you! Returning to the main menu...\n")  
            case _:
                # If the user does not enter a 'y' or an 'n', display an error message
                raise ValueError("You must enter a 'y' or an 'n'!")        
    elif correct_task == 'n':
        print("Thank you! Returning to the main menu...\n")
    else:
        print("You must enter a 'y' or an 'n'!")
        ui_capitalize()

""" Task 2: Identify if a string is a palindrome """
def is_palindrom(string): # function to identify if a string is a palindrome
    string = string.lower()    # Convert the string to lower case
    string = re.sub(r'[^a-z]', '', string)    # Remove all non-alphabetical characters
    if string == string[::-1]:    # If the string is equal to the reverse of the string, it is a palindrome
        return True    # Return True
    else:    # If the string is not equal to the reverse of the string, it is not a palindrome
        return False    # Return False
# Task 2 user interface
def ui_palindrome():
    # code for user interaction with the palindrome task
    print("""
================================================================================================          
*** Welcome to the palindrome identifier! ***
This task will identify if a string is a palindrome.
================================================================================================
Is this the corect task? Type 'y' for yes or 'n' for no and return to the menu.""")
    correct_task = input("Enter your selection: ").lower()  # Get the user's selection
    if correct_task == 'y': # If the user selects 'y', start the task
        print("Thank you! Now starting the task...")    # Display a message to the user
        string = input("Enter a string to check if it is a palindrome: ")   # Get a string from the user
        if is_palindrom(string):    # If the string is a palindrome, display a message to the user
            print(f"{string} is a palindrome!")   # Display a message to the user
            repeat_task(ui_palindrome)  
        else:   # If the string is not a palindrome, display a message to the user
            print(f"{string} is not a palindrome!")   # Display a message to the user
            repeat_task(ui_palindrome)  # Ask the user if they would like to try another string
    elif correct_task == 'n':   # If the user selects 'n', return to the main menu
        print("Thank you! Returning to the main menu...\n")   # Display a message to the user
    else:   # If the user does not enter a 'y' or an 'n', display an error message
        print("You must enter a 'y' or an 'n'!")    # Display an error message to the user
        ui_palindrome() # Return to the task

""" Task 3: Generate a reverse order freq. list of words in a PDF """
def read_pdf():  # Function to read a pdf file and extract the text
    # Open the pdf with PyPDF2 and read the text
    with open("Neg Inversions_2018.pdf", "rb") as pdf_file_in:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_in)
        # Get the number of pages in the pdf
        for page in range(pdf_reader.getNumPages()):
            # Get the text from each page
            page = pdf_reader.getPage(page)
            text = page.extractText()
    return text   # Return the text

def tokenize(text):   # Function to tokenize the text into words
    tokens = word_tokenize(text)   # Tokenize the text into words
    return tokens   # Return the tokens

def remove_stopwords(text):   # Function to remove stopwords from the text
    stops = stopwords.words('english')   # Define stopwords to remove from the list
    no_stops = [word for word in text if word not in stops]   # Remove stopwords from the text
    return no_stops   # Return the text without stopwords

# function that expands contractions in the text
def expand_contractions(text) -> list:   # Function to expand contractions
    # Define a dictionary of contractions to expand
    contractions = {  
        "ain't": "am not","aren't": "are not","can't": "cannot","can't've": "cannot have","'cause": "because",
        "could've": "could have","couldn't": "could not","couldn't've": "could not have","didn't": "did not",
        "doesn't": "does not","don't": "do not","hadn't": "had not","hadn't've": "had not have","hasn't": "has not",
        "haven't": "have not","he'd": "he had","he'd've": "he would have","he'll": "he shall","he'll've": "he shall have",
        "he's": "he has","how'd": "how did","how'd'y": "how do you","how'll": "how will",
        "how's": "how has","i'd": "I had","i'd've": "I would have"
    }
    text = [contractions[word] if word in contractions else word for word in text]   # Expand all contractions in the text
    return text
        
def clean_text(text) -> list:   # Function to clean the text
    text = [word.lower() for word in text]   # Convert all text to lower case
    text = [re.sub(r'[^a-z]', '', word) for word in text]   # Remove all non-alphabetical characters
    text = [word for word in text if word != '']   # Remove all empty strings
    cleaned_text = text   # Set the cleaned text to the text
    return cleaned_text

def frequency_list(text):    # Function to create a frequency list of words and sort it in reverse order
    freq_list = {}    # Define an empty dictionary
    for word in text:    # For each word in the text
        if word in freq_list:    # If the word is already in the dictionary
            freq_list[word] += 1    # Increment the count
        else:    # If the word is not in the dictionary
            freq_list[word] = 1    # Add the word and set the count to 1
    freq_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)    # Sort the dictionary in reverse order
    return freq_list    # Return the sorted dictionary

def to_json(freq_list):    # Function to convert the frequency list to a JSON file
    with open("freq_list.json", "w") as f:    # Open the JSON file
        json.dump(freq_list, f)    # Write the frequency list to the JSON file

def run_freq_list():    # Function to run the frequency list task    
    text = read_pdf()    # Read the text from the pdf
    tokens = tokenize(text)    # Tokenize the text
    no_stops = remove_stopwords(tokens)    # Remove stopwords from the text
    expanded = expand_contractions(no_stops)    # Expand contractions in the text
    cleaned_text = clean_text(expanded)    # Clean the text
    freq_list = frequency_list(cleaned_text)    # Create a frequency list of words
    to_json(freq_list)    # Convert the frequency list to JSON
    print("The frequency list has been created and saved as 'freq_list.json!")

def ui_freq_list():    # Function to handle user input for the frequency list task
    print("""
================================================================================================          
*** Welcome to the frequency list task! ***\n
This task will create a frequency list of words in the 
pdf file 'Neg Inversions_2018.pdf' and save it as a JSON file.
================================================================================================""")
    is_correct_task(run_freq_list)    # Run the frequency list task if it is the desired task
    repeat_task(run_freq_list)    # Run the frequency list task again if the user wants to
    
    

""" Task 4: Pride and Prejudice find similies """
""" From the Pride and Prejudice text, extract all sentences that might contain similes. Your output
needs to be saved as a file. Note that similes are often accompanied by the preposition like as in
the dog eats like a person. It would be best to remember that not all like are associated with
similes. For example, the sentence it seems like John is a loser is not a simile, though the like in
this sentence is also a preposition. """

def read_txt(filename):    # Function to read the text file
    with open(f"{filename}", "r") as f:    # Open the text file
        text = f.read()    # Read the text file
    return text    # Return the text
# ignore this function it was a first attempt, but i did not want to delete it yet
"""def identify_similies(text):    # Function to identify similies in the text
    doc = nlp(text)    # Create a spaCy document
    similies = []    # Define an empty list
    for token in doc:   # For each token in the document
        if token.dep_ == "advmod" and token.lemma_ == "like":   # If the token is an adverbial modifier and the lemma is like
            similie = []    # Define an empty list
            for child in token.head.children:   # For each child of the token
                similie.appened(child.text)    # Append the child to the list
            similies.append(" ".join(similie)) # Append the list to the similies list
    return similies # Return the similies list"""

# Second try at an identify similies function
def identify_similies(text):    # Function to identify similies in the text
    with concurrent.futures.ProcessPoolExecutor() as executor:  # Create a process pool executor
        doc = nlp(text)   # Create a spaCy document
        mask = (doc.dep_ == "advmod") & (doc.lemma_ == "like")  # Create a mask for the tokens
        similes = [executor.submit(" ".join, (child.text for child in token.head.children)) for token in doc[mask]]     # Create a list of tasks to identify similies
        results = [task.result() for task in similes]  # Results of the tasks
        return results  # Return the results

def run_pride_and_prejudice():   # Function to run the pride and prejudice task
    text = read_txt("prideprej.txt")   # Read the text from the text file
    #sentences = sent_tokenize(text)    # Tokenize the text into sentences
    similies = identify_similies(text)    # Identify similies in the text
    print(similies)
#run_pride_and_prejudice()

""" Task 5: Find people listed on the linguistics wikipedia page """
""" From the Wikipedia page on linguistics (https://en.wikipedia.org/wiki/Linguistics), extract all
PERSON-type entities and generate a frequency list of those entities. Who are the important
figures in linguistics? The best way to handle this question is to use SpaCy, which has the
PERSON tag for the .label_ attribute. """

def read_wiki():    # Function to read the text from the wikipedia page
    try:    # Try to read the text from the wikipedia page
        wiki_url = "https://en.wikipedia.org/wiki/Linguistics"    # Define the url
        response = requests.get(wiki_url)    # Get the response from the url
        soup = BeautifulSoup(response.text, "html.parser")    # Create a soup object
        text = soup.get_text()    # Get the text from the soup object
        return text    # Return the text
    except:    # If the text cannot be read
        print("Error reading the text from the wikipedia page")
        
def get_people(text):    # Function to get the people from the text
    doc = nlp(text)    # Create a spaCy document
    people = []    # Define an empty list
    for ent in doc.ents:    # For each entity in the document
        if ent.label_ == "PERSON":    # If the entity is a person
            people.append(ent.text)    # Append the entity to the list
        else:   # If the entity is not a person
            continue    # Continue to the next entity
    return people    # Return the list

def remove_linguistics(people):   # Function to remove the word linguistics from the list
    people = [person for person in people if person.lower() != "linguistics"]    # Remove the word linguistics from the list
    return people    # Return the list

def people_frequency_list(people):    # Function to create a frequency list of people
    freq_list = {}    # Define an empty dictionary
    for person in people:    # For each person in the list
        if person in freq_list:    # If the person is already in the dictionary
            freq_list[person] += 1    # Increment the count
        else:    # If the person is not in the dictionary
            freq_list[person] = 1    # Add the person and set the count to 1
    freq_list = sorted(freq_list.items(), key=lambda x: x[1], reverse=True)    # Sort the dictionary in reverse order
    return freq_list    # Return the sorted dictionary

def top_ten_people(freq_list):    # Function to print the top ten people
    print("The top ten people in linguistics are:")
    for i in range(10):    # For the first ten items in the list
        print(f"{i+1}. {freq_list[i][0]}")    # Print the person

def run_people():   # Function to run the people task
    text = read_wiki()    # Read the text from the wikipedia page
    people = get_people(text)    # Get the people from the text
    people = remove_linguistics(people)    # Remove the word linguistics from the list
    freq_list = people_frequency_list(people)    # Create a frequency list of people
    top_ten_people(freq_list)    # Print the top ten people

def ui_people():    # Function to run the people task from the user interface
    print("""
================================================================================================          
*** Welcome to the frequency list task! ***\n
This task will extract all PERSON-type entities from the linguistics 
Wikipedia page and generate a frequency list of those entities.
Along with the frequency list, the top ten people in linguistics will be printed.
================================================================================================""")
    is_correct_task(run_people)   # Run the people task
    repeat_task(run_people)    # Ask the user if they want to repeat the task
    

""" Task 6: Display the dependency parse for the 78th sentence of the linguistics wikipedia page """""
""" Using spaCy, display the dependency parse for the 78th sentence of the above Wikipedia page.
For this question, you need to refer to the spaCy manual available online. """

def get_sentence():    # Return the 78th sentence
    text = read_wiki()    # Read the text from the wikipedia page
    sentences = sent_tokenize(text)    # Tokenize the text into sentences
    return sentences[77]    # Return the 78th sentence
    
def display_dependency_parse(sentence):    # Function to display the dependency parse
    for token in sentence:    # For each token in the sentence
        return f"{token.text:12}{token.dep_:12}{token.head.text:12}{token.head.pos_:12}{[child for child in token.children]}"    # Print the token, dependency, head, head part of speech, and children

def run_dependency_parse():    # Function to run the dependency parse task
    sentence = get_sentence()    # Get the 78th sentence
    dependency_parse = display_dependency_parse(sentence)    # Display the dependency parse
    print(dependency_parse)    # Print the dependency parse

def ui_dependency_parse():    # Function to run the dependency parse task from the user interface
    print('''
================================================================================================
""" Task 7: Generate a tree diagram from a sentence """
""" Generate a tree diagram from a sententence """''')
        
# second attempt at the tree diagram this time using displacy
def generate_tree_diagram(sentence):    # Function to generate a tree diagram using displacy
    doc = nlp(sentence)    # Create a spaCy document
    for token in doc:    # For each token in the document
        print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])    # Print the token, dependency, head, head part of speech, and children
    tree = displacy.render(doc, style="dep", jupyter=False)    # Render the tree diagram
    with open("tree.html", "w", encoding="utf-8") as f:
        f.write(tree)
    
""" Whooooo! Last task! Task 8: Chunk a sentence into all NPs, PPs, and VPs """        

def chunk_sentence(sentence):   # Function to chunk a sentence using NLTK               # I had to look up the grammar for this one
    grammar = r"""
NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>}               # Chunk prepositions followed by NP
VP: {<MD>?<VB.*><NP|PP>*}    # Chunk verbs followed by optional modals, NP or PP
"""
    tokens = word_tokenize(sentence)    # Tokenize the sentence
    tagged = nltk.pos_tag(tokens)    # Tag the tokens
    chunker = nltk.RegexpParser(grammar)    # Create a chunker
    chunks = chunker.parse(tagged)    # Parse the tagged tokens
    return chunks    # Return the chunks
    
def run_chunk_sentence():    # Function to run the chunk sentence task
    sentence = "John believes that Mary loves him."    # Define the sentence
    chunks = chunk_sentence(sentence)    # Chunk the sentence
    print(chunks)    # Print the chunks
    chunks.draw()    # Draw the chunks


""" Main program loop """ 
def main():   # Main function
    mainflag = True  # Set the main flag to true
    while mainflag == True: # While the main flag is true
        menu()  # Call the menu function
        print("Enter a number to select a task or 'q' to quit.")    # Print the menu
        selection = input("Enter your selection: ")   # Get the user's selection
        match selection:    # Match the user's selection
            case '1':   # If the user selected task 1
                ui_capitalize()   # Call the ui_capitalize function
            case '2':   # If the user selected task 2
                ui_palindrome()  # Call the ui_palindrome function
            case '3':   # If the user selected task 3
                ui_freq_list()  # Call the ui_freq_list function
            case '4':   # If the user selected task 3
                print("\n***This task is not yet implemented.***")   # Print an error message
            case '5':   # If the user selected task 5
                ui_people()   # Call the ui_people function
            case '6':   # If the user selected task 6
                print("\n***This task is not yet implemented.***")   # Print an error message
            case '7':   # If the user selected task 7
                print("\n***This task is not yet implemented.***")   # Print an error message
            case '8':   # If the user selected task 8
                print("\n***This task is not yet implemented.***")   # Print an error message
            case 'q':   # If the user selected to quit
                print("Thank you for using this program! Goodbye!")  # Print a goodbye message
                mainflag = False    # Set the main flag to false
            case _:   # If the user selected an invalid option
                print("Invalid selection. Please try again.")   # Print an error message
                
if __name__ == '__main__':  # If the program is being run directly
    main()  # Call the main function