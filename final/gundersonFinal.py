"""
Code for the final exam by Evan Gunderson.
This code should be able to run correctly from the terminal with user input. *Must be run in Python 3.10 or higher*
Every task will be addressed in this program and will be identified by a triple quote comment.
To use this program, type the following in the terminal: python3.1x gundersonFinal.py
"""

# global imports
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import spacy
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
| 1. Capitalize a sentence correctly                |
| 2. Identify if a string is a palindrome           |
| 3. Generate a freq. list of words in a PDF        |
| 4. Pride and Prejudice similies                   |
| 5. People form Linguistics Wikipedia page         |
| 6. Use spaCy to find 78th sentence of wiki page   |
| 7. Generate tree diagram of a sentence            |
| 8. Chunk all NPs, PPs, and VPs from a sentence    |
|                                                   |
| *Type 'q' to quit*                                |
=====================================================
""")


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
*** Welcome to the Capitalize a sentence correctly task! ***
Is this the corect task? Type 'y' for yes or 'n' for no and return to the menu.
""")
    correct_task = input("Enter your selection: ")
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
    pass

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

def ui_freq_list():    # Function to run the frequency list task
    pass

def run_freq_list():    # Function to run the frequency list task    
    text = read_pdf()    # Read the text from the pdf
    tokens = tokenize(text)    # Tokenize the text
    no_stops = remove_stopwords(tokens)    # Remove stopwords from the text
    expanded = expand_contractions(no_stops)    # Expand contractions in the text
    cleaned_text = clean_text(expanded)    # Clean the text
    freq_list = frequency_list(cleaned_text)    # Create a frequency list of words
    to_json(freq_list)    # Convert the frequency list to JSON

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

def run_pride_and_prejudice():
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
run_people()




""" Main program loop """
def main():
    mainflag = True
    while mainflag == True:
        menu()
        print("Enter a number to select a task or 'q' to quit.")
        selection = input("Enter your selection: ")
        match selection:
            case '1':
                ui_capitalize()

            case 'q':
                print("Thank you for using this program! Goodbye!")
                mainflag = False
   
# Call the main function
#if __name__ == '__main__':
    main()